# Functions
**This session introduces one to functions and it's features.**

## Introduction
Let's start with an abstract example of echoes. When you shout out anything, lets say from a rocky mountain or valley, the message bounces back repeatedly, but with a loss in the amplitude and the actual message. Let's try recreating that as code using the stuff we learned in the last session. In order to do that, we'll use the following prompts:
- Allow the user to input any string
- Print a statement that states what is the message to be echoed
- Print the input in all uppercase first, followed by the original input, then the input in all lowercase [***HINT: .upper()***]
- To show data loss, we next print the input upto the second last character and then the third last character [***HINT: acess the range of the input string***]

**Script: [simple_echo](https://github.com/hsrwrobotics/Robotics_club_lectures/blob/master/Week%202/Functions/simple_echo.py)**


Assuming the code works, consider the scenario where now we need to use this echo "feature" multiple times in the same run/file, it would mean we would have to type out the entire 7-10 lines of code everytime we want to use it. 
This is where functions come in to play. Functions allow us to "reuse" an entire block of code as we see fit. The block of code that needs to be reused needs to be only written once inside the **function definition**. The function definition consistes of mainly 3 parts: **function name and arguments**, **body** and **return statements**. This next script details writing the echo feature as a function which uses a loop to show data loss (so that the input is echoed till its first character). 

**Script: [func_echo](https://github.com/hsrwrobotics/Robotics_club_lectures/blob/master/Week%202/Functions/func_echo.py)**

## Local variables and Return statements

***TBD***


**Script: []()**

## Recursive functions
Recursive functions are functions that call itself within its definition. A nifty feature when dealing with iterative processes that increment/decrement in fixed steps. The most common example to understand recursion is the calculation of factorial.
**Script: [func_fact](https://github.com/hsrwrobotics/Robotics_club_lectures/blob/master/Week%202/Functions/func_fact.py)**
