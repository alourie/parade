#!/usr/bin/python

import sys

class City(object):
    def __init__(self, name):
        self.righties = []
        self.hasLefties = False
        self.name = name

    def addRight(self, city):
        if not (
            self.name == city.name or
            city.name in (righty.name for righty in self.righties)
        ): 
            self.righties.insert(0, city)
            city.hasLefties = True

    def hasAtRight(self, city):
        if self.name == city.name:
            return True
        for righty in self.righties:
            if righty.hasAtRight(city):
                return True
        return False

    def isFirst(self):
        if self.hasLefties:
            return False
        return True

    def getAll(self):
        allCities = [self.name]
        for citylist in (righty.getAll() for righty in self.righties):
            allCities.extend(citylist)
        return allCities


if __name__ == "__main__":
    tfile = sys.argv[1]
    content = []
    with open(tfile, 'r') as pf:
        content = pf.read().splitlines()

    cities = {}
    for line in content:
        line = line.split()
        city1, city2 = (
            cities[city] if city in cities 
            else City(city)
            for city in (line[0], ' '.join(line[3:]))
        )

        if 'after' == line[2]:
            city1, city2 = city2, city1

        if city2.hasAtRight(city1):
            raise 'Incorrect format!'
        else:
            city1.addRight(city2)

        for city in (city1, city2):
            cities[city.name] = city


    for city in cities.values():
        if city.isFirst():
            cities = city.getAll()
            for c in cities:
                print c
