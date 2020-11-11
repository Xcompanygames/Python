import numpy as np
import cv2
import imutils


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver



def getContours(imgC,image):
    cnts = cv2.findContours(imgC.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if (M["m00"] == 0):
            M["m00"] = 1

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        # cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (5, 5, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (5, 5, 255), 2)
        cv2.waitKey(0)
def getContours_Flipped(imgC,image):
    # Find contours and hierarchy
    cnts_2, hier = cv2.findContours(imgC, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[
                   -2:]  # Use [-2:] for OpenCV 3, 4 compatibility.
    # Draw all contours with green color for testing
    # cv2.drawContours(image, cnts_2, -1, (0, 255, 0))
    # loop over the contours
    for c, h in zip(cnts_2, hier[0]):
        if h[3] > 0:
            # compute the center of the contour
            M = cv2.moments(c)
            if (M["m00"] == 0):
                M["m00"] = 1

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (5, 5, 255), -1)
            cv2.putText(image, "center", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (5, 5, 255), 2)


def getting_centers(image):
    #Setting kernel value for dilate
    kernel = np.ones((5, 5))

    # image processing

    # Convert to gray
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Dilate the image
    imageDilate  = cv2.dilate(imageGray, kernel, iterations=3)
    # Getting the image Canny
    imgCanny = cv2.Canny(imageDilate, 50, 50)
    ###################

    # flipped image processing
    # Erode the image
    ImageEroded = cv2.erode(image, kernel, iterations=1)
    # Dilate the image
    imageBlurred = cv2.GaussianBlur(ImageEroded, (5, 5), 0)
    # Convert to gray
    imageGray_AfterBlurring = cv2.cvtColor(imageBlurred, cv2.COLOR_BGR2GRAY)
    # Apply threshold, this will flip the board colors
    _, imageThresh = cv2.threshold(imageGray_AfterBlurring, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ###################
    ###################
    getContours(imgCanny,image)
    getContours_Flipped(imageThresh,image)
    ###################




# Load the image

image1 = cv2.imread('Resources/ChessBoard_Straight.jpg')
image2 = cv2.imread('Resources/ChessBoard_Straight2.jpg')
image3 = cv2.imread('Resources/ChessBoard_Straight3.jpg')
image4 = cv2.imread('Resources/ChessBoard_Straight4.jpg')
image5 = cv2.imread('Resources/ChessBoard_Straight5.jpg')

getting_centers(image1)
getting_centers(image2)
getting_centers(image3)
getting_centers(image4)
getting_centers(image5)

imgBlank = np.zeros_like(image1)
imgStack = stackImages(0.6,([image1,image2,image3],[image4,image5,imgBlank]))
cv2.imshow("Stack",imgStack)

cv2.waitKey(0)
