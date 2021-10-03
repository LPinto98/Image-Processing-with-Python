import cv2
import numpy as np



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

logo = cv2.imread('your_watermark_image.png')
size = 100
logo = cv2.resize(logo, (size, size))

img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		frame = cv2.flip(frame, 1)
		roi = frame[-size-10:-10, -size-10:-10]
		roi[np.where(mask)] = 0
		roi += logo
		cv2.imshow('WebCam', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()