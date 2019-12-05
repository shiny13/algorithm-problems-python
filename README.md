# Algorithm problems in Python
Interesting Algorithm problems solved using python

***Note: Please use Python3 as all the print messages and some inputs are taken that needs pyhton3*** 

## How to run
Simply navigate to the directory where the python program file is located that by using `cd` command.

Then run the program using `python3 <filename>.py`. An example is shown using the fibonacci problem file:
```
python3 fibonacci.py
```

If you have installed python with an installer and it created an alias for you, you may use the alias to run the program as well. I have the `py` aslias for `python3` in my computer. Therefore:
```
py fibonacci.py
```

## Input types for each program
Each file may require specific format or type of input, so please check the comments on the program to check what sort of input it expects. Then you can enter inputs according to what it expects to check the if the algorithm works or perhaps add additional stress testing code on it if you need to test it further.

I have used the following code in general for most of the inputs:
```
import sys

sys.stdin.read()
```

If this type is input is used, then the program will take as many inputs as you provide and only stop when you provide `Control-Z` for windows followed by enter or `Control-D` for Mac/Linux followed by enter.

