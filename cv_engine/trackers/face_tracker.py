from ultralytics import YOLO


class FaceTracker:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self._model_path = model_path
        self._model = None

    @property
    def model(self):
        if self._model is None:
            self._model = YOLO(self._model_path)
        return self._model

    def track(self, frame):
        results = self.model.track(
            frame, tracker="bytetrack.yaml", persist=True, verbose=False
        )
        tracked = []
        if results[0].boxes.id is not None:
            for box, track_id in zip(results[0].boxes, results[0].boxes.id):
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                tracked.append({
                    "track_id": int(track_id.item()),
                    "bbox": [int(x1), int(y1), int(x2), int(y2)],
                    "confidence": box.conf[0].item(),
                })
        return tracked
