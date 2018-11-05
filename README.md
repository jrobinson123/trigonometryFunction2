# trigonometryFunction2
A function written in python3 which can take in a horizontal distance and angle of elevation and print out an estimation of the height of an object

Consider when you look at the top of a building, there is the horizontal distnace between you and the building, the height of the building, and the angle of elevation that occurs from your line of sight

Heres a visual representation of this
![right triangle graphic](https://github.com/jrobinson123/trigonometryFunction2/blob/master/images/trigonometryGraphic.png)

From this graphic you can extract some of the variables in play when given this particular problem. Three key variables are used to solve the height:
- The angle of elevation: The angle of elevation that occurs between your line of sight and the line of the ground
- Distance: the horizontal distance between you and the object you're observing
- Observer height: The height of the observer(more precesilely the height of your eyes)

Then height can be solved using this equation:
height = tan(angle of elevation * distance + observer height

Here's a to scale, visual  representation of these variables


Based on the values of these variables we can solve for height 

height = tan(27) * 75 + 7 
height = (.5095 * 75) + 7
height = 38.2 + 7
height = 45.2

This computer program automates this project by taking in inputs, converting them to correpsonding variables,
then applying a mathematical function 

### Here's the code
```python

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






# trigonometryFunction2
A function written in python3 which can take in a horizontal distance and angle of elevation and print out an estimation of the height of an object


Heres a visual representation of the kind of problem this program could solve
