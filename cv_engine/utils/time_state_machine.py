import time
from dataclasses import dataclass, field
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class PersonExamState:
    track_id: int

    gaze_deviation_start: float | None = None
    head_down_start: float | None = None

    head_turn_events: int = 0
    _last_yaw_normal: bool = True

    risk_level: RiskLevel = RiskLevel.LOW
    gaze_deviation_duration: float = 0.0
    head_down_duration: float = 0.0
    cheating_object_nearby: bool = False
    last_update: float = field(default_factory=time.monotonic)

    YAW_THRESHOLD: float = 15.0
    PITCH_THRESHOLD: float = 20.0
    SUSTAINED_SEC: float = 2.0
    TURN_COUNT_MEDIUM: int = 5
    TURN_COUNT_HIGH: int = 10


class ExamStateMachine:
    def __init__(self):
        self._states: dict[int, PersonExamState] = {}

    def update(
        self,
        track_id: int,
        pitch: float,
        yaw: float,
        fatigue: dict,
        cheating_nearby: bool = False,
        now: float | None = None,
    ) -> dict:
        if now is None:
            now = time.monotonic()

        state = self._states.get(track_id)
        if state is None:
            state = PersonExamState(track_id=track_id)
            self._states[track_id] = state

        # 偏视检测
        yaw_deviant = abs(yaw) > state.YAW_THRESHOLD
        if yaw_deviant:
            if state.gaze_deviation_start is None:
                state.gaze_deviation_start = now
            state.gaze_deviation_duration = now - state.gaze_deviation_start
        else:
            state.gaze_deviation_start = None
            state.gaze_deviation_duration = 0.0

        # 转头边沿检测
        yaw_normal = not yaw_deviant
        if not yaw_normal and state._last_yaw_normal:
            state.head_turn_events += 1
        state._last_yaw_normal = yaw_normal

        # 低头检测
        head_down = abs(pitch) > state.PITCH_THRESHOLD
        if head_down:
            if state.head_down_start is None:
                state.head_down_start = now
            state.head_down_duration = now - state.head_down_start
        else:
            state.head_down_start = None
            state.head_down_duration = 0.0

        # 作弊物品
        state.cheating_object_nearby = cheating_nearby

        # 风险等级
        state.risk_level = self._compute_risk(state)
        state.last_update = now

        return {
            "risk_level": state.risk_level.value,
            "gaze_deviation_duration": round(state.gaze_deviation_duration, 2),
            "head_down_duration": round(state.head_down_duration, 2),
            "head_turn_events": state.head_turn_events,
            "cheating_object_nearby": state.cheating_object_nearby,
        }

    def _compute_risk(self, state: PersonExamState) -> RiskLevel:
        # HIGH
        if state.gaze_deviation_duration >= state.SUSTAINED_SEC:
            return RiskLevel.HIGH
        if state.head_down_duration >= state.SUSTAINED_SEC and state.cheating_object_nearby:
            return RiskLevel.HIGH
        if state.head_turn_events >= state.TURN_COUNT_HIGH:
            return RiskLevel.HIGH

        # MEDIUM
        if state.gaze_deviation_duration >= 1.0:
            return RiskLevel.MEDIUM
        if state.head_down_duration >= 1.0:
            return RiskLevel.MEDIUM
        if state.head_turn_events >= state.TURN_COUNT_MEDIUM:
            return RiskLevel.MEDIUM
        if state.cheating_object_nearby:
            return RiskLevel.MEDIUM

        return RiskLevel.LOW

    def cleanup(self, active_ids: set[int]):
        stale = [tid for tid in self._states if tid not in active_ids]
        for tid in stale:
            del self._states[tid]
