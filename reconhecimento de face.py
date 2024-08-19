import cv2
from cvzone.PoseModule import PoseDetector

"""
    This module estimates pose points of a human body using the
    mediapipe library.
"""

detector = PoseDetector()

# Initialize the camera object
cap = cv2.VideoCapture(0)

while True:
    # Capture video frame by frame using a loop
    success, img = cap.read()
    
    if not success:
        break

    # Send the frame to find the landmarks of the body
    img = detector.findPose(img)
    
    """
        Find the pose landmarks in an image of BGR color space.
        :param img: Image to find the pose in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
    """
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=True)  # Pay attention to indentation
    
    # Display the result
    cv2.imshow("Result", img)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
