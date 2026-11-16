## [imports]
import cv2 as cv
import sys
## [imports]

## [imread]
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
## [imread]

## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]

## [imshow]
## [imshow]
cv.imshow("Display window", img)

# Use a timed loop to prevent the Python kernel from freezing
k = 0
while True:
    k = cv.waitKey(100) & 0xFF
    
    # If the window is closed, waitKey returns -1 on some backends, 
    # but on others it just stops updating. We check for the 'X' button 
    # using a try/except block for maximum portability.
    try:
        if cv.getWindowProperty("Display window", cv.WND_PROP_VISIBLE) < 1:
            break
    except cv.error:
        break
        
    # Break if Escape key is pressed
    if k == 27:
        break
    
    # Break if 's' is pressed to allow the save function to run
    if k == ord("s"):
        break
## [imshow]