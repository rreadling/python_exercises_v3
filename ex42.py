## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__ (self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__ (self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__ (self, name):
        ## ??
        self.name = name

        ## Person has- pet of some kind
        self.pet = None

    ## ??
    class Employee(Person):

        def __init__(self, name, salary):
            ## ?? hmm what is this strange magic?
            super(Employee, self).__init__(name)
            ## ??
            self.salary = salary

## ??
