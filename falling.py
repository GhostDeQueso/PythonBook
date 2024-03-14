
def main():

    for time in range(1, 11):
        distance = falling_distance(time)
        print(f"In {time:.1f} sec, it falling distance {distance:.2f} meters")
    




def falling_distance(time):
    g = 9.8 
    t = time ** 2
    distance = 0.5 * g * t
    return distance
    


main()