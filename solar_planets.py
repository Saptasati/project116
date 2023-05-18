import cv2

img = cv2.imread("PRO-C116-project-image-main-main/PRO-C116-project-image-main-main/solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255, 255, 255)
           )

cv2.putText(img,
            "Mercury",
            (110, 185),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.putText(img,
            "Venus",
            (190, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.putText(img,
            "Earth",
            (285, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.putText(img,
            "Moon",
            (340, 160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255, 255, 255)
           )

cv2.putText(img,
            "Mars",
            (375, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )
cv2.putText(img,
            "Jupiter",
            (560, 60),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.putText(img,
            "Saturn",
            (750, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )
cv2.putText(img,
            "Uranus",
            (950,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.putText(img,
            "Neptune",
            (1100, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
           )

cv2.imshow("output", img)
cv2.imwrite("Solar_system_with_name.jpg", img)
cv2.waitKey(0)