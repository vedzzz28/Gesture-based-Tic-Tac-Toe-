import cv2
import mediapipe
import pyautogui
capture_hands = mediapipe.solutions.hands.Hands()
drawing_options = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()       #to get screen size 
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
    _,image = camera.read()
    image_height, image_width, _ = image.shape       #getting height and width of image ('_' means null depth )
    image =cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands: 
        for hand in all_hands:
            drawing_options.draw_landmarks(image,hand)                  #landmark points
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):    
                x = int(lm.x * image_width)             #to convert landmarks from float to integer 
                y = int(lm.y * image_height)            #to convert landmarks from float to integer
               # print(x,y)
                if id == 8:                                        #id 8 means forefinger
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    cv2.circle(image,(x,y),20,(0,255,255))         #to create circle on forefinger
                    pyautogui.moveTo(mouse_x,mouse_y)              # for mouse cursor draging     
                    x1 = x
                    y1 = y
                       
                if id == 4:                                        #id 4 means thumb
                    x2 = x
                    y2 = y 
                    cv2.circle(image,(x,y),20,(0,255,255))
        distance = y2 - y1              # finding vertical distance between 2 points
        print(distance)
        if(distance < 25):                 # if distance between fingers is close enough then click
            pyautogui.click()
                    
    cv2.imshow("Hand movement video capture",image)
    key = cv2.waitKey(100)
    if key == 27:
        break     
camera.release()
cv2.destroyAllWindows()               #press esc for closing camera 
