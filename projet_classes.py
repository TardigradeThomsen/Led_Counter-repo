import cv2
import numpy as np


class CameraInterface:
    def __init__(self, camera_id: int = 0):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)

    @staticmethod
    def correct_orientation(frame: np.ndarray) -> np.ndarray:
        """Returns the frame with corrected orientation."""
        corrected_frame = np.rot90(frame)
        return corrected_frame

    def switch_camera(self) -> bool:
        """Switches to the next available camera and returns whether it was successful."""
        self.cap.release()
        for i in range(self.camera_id+1, 100):
            cap = cv2.VideoCapture(i)
            if cap is not None and cap.isOpened():
                self.camera_id = i
                self.cap = cap
                return True
        return False

    def get_frame(self, correct_orientation: bool = False) -> np.ndarray:
        """Returns a frame from the camera, with optional orientation correction."""
        ret, frame = self.cap.read()
        if ret:
            if correct_orientation:
                frame = self.correct_orientation(frame)
            return frame

    def get_camera_info(self) -> dict:
        """Returns a dictionary containing information about the camera."""
        info = {
            "frame_size": (self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            "fps": self.cap.get(cv2.CAP_PROP_FPS)
        }
        return info

    def release(self) -> None:
        """Releases the camera."""
        self.cap.release()

    def __del__(self) -> None:
        """Cleans up when the object is deleted."""
        self.release()
