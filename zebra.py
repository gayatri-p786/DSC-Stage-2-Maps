import cv2
import numpy as np

img = cv2.imread("zebra3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,
                           (15, 15), 6)

ret, thresh = cv2.threshold(blurred,
                            180, 255,
                            cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh.copy(),
                                  cv2.RETR_TREE,
                                  cv2.CHAIN_APPROX_SIMPLE)

rec = []

for c in contours:
    # if the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 2000:
        continue

    # get the min area rect
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    print("box:", box[0][0])
    rec.append((box[0][0], box[0][1]))
    rec.append((box[-1][0], box[-1][1]))
    # draw a red 'nghien' rectangle
    # cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# cv2.imwrite('zebra_lane1.jpg', img)

font = cv2.FONT_HERSHEY_COMPLEX
org = rec[-1]
fontScale = 0.5
thickness = 1

cv2.putText(img, 'Zebra', org, font,
            fontScale, (0, 0, 255), thickness)

cv2.rectangle(img, rec[1], rec[-1], (255, 0, 0), 2)

print("Rect list: ", rec)
# print("Rect coordi: ", rec[0][0])


cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
