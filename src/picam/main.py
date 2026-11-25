from picamera2 import Picamera2, Preview
import time

def main() -> None:
    camera = Picamera2()
    camera_config = camera.create_preview_configuration()
    camera.configure(camera_config)
    camera.start_preview(Preview.DRM)
    camera.start()
    time.sleep(2)
    camera.capture_file("/tmp/test.jpg")

if __name__ == "__main__":
    main()