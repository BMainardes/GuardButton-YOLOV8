# GuardButton
Security Button with Real-Time Object Detection

# Overview
This Course Completion Work (TCC) project aims to develop an integrated security system for companies, using a panic button connected to an Arduino and a real-time object detection system with YOLO. The system alerts authorities in the event of an emergency and uses machine learning to identify threats.

# Project Structure
Panic Button: A physical button connected to the Arduino that triggers an alert to authorities in the event of an emergency.
Object Detection with YOLO: Uses the YOLO network to detect objects in real time in images captured by security cameras.
Integration with Mobile Devices and Police Centers: Sends notifications and alerts to authorities, integrating with monitoring systems and mobile devices.
Technologies Used
Hardware:

Arduino UNO or Arduino Nano
Communication modules (GSM, Wi-Fi, LoRa)
Security cameras
Software:

Python for machine learning, backend and automation scripts
MySQL
Firebase or Twilio for sending notifications
Machine Learning:

YOLO (You Only Look Once): For real-time object detection

You can found and use my personal dataset in:
```
https://app.roboflow.com/guardianbutton/guns-detection-twpvd/deploy
```
Currently this dataset can only recognize weapons with an accuracy of 75.3%, but I am working to implement more classes in it and increase its accuracy., if you want to work with me and provide a larger dataset with another classes, please DM me 🙂

# Cloning the Repository
```
git clone https://github.com/BMainardes/GuardButton-YOLOV8.git
```
# Configuration and Installation
```
pip install -r requirements.txt
```
# Running
```
python GuardButton.py
```

