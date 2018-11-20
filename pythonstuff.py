>> planet = 'Pluto'
>>> print(planet)
Pluto
>>> moon = 'Charon'
>>> p = planet
>>> p
'Pluto'
>>> planet = 9
>>> 9
9
>>> planet
9
>>> planet = 'Sedna'
>>> print(plant)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'plant' is not defined
>>> string = "two"
>>> number = 3
>>> print(string * number)
twotwotwo
>>> print(int('2') + 3)
5
>>> print('2' + str(3))
23
>>> 3 < 5
True
>>> 3 != 5
True
>>> 3 == 5
False
>>> 3 >= 5
False
>>> 1 < 3 <5
True
>>> course = Python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Python' is not defined
>>> "course" = python
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> course = 'python'
>>> rating = '7'
>>> print (course + rating)
python7
>>> a = '3'
>>> b = '4'
>>> print (a** + b**)
  File "<stdin>", line 1
    print (a** + b**)
                    ^
SyntaxError: invalid syntax
>>> print ((a*a) + (b*b))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> print(int(a*a)+int(b*b))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> asquared = (a^2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ^: 'str' and 'int'
>>> a
'3'
>>> a*a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> int(a)*int(a)
9
>>> asquared = int(a)*int(a)
>>> bsquared = int(b)*int(b)
>>> asquared
9
>>> bsquared
16
>>> csquared = int(asquared)+int(bsquared)
>>> csquared
25
>>> 25**0.5
5.0
>>> type(a)
<class 'str'>
>>> a(type)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> type(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> type(asquared)
<class 'int'>
>>> type(bsquared)
<class 'int'>
>>> type(csquared)
<class 'int'>
>>> type(25**0.5)
<class 'float'>
>>> print(a + " squared equals " + b + " squared + " + c + " squared.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> c = (int(a**2) + int(b**2) * 0.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> print(a + " squared equals " + b + " squared + ")
3 squared equals 4 squared + 
>>> print(a + " squared equals " + b + " squared ")
3 squared equals 4 squared 
>>> a = str(a)
>>> b = str(b)
>>> c = str(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> c = (0.5 * (int(b**2) + (int(c**2)))
... 
... 
... c
  File "<stdin>", line 4
    c
    ^
SyntaxError: invalid syntax
>>> c = (0.5 * (int(b**2) + (int(a**2)))
... 
... 
... c
  File "<stdin>", line 4
    c
    ^
SyntaxError: invalid syntax
>>> c = (0.5 * (int(b)**2) + (int(a)**2)))
  File "<stdin>", line 1
    c = (0.5 * (int(b)**2) + (int(a)**2)))
                                         ^
SyntaxError: invalid syntax
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> a
'3'
>>> type(a)
<class 'str'>
>>> type(csquared)
<class 'int'>
>>> a = (asquared **0.5)
>>> a
3.0
>>> b = (bsquared **0.5)
>>> c = (csquared **0.5)
>>> c
5.0
>>> b
4.0
>>> a = str(a)
>>> b = str(b)
>>> c = str(c)
>>> print(a + " squared equals " + b + " squared + c + " squared)
  File "<stdin>", line 1
    print(a + " squared equals " + b + " squared + c + " squared)
                                                               ^
SyntaxError: invalid syntax
>>> print(a + " squared equals " + b + " squared + c + " squared ")
  File "<stdin>", line 1
    print(a + " squared equals " + b + " squared + c + " squared ")

