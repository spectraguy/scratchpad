# Object-oriented paradigm

Python is object-oriented like essentially every modern programming language.  Nearly everything is represented as an object.  To refer to a property of an object, use `.`.  For instance, if I have an object named `person`, I might expect `print(person.haircolor)` to print `Blond` to the console.  If I had an object named `company`, I might expect `print(company.president.haircolor)` to also print `Blond`, because the `president` property of `company` contained an object similar to my `person` object, and I know my `person` object had a property named `haircolor`.

Python modules are objects too.  So, if I have the line `import numpy as np`, I now have a object (which happens to be the numpy Python module) named `np` in my workspace.  One of the numpy module's properties is a function named `abs`, so I can call that function and print the result from passing -1 to that function with `print(np.abs(-1))`.  Or, if I just `print(np.abs)`, I'll see a somewhat-cryptic note trying to represent a function as a string that can be printed to the console.

A "Class" defines how a whole class of objects behaves.  For instance, let's define the data stored for each `Person` along with things we can do with a `Person`:

```python
class Person(object):
    def __init__(self, name, haircolor):
        self.haircolor = haircolor
        self.name = name

    def say_hi(self):
        print('Hi, my name is ' + self.name + ' and I have ' + self.haircolor + ' hair')

    def dye_hair(self, newcolor):
        self.haircolor = newcolor
```

A function defined, in general, for any instance of a class is called a "method".  The `__init__` method above is a special method that is called whenever an instance of a class is created.  Here's how to create two instances of the `Person` class:

```python
ben = Person(name='Ben', haircolor='brown')
lucy = Person(name='Lucy', haircolor='black')
```

We can access the data for one of the objects:

```python
print(ben.haircolor)

>>> brown
```

We can perform an action that any `Person` is capable of doing:

```python
lucy.say_hi()

>>> Hi, my name is Lucy and I have black hair
```

Note that the `ben` and `lucy` variables actually just contain *pointers* (or *references*) to the actual instance.  Consider this behavior:

```python
best_person = lucy
best_person.say_hi()
lucy.dye_hair('purple')
best_person.say_hi()

>>> Hi, my name is Lucy and I have black hair
    Hi, my name is Lucy and I have purple hair
```

The possibly-confusing thing is that we dyed `lucy`'s hair, but then observed `best_person`'s hair change color.  This is different behavior than when variables are stored *by value* rather than *by reference* -- Matlab stores everything *by value* unless specifically requested otherwise by a specially-defined class.  So, this behavior is probably more familiar:

```python
x = 1
y = x
print(y)
x = 2
print(y)

>>> 1
    1
```

The difference is because assignment *by value* copies/overwrites all data, whereas assignment *by references* only sets which object instance the variable is referring to.  The only way to create a new instance is with a constructor -- in this case, the syntax being `new_instance = Person(name='Foo', haircolor='bar')` which calls the special `__init__` method.  So, if you want to count how many instances of a class you have, just count the number of times the constructor is invoked -- the number of assignments (like `best_person = lucy`) is irrelevant because assignments merely change the pointer in the variable (`best_person` now points to the same instance of `Person` that `lucy` does), and not the instance.  The important take-away here is that a new instance is only created when a constructor is called.

There is far more depth regarding the object-oriented paradigm, but I think these are many of the important "gotchas" you'll likely encounter when trying to work with tools and systems designed with this paradigm.
