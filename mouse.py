import cv2
import mediapipe as mp
import util
import pyautogui
from pynput.mouse import Button, Controller 




mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,  #capturing the video hence image is False
    model_complexity = 1, # to get a better window
    min_detection_confidence = 0.7, # if it matches 70% to the hand then only detect it
    min_tracking_confidence = 0.7, # if it matches 70% to hand then only track it
    max_num_hands = 1 # max hand detected is 1
)
screen_width, screen_height = pyautogui.size()
mouse = Controller() 


def find_finger(processed):
    if processed.multi_hand_landmarks: 
        hand_landmarks = processed.multi_hand_landmarks[0] # if multi hand detected then take the first hand
        
        return hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP] #detects the index finger

        
    return None




def move_mouse(index_finger):
    if index_finger is not None:
        # gives actual position of index finger in the frame or the screen
        x = int(index_finger.x * screen_width)
        y = int(index_finger.y * screen_height)
        pyautogui.moveTo(x,y)

        
def left_click(landmarks_list, thumb_index_dist):
    #checks the conditions: thumb open, index finger bend, middle finger straight
    
    return (util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 60 and 
            util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and 
            thumb_index_dist > 10)
    
    
def right_click(landmarks_list, thumb_index_dist):
    # checks the conditons: thumb straight, index finger straight and middle finger bend

    return (util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90 and 
            util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 60 and 
            thumb_index_dist > 10)
    
    
def double_click(landmarks_list, thumb_index_dist):
    # checks the conditons: thumb straight, index finger straight and middle finger bend

    return (util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 60 and 
            util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 60 and 
            thumb_index_dist > 10)
    
    







def detect_gestures(frame, landmarks_list, processed):
    if len(landmarks_list)>=21:
        
        index_finger=find_finger(processed)
        # print(index_finger)
        
        thumb_index_dist=util.get_distance([landmarks_list[4], landmarks_list[5]]) # find the distance between point 4 of thumbs
                                                                                 # and point 5 of index finger

        
        # if the thumbs is closed i.e. distance between index and thumbs is less than 50 and index finger upright 
        # i.e. angle of index finger > 90 then move mouse accordingly
        if thumb_index_dist < 20 and (util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90):
                move_mouse(index_finger)
            
        
        ## LEFT CLICK
        elif left_click(landmarks_list, thumb_index_dist):
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2) # to put text on frame at 
                                                                                                 # (50,50) from the top 
            
        ## RIGHT CLICK
        elif right_click(landmarks_list, thumb_index_dist):
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        ## DOUBLE CLICK
        elif double_click(landmarks_list, thumb_index_dist): 
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)



def main():
    cap=cv2.VideoCapture(0)
    draw=mp.solutions.drawing_utils # to draw the lines and points on the hand

    try:
        while cap.isOpened():
            ret, frame=cap.read()  # ret returns true/ false if frame is opened or not and frame gives the video frame
            
            if not ret:
                break
            
            frame=cv2.flip(frame, 1) # to mirror the frame
            
            frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # frame takes color in BGR format so changing it to RGB
            processed=hands.process(frameRGB) #stores the porcessed outputs
            
            landmarks_list=[]
            
            if processed.multi_hand_landmarks: 
                hand_landmarks = processed.multi_hand_landmarks[0] # if multi hand detected then take the first hand
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x, lm.y)) # append the coordinates in the list in tuple form

                
            # print(landmarks_list)  ## to see it is append or not 
                    
            detect_gestures(frame, landmarks_list, processed)

            cv2.imshow('Virtual Mouse', frame) # to show the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):  # check after every 1ms and if q is pressed then exit... ord takes ascii value of q 
                break
            
            
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
        
if __name__ == '__main__':
    main()