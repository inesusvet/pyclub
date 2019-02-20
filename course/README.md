# Cheatsheet on python syntax

1. How to create a variable for an _integer_?

```python
>>> one = 1
>>> one + 2
3
```

1. How to create a variable for a _float number_?

```python
>>> number = 2.5
>>> number ** 2
6.25
```

1. How to create a variable for a _string_?

```python
>>> text = 'James Bond 007'
>>> text[6:10]
'Bond'
>>> not_a_number = text[11:14]
>>> not_a_number
'007'
>>> number = int(not_a_number)
>>> number
7
>>> not_a_number = str(100500)
>>> not_a_number
'100500'
```

1. How could I crate _a list_ of string values?

```python
>>> l = ['apple', 'pear', 'grape']
>>> l[0]
'apple'
>>> l[-1]
'grape'
>>> l[1] = 'batman'
>>> l
['apple', 'batman', 'grape']
```

1. How could I create _a list_ of characters from a string?

```python
>>> chars = list('python')
>>> chars + ['i', 's', 't']
['p', 'y', 't', 'h', 'o', 'n', 'i', 's', 't']
```

1. How could I create _a dictionary_ with strings as keys and numbers as values?

```python
>>> grades = {'Styazhkin': 4, 'Skomorohova': 5, 'Kovrov': 5, 'Pupkin': 2}
>>> grades['Styazhkin']
4
>>> grades['Putin'] = 100500
>>> grades
{'Pupkin': 2, 'Skomorohova': 5, 'Styazhkin': 4, 'Putin': 100500, 'Kovrov': 5}
```

1. How to learn about the tools?

```python
type(), dir(), help()
```

1. How does _a function_ look like?

```python
>>> def humanize(time_in_seconds):
...     result = str(time_in_seconds % 60) + 's'
...     time_in_minutes = time_in_seconds // 60
...     if time_in_minutes > 0:
...         result = str(time_in_minutes % 60) + 'm ' + result
...     time_in_hours = time_in_minutes // 60
...     if time_in_hours > 0:
...         result = str(time_in_hours % 24) + 'h ' + result
...     time_in_days = time_in_hours // 24
...     if time_in_days > 0:
...         result = str(time_in_days % 7) + 'd ' + result
...     time_in_weeks = time_in_days // 7
...     if time_in_weeks > 0:
...         result = str(time_in_weeks) + 'w ' + result
...     return result
...
```

1. How does _a function call_ look like?

```python
>>> h = humanize(100500)
'1d 3h 55m 0s'
```

1. How does _class_ look like?

```python
class Person:
    organization = 'space'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
```

1. How to create an object of my class?

```python
>>> me = Person('Ivan', 'Styazhkin')
>>> me.organization
'space'
>>> me.get_full_name()
'Ivan Styazhkin'
>>> brother = Person('Vasily', 'Styazhkin')
>>> brother.name
'Vasily'
>>> brother.organization
'space'
```

1. How to do math calculations?

```python
>>> import math
>>> a, b = 2.5, 4
>>> length_of_hypotenuse = math.sqrt(a ** 2 + b ** 2)
```
