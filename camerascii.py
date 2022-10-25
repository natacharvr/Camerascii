import cv2
import time
import os
vid = cv2.VideoCapture(0)
  
if not (vid.isOpened()):
    print("erreur d'ouverture de la caméra")

while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.resize(grey, (0,0), fx = 0.2, fy = 0.2)
    line = ""
    for pixx in range(0, len(grey), 2) :
        line += "\n"
        for pixy in range(0, len(grey[0]), 2) :
            if grey[pixx, pixy] in range(0, 40) :
                grey[pixx, pixy] = 0
                line += "@"
            elif grey[pixx, pixy] in range(40, 80) :
                line += "#"
                grey[pixx, pixy] = 40
            elif grey[pixx, pixy] in range(80, 120) :
                line += "*"
                grey[pixx, pixy] = 80
            elif grey[pixx, pixy] in range(120, 160) :
                line += "+"
                grey[pixx, pixy] = 120
            elif grey[pixx, pixy] in range(160, 200) :
                line += ":"
                grey[pixx, pixy] = 160
            elif grey[pixx, pixy] in range(200, 240) :
                line += "."
                grey[pixx, pixy] = 200
            elif grey[pixx, pixy] in range(240, 255) :
                line += " "
                grey[pixx, pixy] = 240
    os.system("cls")
    # Display the resulting frame
    cv2.imshow('frame', grey)
    print(line)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()