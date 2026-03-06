import cv2
from utils.config_loader import load_config


def start_camera(source):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Retail System Camera", frame)

        # press ESC to quit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    print("Starting Edge AI Retail System...")

    # Load configuration
    config = load_config()
    print("Loaded config:", config)

    # Get camera source from config
    camera_source = config["camera"]["source"]

    # Start camera
    start_camera(camera_source)


if __name__ == "__main__":
    main()