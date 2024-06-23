import cv2
import numpy as np
import os
import smtplib
import ssl
from email.message import EmailMessage
from imghdr import what
import geocoder  
from datetime import datetime
import pytz

# Initialize video capture
cap = cv2.VideoCapture(0)

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# Function to get current UTC time
def get_utc_time():
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    return utc_now.strftime('%Y-%m-%d %H:%M:%S UTC')

# Function to get current local time
def get_local_time():
    local_now = datetime.now()
    return local_now.strftime('%Y-%m-%d %H:%M:%S')

# Function to get physical location coordinates (using IP-based geolocation)
def get_physical_location():
    try:
        g = geocoder.ip('me')
        if g.ok:
            return g.latlng  
        else:
            return None
    except Exception as e:
        print(f"Error getting IP-based location: {e}")
        return None

# Function to send an email alert with time and location
def send_email_alert(image_encoded):
    email_sender = 'csedsproject@gmail.com'
    email_password = 'zblk pifm fxdc raqf'
    email_receiver = 'csedsproject@gmail.com'
    subject = "Alert: Intruder Detected"

    utc_time = get_utc_time()
    local_time = get_local_time()
    location = get_physical_location()
    if location:
        latitude, longitude = location
        body = f"An intruder was detected at {utc_time} (UTC) / {local_time} (local time) (UTC) in the location:  {latitude} latitude and  {longitude} longitude. The captured image is attached below."
    else:
        body = f"An intruder was detected at {utc_time} (UTC) / {local_time} (local time) . The captured image is attached below. Location information not available."

    # Creating email message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Attaching image
    em.add_attachment(image_encoded, maintype='image', subtype='jpeg', filename='suspect_image.jpg')

    # Creating SSL context for secure connection
    context = ssl.create_default_context()

    try:
        # Connecting to the Gmail server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

email_sent = 0  

# Starting an infinite loop to continuously capture frames from the camera
while True:
    ret, frame = cap.read() 

    if not ret:
        continue 

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting the frame to grayscale

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(faces) == 0:
        continue  

    for face in faces[:1]:  
        x, y, w, h = face  
        offset = 10  
        face_offset = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_selection = cv2.resize(face_offset, (100, 100)) 

        cv2.imshow("Face", face_selection)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (10, 0, 240), 2)

        if email_sent == 0:  
            image_encoded = cv2.imencode('.jpg', frame)[1].tobytes()
            print("Image taken successfully")
            send_email_alert(image_encoded)  
            email_sent += 1  

    cv2.imshow("faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
