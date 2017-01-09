"""
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based
on arrival time) of all animals at the shelter or they can select whether
they prefer a dog or a cat (and receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data
structures to maintain this system and implement operations such as
enqueue, dequeueAny, dequeueDog and dequeueCat.
"""

from collections import deque
import pytest


class Animal(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return '%s(%s)' % (type(self), self._name)


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)



class Shelter(object):

    class _Animal(object):
        __last_id = 0

        def __init__(self, animal):
            self.animal = animal
            self.id = Shelter._Animal.__last_id = Shelter._Animal.__last_id + 1
            print self.id, self.animal


    def __init__(self):
        self._dogs = deque()
        self._cats = deque()


    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self._dogs.append(Shelter._Animal(animal))
        elif isinstance(animal, Cat):
            self._cats.append(Shelter._Animal(animal))
        else:
            raise AttributeError('this shelter only accepts dogs and cats')


    def dequeueAny(self):
        if not self._dogs: return self.dequeueCat()
        if not self._cats: return self.dequeueDog()

        print self._dogs[0].id, self._cats[0].id
        if self._dogs[0].id < self._cats[0].id: return self.dequeueDog()
        else: return self.dequeueCat()


    def dequeueDog(self):
        if not self._dogs: raise ValueError('no required animal available')
        return self._dogs.popleft().animal


    def dequeueCat(self):
        if not self._cats: raise ValueError('no required animal available')
        return self._cats.popleft().animal


def test_animal_shelter():
    shelter = Shelter()

    with pytest.raises(ValueError): shelter.dequeueAny()
    with pytest.raises(ValueError): shelter.dequeueDog()
    with pytest.raises(ValueError): shelter.dequeueCat()

    with pytest.raises(AttributeError): shelter.enqueue(2.0)

    cat_a = Cat('cat_a')
    cat_b = Cat('cat_b')
    shelter.enqueue(cat_a)
    shelter.enqueue(cat_b)
    with pytest.raises(ValueError): shelter.dequeueDog()

    dog_a = Dog('dog_a')
    dog_b = Dog('dog_b')
    cat_c = Cat('cat_c')
    shelter.enqueue(dog_a)
    shelter.enqueue(dog_b)
    shelter.enqueue(cat_c)

    assert shelter.dequeueAny() == cat_a
    assert shelter.dequeueDog() == dog_a
    assert shelter.dequeueCat() == cat_b
    assert shelter.dequeueAny() == dog_b
    assert shelter.dequeueAny() == cat_c
