# Intrusion-Detection-and-Alert-System
The Intruder Detection System is a Python-based application that uses computer vision to detect intruders in real-time using a webcam. When an intruder is detected, the system captures an image, sends an email alert with the image attachment, and logs the time and location of the detection.
It is designed to monitor secure locations such as bank locker rooms, crime scenes, and other restricted areas. This feature facilitates prompt security alerts in the event of a breach, while the accompanying image attachments aid in the swift identification and capture of suspects.  
This project aims to provide a simple yet effective way to monitor and notify users of potential security breaches using readily available hardware and basic computer vision techniques.

## Features

- Real-time face detection using OpenCV's Haar Cascade Classifier.
- Capture and email alert functionality upon detecting an intruder.
- Log the timestamp and physical location (latitude and longitude) of the detection.
- Adjustable face detection sensitivity and notification settings.

## Installation Prerequisites

- Python 3.6 or higher
- OpenCV (cv2)
- NumPy
- Requests
- Geocoder

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/intruder-detection-system.git
   cd intruder-detection-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

- Set up a Gmail account for sending email alerts.
- Replace `email_sender` and `email_password` in the `send_email_alert` function with your Gmail credentials.

### Usage

1. Run the application:
   ```bash
   python intruder_detection.py
   ```
2. Adjust the camera to monitor the desired area.
3. When a face is detected, an email alert will be sent to the configured recipient.

## Contributing

Contributions are welcome! If you have suggestions, enhancements, or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

