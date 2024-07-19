# from ultralytics import YOLO
# import cv2
# from sort.sort import *
# from utils import get_car, read_license_plate, write_csv

# coco_model = YOLO("yolov8n.pt")
# license_plate_detector = YOLO("./license_plate_detector.pt")
# mot_tracker = Sort()

# results = {}

# cap = cv2.VideoCapture('./assets/sample.mp4')

# vehicles = [2, 3, 5, 7]

# # Detect Vehicles
# frame_nmr = -1
# ret = True 
# while ret:
#     frame_nmr += 1
#     ret, frame = cap.read()

#     if ret:
#         results[frame_nmr] = {}
#         detections = coco_model(frame)[0]
#         detections_ = []
#         for detection in detections.boxes.data.tolist():
#             x1, y1, x2, y2, score, class_id = detection
#             if int(class_id) in vehicles:
#                 detections_.append([x1, y1, x2, y2, score])

# # Track Vehicles
#         track_ids = mot_tracker.update(np.asarray(detections_))

# # Detect License Plate
#         if frame_nmr > 10:
#             break
        
#         else: license_plates = license_plate_detector(frame)[0]
#         for license_plate in license_plates.boxes.data.tolist():
#             x1, y1, x2, y2, score, class_id = license_plate

#             # Assign license plate to car
#             xcar1, ycar1, xcar2, ycar2, car_id =  get_car(license_plate, track_ids)

#             if car_id != -1:

#                 #crop license plate
#                 license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

#                 # Image processing
#                 license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
#                 _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

#                 # Read License Plate
#                 license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

#                 if license_plate_text is not None:
#                     results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]}, 'license_plate': {'bbox': [x1, y1, x2, y2], 'text': license_plate_text, 'bbox_score': score, 'text_score': license_plate_text_score}}

# # Write Results
# write_csv(results, './test.csv')

from ultralytics import YOLO
import cv2
import numpy as np
from sort.sort import *
from utils import get_car, read_license_plate, write_csv
import csv

# Initialize models and tracker
coco_model = YOLO("yolov8n.pt")
license_plate_detector = YOLO("./license_plate_detector.pt")
mot_tracker = Sort()

# IP Camera URL
ip_camera_url = 'http://<ip_camera_address>/video'

# Open the IP camera stream
cap = cv2.VideoCapture(ip_camera_url)

vehicles = [2, 3, 5, 7]  # List of vehicle classes to detect

# Prepare the CSV file
csv_file_path = './test.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frame', 'Car ID', 'Car BBox', 'License Plate BBox', 'License Plate Text', 'BBox Score', 'Text Score'])

frame_nmr = -1
while True:
    frame_nmr += 1
    ret, frame = cap.read()

    if not ret:
        break

    results = {}
    detections = coco_model(frame)[0]
    detections_ = []
    for detection in detections.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = detection
        if int(class_id) in vehicles:
            detections_.append([x1, y1, x2, y2, score])

    # Track Vehicles
    track_ids = mot_tracker.update(np.asarray(detections_))

    # Detect License Plates
    license_plates = license_plate_detector(frame)[0]
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate

        # Assign license plate to car
        xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

        if car_id != -1:
            # Crop license plate
            license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

            # Image processing
            license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
            _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

            # Read License Plate
            license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

            if license_plate_text is not None:
                results[frame_nmr] = {
                    car_id: {
                        'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                        'license_plate': {
                            'bbox': [x1, y1, x2, y2],
                            'text': license_plate_text,
                            'bbox_score': score,
                            'text_score': license_plate_text_score
                        }
                    }
                }

                # Write results to CSV file
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        frame_nmr,
                        car_id,
                        [xcar1, ycar1, xcar2, ycar2],
                        [x1, y1, x2, y2],
                        license_plate_text,
                        score,
                        license_plate_text_score
                    ])
    
    # Break the loop if needed (e.g., after a certain number of frames or based on a condition)
    # For now, it runs indefinitely until the camera stream is interrupted or manually stopped.
