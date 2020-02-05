## Python Traceback in General

There are several sections to every python traceback that are important. The diagram below was an attempt to help you see those different parts.

{% img 'python-traceback-diagram' centered=True %}

In python, it is best to read the traceback from the bottom moving up. In the last line of the traceback, I call the error message line which contains the exceptions and the name which was raised (outlined in blue). After the exception name is the error message (outlined in yellow). This message usually contains helpful information for understanding the reason for the exception being raised. Moving up the traceback (out-lined in green) are the different function calls moving from bottom to top, most recent to least recent. These calls are represented by two-line entries for each call. The first line of each call contains information like; the file name, line number and module name all specifying where the code can be found. The second line of these calls contains the actual code that was executed (underline in red).

There are a few differences between traceback outputs when executing your code in the `command-line` and running code in the `REPL`. Below is the same code from the previous section executed in a `REPL` and the resulting traceback output.

```python
>>> def greet(someone):
...    print('Hello, ' +someon)
... 
>>> greet("Chad")

Traceback (most recent call last):
  File "", line 1, in 
  File "", line 2, in greet
NameError: name 'someon' is not defined
```