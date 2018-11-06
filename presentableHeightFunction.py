import math

#take input for observer height
observerHeight = int(input("What's your height(in feet) "))

#take input for horizontal distance
distance = int(input("What's the horizontal distance between you and the object you want to measure(in feet) "))

#input for the angle of elevation then conversin from degrees to radians
angleOfElevation = int(input("what angle did you measure between you and the object you want to measure(in degrees) "))
angleOfElevation = math.radians(angleOfElevation)

# function for solving height
def heightFinder(angleOfElevation_,distance_,observerHeight_):
    height = (math.tan(angleOfElevation_) * distance_) + observerHeight_

    #print statements for inputs
    print("angle of elevation {}".format(math.degrees(angleOfElevation_)))
    print("tangent of the angle of elevation {}".format(math.tan(angleOfElevation_)))
    print("distance {}".format(distance_))
    print("observer height(your height) {}".format(observerHeight_))
    return height


# running of the height solving functoi
finalHeight = heightFinder(angleOfElevation,distance,observerHeight)
print("this is the height of the object you observed: {}".format(finalHeight))
