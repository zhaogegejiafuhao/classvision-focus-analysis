from ultralytics import YOLO


class FaceDetector:
    def __init__(self, model_path: str = "models/yolov8n.pt"):
        self._model_path = model_path
        self._model = None

    @property
    def model(self):
        if self._model is None:
            self._model = YOLO(self._model_path)
        return self._model

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        detections = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "confidence": conf,
            })
        return detections
