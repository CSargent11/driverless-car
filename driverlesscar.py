class DriverlessCar:
    def __init__(self):
        self.speed = 0
        self.state = "stopped"
        self.brake_system = BrakeSystem()
        self.lidar_sensor = LightDetectionRanging()
        self.camera = Camera()

    def accelerate(self):
        self.speed += 1
        print("Accelerating. Speed:", self.speed)
        

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
        print("Decelerating. Speed:", self.speed)

    def drive(self, target_speed: int):
        while self.speed!=target_speed:
            self.accelerate()
        # Accelerate the car until the target speed is reached
        #self.speed = 0
        self.state = "driving"
        print("Car driving.")

    def stop(self):
        while self.speed>0:
            self.brake_system.applyBrake()
            self.decelerate()
        self.state = "stopped"
        # Decelerate the car until the speed reaches 0
        
        print("Car stopped.")

    def park(self):
        self.speed = 0
        self.state = "parked"
        self.brake_system.applyBrake()
        print("Car parked.")
        # Set the car's state as "parked"


class BrakeSystem:
    def __init__(self):
        self.brakeLights = BrakeLights()

    def applyBrake(self):
        self.brakeLights.turnOn()
        print("Brake applied.")

    def releaseBrake(self):
        self.brakeLights.turnOff()
        print("Brake released.")


class BrakeLights:
    def __init__(self):
        self.status = False

    def turnOn(self):
        self.status = True
        print("Brake lights turned on.")

    def turnOff(self):
        self.status = False
        print("Brake lights turned off.")

class BrakeLightDetector:
    def __init__(self):
        self.camera = Camera()

    def detect_brake_lights(self):
        image = self.camera.capture_image()
        brake_light_status = self.process_image(image)
        return brake_light_status

    def process_image(self, image):
        # Simulating image processing to detect brake lights
        # Replace this with your actual image processing algorithm
        if "brake lights on" in image.lower():
            return True
        else:
            return False

class LightDetectionRanging:
    def __init__(self):
        self.object_distance = 0

    def measureDistance(self):
        # Simulating distance measurement
        self.object_distance = 50 # meters

        # Simulating the distance rate of change from car to object
        self.distance_rate_change = 10 # meters per second
        print("Object Distance measured:", self.object_distance)

class RoadSignDetection:
    def __init__(self):
        self.camera = Camera()

    def detect_sign(self):
        image = self.camera.capture_image()
        sign_text = self.ocr(image)
        return sign_text

    def ocr(self, image):
        # Simulating optical character recognition (OCR)
        # Replace this with your actual OCR implementation
        return "Stop" if "STOP" in image else "Unknown"

class Camera:
    def __init__(self):
        self.image = None

    def capture_image(self):
        # Simulating image capture
        self.image = "Captured image of road sign"
        print("Image captured.")

    def capture_image(self):
        # Simulating image capture
        image = "Captured image of brake lights"
        return image

# Example usage
car = DriverlessCar()
car.drive(target_speed=100)

road_sign_detection = RoadSignDetection()
sign_text = road_sign_detection.detect_sign()
print("Detected Road Sign:", sign_text)

# Simulating the need to stop due to object detected by Lidar
car.lidar_sensor.measureDistance()
if car.lidar_sensor.object_distance < 10 or car.lidar_sensor.distance_rate_change>5:
    car.stop()

# Simulating the need to stop due to an obstacle detected by the camera
car.camera.capture_image()
if car.camera.image is not None:
    car.stop()


def test_driverless_car():
    car = DriverlessCar()
    car.drive(target_speed=100)
    assert car.speed == 100
    assert car.state == "driving"

    car.stop()
    assert car.speed == 0
    assert car.state == "stopped"

    car.park()
    assert car.speed == 0
    assert car.state == "parked"

# Run the test
test_driverless_car()