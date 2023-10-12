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

def tim_sort(arr, min_merge = 1):
    n = len(arr)
    
    r = 0
    while n >= min_merge:
        r |= n & 1
        n >>= 1
        
    minRun = n + r

    for left in range(0, n, minRun):
        right = min(left + minRun - 1, n - 1)
        
        for i in range(left + 1, right + 1):
            j = i
            
            while j > left and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

    size = minRun
    while size < n:
        for l in range(0, n, 2 * size):
            m = min(n - 1, l + size - 1)
            r = min((l + 2 * size - 1), (n - 1))
            
            if m < r:
                len1, len2 = m - l + 1, r - m
                left, right = [], []
                
                for i in range(0, len1):
                    left.append(arr[l + i])
                    
                for i in range(0, len2):
                    right.append(arr[m + 1 + i])
                    
                i, j, k = 0, 0, l
                while i < len1 and j < len2:
                    if left[i] <= right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                while i < len1:
                    arr[k] = left[i]
                    k += 1
                    i += 1

                while j < len2:
                    arr[k] = right[j]
                    k += 1
                    j += 1
                    
        size = 2 * size
        
    return arr
    
def num_sort(arr):
    a = []
    for i in arr:
        if type(a[int(i)]) != "list":
            a[int(i)] = []
        a[int(i)].append(i)
        
    b = []
    for x in a:
        for y in x:
            if y > 1:
                b.append(y)
    return b
