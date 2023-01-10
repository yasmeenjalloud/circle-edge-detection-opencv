import cv2 as cv
cap = cv.VideoCapture(0)    
while True:
    isSuccess, img = cap.read()
    cv.putText(img, 'Edge Detection', (100, 225),
    cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv.circle(img, (50, 50), 30, (100, 20, 200), thickness=3)
    cv.circle(img, (600, 50), 30, (100, 20, 200), thickness=3)
    cv.circle(img, (50, 400), 30, (100, 20, 200), thickness=3)
    cv.circle(img, (600, 400), 30, (100, 20, 200), thickness=3)
    Img_gray = cv.imread('doc.png', 0)
    blur_img = cv.GaussianBlur(Img_gray, (5, 5), 0)
    edge_img = cv.Canny(blur_img, 100, 100)
    cv.imshow('Canny Edge Image', edge_img)
    cv.imshow('Circle image', img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break