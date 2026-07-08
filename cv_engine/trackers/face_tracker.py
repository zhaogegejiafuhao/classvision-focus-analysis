import cv2
from ultralytics import YOLO

COCO_NAMES = {
    0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 5: "bus",
    7: "truck", 9: "traffic light", 11: "stop sign", 13: "bench",
    15: "cat", 16: "dog", 24: "backpack", 26: "handbag", 28: "suitcase",
    31: "tie", 56: "chair", 57: "couch", 58: "potted plant", 59: "bed",
    60: "dining table", 61: "toilet", 62: "tv", 63: "laptop", 64: "mouse",
    65: "remote", 66: "keyboard", 67: "cell phone", 73: "book", 74: "clock",
    75: "vase", 76: "scissors", 77: "teddy bear", 78: "hair drier", 79: "toothbrush",
}

CHEATING_OBJECT_CLASSES = {67: "cell phone", 63: "laptop", 73: "book", 28: "suitcase"}


class FaceTracker:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self._model_path = model_path
        self._model = None
        self._face_cascade = None
        self._next_fallback_id = 10000

    @property
    def model(self):
        if self._model is None:
            self._model = YOLO(self._model_path)
        return self._model

    def track(self, frame):
        results = self.model.track(
            frame, tracker="bytetrack.yaml", persist=True, verbose=False, conf=0.15
        )
        persons = []
        objects = []
        yolo_person_bboxes = []

        if results[0].boxes.id is not None:
            for box, track_id in zip(results[0].boxes, results[0].boxes.id):
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                cls_id = int(box.cls[0].item())
                item = {
                    "track_id": int(track_id.item()),
                    "bbox": [int(x1), int(y1), int(x2), int(y2)],
                    "confidence": box.conf[0].item(),
                    "class_id": cls_id,
                    "class_name": COCO_NAMES.get(cls_id, f"class_{cls_id}"),
                }
                if cls_id == 0:
                    persons.append(item)
                    yolo_person_bboxes.append((int(x1), int(y1), int(x2), int(y2)))
                elif cls_id in CHEATING_OBJECT_CLASSES:
                    item["is_cheating_object"] = True
                    objects.append(item)
                else:
                    objects.append(item)

        # 兜底：YOLO 没检测到人时用 OpenCV 人脸检测
        if len(persons) == 0:
            try:
                if self._face_cascade is None:
                    self._face_cascade = cv2.CascadeClassifier(
                        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
                    )
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self._face_cascade.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=4, minSize=(60, 60)
                )
            except Exception:
                faces = []
            for (fx, fy, fw, fh) in faces:
                # 检查这个人脸是否已经被 YOLO person 框包含
                face_cx, face_cy = fx + fw // 2, fy + fh // 2
                contained = any(
                    x1 <= face_cx <= x2 and y1 <= face_cy <= y2
                    for x1, y1, x2, y2 in yolo_person_bboxes
                )
                if not contained:
                    self._next_fallback_id += 1
                    persons.append({
                        "track_id": self._next_fallback_id,
                        "bbox": [int(fx), int(fy), int(fx + fw), int(fy + fh)],
                        "confidence": 0.5,
                        "class_id": 0,
                        "class_name": "person",
                    })

        return persons, objects
