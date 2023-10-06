import numpy as np

# get the point between 2 points in 3d space based on t
# example, at t=0.5 it will get the position half way through these 2 points
def linear_interpolation(p1: tuple, p2: tuple, t: int):
    return np.add(p1, np.multiply(np.subtract(p2, p1), t))


def hydrophone_triangulation(left_time, front_time, right_time):
    front_angle = 60 #! currently assuming the hydrophones are placed as an equilateral triangle
    left_angle = 60 # will be used when i update this not to be equilateral triangle only
    right_angle = 60 # will be used when i update this not to be equilateral triangle only
    true_heading = 1 #? set it as 1 here so we can set a negative based on the detected quadrant
    
    if front_time >= left_time:
        if front_time >= right_time:
            # Quadrant 1 #? Center of the 3 hydrophones is the origin point (0, 0)
            distance_between_points = 1500*front_time - 1500*right_time
            
        elif right_time > front_time:
            # Quadrant 3
            true_heading *= -1
            distance_between_points = 1500*right_time - 1500*left_time
            
    else:
        if left_time > right_time:
            # Quadrant 4
            distance_between_points = 1500*left_time - 1500*right_time
            
        elif right_time > left_time:
            # Quadrant 2
            true_heading *= -1
            distance_between_points = 1500*right_time - 1500*front_time
            
    distance_between_points = abs(distance_between_points) #? if its negative its basically in the sub, im abs-ing it just to be safe when it gets down close to or past zero (-0.00001)
    time_between_points = distance_between_points/1500
    distance_to_origin = abs(distance_between_points/np.sqrt(3))
    #all the math is based on the left angle, too lazy to change it rn, fyi we are using the cosine rule to calculate everything
    angle_left = np.degrees(np.arccos((left_time**2 + time_between_points**2 - front_time**2)/(2*left_time*time_between_points)))
    angle_front = np.degrees(np.arccos((left_time**2 - time_between_points**2 - front_time**2)/(-2*left_time*front_time)))
    angle_right = np.degrees(np.arccos((front_time**2 - left_time**2 - right_time**2)/(-2*left_time*right_time)))
    angle_target = np.arccos((left_time**2 + front_time**2 - time_between_points**2)/(2*left_time*front_time))
    true_heading *= (180 - angle_front - front_angle/2)
    x = (distance_to_origin/np.sin(angle_target/2))*np.sin(np.radians(angle_left+front_angle/2)) #? i think this is right?
            
    
    return (x, true_heading)

print(hydrophone_triangulation(0.00067, 0.0011547, 0.00133))
