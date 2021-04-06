class Person(object):
    def __init__(self, name, haircolor):
        self.haircolor = haircolor
        self.name = name

    def say_hi(self):
        print('Hi, my name is ' + self.name + ' and I have ' + self.haircolor + ' hair')

    def dye_hair(self, newcolor):
        self.haircolor = newcolor

ben = Person(name='Ben', haircolor='brown')
lucy = Person(name='Lucy', haircolor='black')

ben.say_hi()
lucy.say_hi()
