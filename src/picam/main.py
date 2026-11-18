from picamera2 import Picamera2

def main() -> None:
    camera = Picamera2()
    camera.start()
    camera.capture_file("/tmp/test.jpg")
    camera.stop()
    print("Saved /tmp/test.jpg")

if __name__ == "__main__":
    main()