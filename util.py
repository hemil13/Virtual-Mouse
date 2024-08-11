import numpy as np

def get_angle(a,b,c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0]) # distance between cb and ab WRT x-axis
    angle=np.abs(np.degrees(radians)) # converting it to degrees and absoluting the value
    return angle


def get_distance(landmark_list):
    if len(landmark_list)<2:
        return
    
    
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    l=np.hypot(x2-x2, y2-y1) #gets the distance
    return np.interp(l, [0,1],[0,1000]) # l gives value between 0-1 to increasing the range to 0-1000
        
    