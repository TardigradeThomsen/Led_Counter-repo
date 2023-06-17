from projet_classes import CameraInterface
import cv2


def main():
    cam = CameraInterface(camera_id=4)

    while True:
        frame = cam.get_frame()
        cv2.imshow("frame", frame)
        key = cv2.waitKey(30)
        if key == ord('q'):
            break


if __name__ == '__main__':
    main()

