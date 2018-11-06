# trigonometryFunction2

Consider when you look at the top of a building, there is the horizontal distnace between you and the building, the height of the building, and the angle of elevation that occurs from your line of sight

The program I wrote is a function which can take in a horizontal distance and angle of elevation, and a users height and print out and estimation of the height of the object you're looking at

Heres a visual representation of this
![right triangle graphic](https://github.com/jrobinson123/trigonometryFunction2/blob/master/images/trigonometryGraphic.png)

From this graphic you can extract some of the variables in play when given this particular problem. Three key variables are used to solve the height:
- The angle of elevation: The angle of elevation that occurs between your line of sight and the line of the ground
- Distance: the horizontal distance between you and the object you're observing
- Observer height: The height of the observer(more precesilely the height of your eyes)

Then height can be solved using this equation:
height = tan(angle of elevation * distance + observer height

Here's a to scale, visual  representation of these variables
![to scale visual representation] (https://github.com/jrobinson123/trigonometryFunction2/blob/master/images/toScaleVisualRepresentation.png)


Based on the values of these variables we can solve for height 

height = tan(27) * 75 + 7 

height = (.5095 * 75) + 7

height = 38.2 + 7

height = 45.2

This computer program automates this project by taking in inputs, converting them to correpsonding variables,
then applying a mathematical function 

### Here's the code
```python
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


```



### dependencies
built with python 3.6 using the built in math library

###  User Inputs 
* User's height
* distance from object
* angleOfElevation

### Usage
To run this program:
```shell
python3 finalHeightFunction.py
```







