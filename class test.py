# a class sample copied from network
class A(object):
    def __init__(self):
        self.x = 'Hello'

    #print out test
    def out(self, foo):
        print self.x + ' ' + foo


a = A()             # We do not pass any argument to the __init__ method
a.out('Sailor!')    # We only pass a single argument


# a test code for Class ans Object
class myObj:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def out(self):
        print('ID is: ' + str(self.id) + ', Name is ' + self.name)


obj = myObj(1, 'this')
obj.out()


class Shark:
    def __init__(self):
        print("This is the constructor method.")


sh = Shark()
