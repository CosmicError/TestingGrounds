import numpy as np

def hydrophone_triangulation(t2, t1, t3):
    front_angle = 60 #! currently assuming the hydrophones are placed as an equilateral triangle
    #left_angle = 60 # will be used when i update this not to be equilateral triangle only
    #right_angle = 60 # will be used when i update this not to be equilateral triangle only
    true_heading = 1 #? set it as 1 here so we can set a negative based on the detected quadrant
    d2h = ...
    
    if t1 >= t2:
        if t2 >= t3:
            # Quadrant 1 #? Center of the 3 hydrophones is the origin point (0, 0)
            d2h = 1500*t1 - 1500*t3
            
        elif t3 > t2:
            # Quadrant 3
            true_heading *= -1
            d2h = 1500*t3 - 1500*t2
            
    else:
        if t2 > t3:
            # Quadrant 4
            d2h = 1500*t2 - 1500*t3
            
        elif t3 > t2:
            # Quadrant 2
            true_heading *= -1
            d2h = 1500*t3 - 1500*t1
    
    #Calculate source heading
    d2h = abs(d2h) #The distance between each hydrophone (assuming they're all equal distance apart)
    t4 = d2h/1500 #The time it takes to go between each hydrophone (assuming they're all equal distance apart)
    A = np.degrees(np.arccos((t2**2 - t4**2 - t1**2)/(-2*t2*t1)))
    true_heading *= (180 - A - front_angle/2)
    #C = np.degrees(np.arccos((t1**2 - t2**2 - t3**2)/(-2*t2*t3)))
    
    #Calculate distance to source
    distance_to_origin = abs(d2h/np.sqrt(3)) #The distance to the center of the 3 hydrophones
    B = np.degrees(np.arccos((t2**2 + t4**2 - t1**2)/(2*t2*t4)))
    D = np.arccos((t2**2 + t1**2 - t4**2)/(2*t2*t1))
    x = (distance_to_origin/np.sin(D/2))*np.sin(np.radians(B+front_angle/2)) #? i think this is right?
    
    return (x, true_heading)

print(hydrophone_triangulation(0.00067, 0.0011547, 0.00133))

# get the point between 2 points in 3d space based on t
# example, at t=0.5 it will get the position half way through these 2 points
def linear_interpolation(p1: tuple, p2: tuple, t: int):
    return np.add(p1, np.multiply(np.subtract(p2, p1), t))

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
