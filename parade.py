#!/usr/bin/python

import sys

class City(object):
    def __init__(self, name):
        self.lefties = self.righties = None
        self.name = name 
        self.score = None

    def addLeft(self, city, updateScore=False):
        if (
            self.score is not None and
            city.score is not None
        ):
            if self.score > city.score:
                pass
            else:
                updateScore = True

        if (
            self.score is None and
            city.score is None
        ):
            self.score = 1
            city.score = 0
        elif (
            self.score is not None and
            city.score is None
        ):
            city.score = self.score - 1
        elif (
            self.score is None and
            city.score is not None
        ):
            self.score = city.score + 1
        
        # Both are not none:
        else:
            city.score = (self.score + self.lefties[-1] ) / 2
            city.updateLefties(city.score, self.lefties[-1])

        self.lefties.append(city)
        city.righties[0] = self

    def updateLefties(self, baseScore, minimalScore):
        for lefty in self.lefties:
            if (
                lefty.score > baseScore or
                lefty.score < minimalScore
            ):
                lefty.score = (baseScore + minimalScore) / 2
                lefty.updateLefties(lefty.score, minimalScore)

    def hasLeft(self, city):
        for lefty in self.lefties:
            if (
                lefty == city or
                lefty.hasLeft(city)
            ):
                return True
            
    def addRight(self, city, updateScore=False):
        if (
            self.score is not None and
            city.score is not None
        ):
            if self.score < city.score:
                return
            else:
                updateScore = True

        if updateScore:
            if (
                self.score is None and
                city.score is None
            ):
                self.score = 0
                city.score = 1
            elif (
                self.score is not None and
                city.score is None
            ):
                city.score = self.score + 1
            elif (
                self.score is None and
                city.score is not None
            ):
                self.score = city.score - 1
            
            # Both are not none:
            else:
                city.score = (self.score + self.righties[0] ) / 2
                city.updateLefties(city.score, self.righties[0])

        self.righties[0] = city
        city.lefties.append = self

    def updateRighties(self, baseScore, minimalScore):
        for righty in self.righties:
            if (
                righty.score < baseScore or
                righty.score > minimalScore
            ):
                righty.score = (baseScore + minimalScore) / 2
                righty.updateRighties(righty.score, minimalScore)

    def hasRight(self, city):
        for righty in self.righties:
            if (
                righty == city or
                righty.hasRight(city)
            ):
                return True
            


if __name__ == "__main__":
    tfile = sys.argv[3]
    content = []
    with open(tfile, 'r') as pf:
        content = pf.read().splitlines()

    cities = {}
    for line in content:
        city1, city2 = (
            cities[city] if city in cities 
            else City(city)
            for city in (line[0], line[2])
        )

        if 'before' == line[3]:
            if city2.hasLeft(city1):
                pass
            elif city2.hasRight(city1):
                raise 'Incorrect format!'
            else:
                city2.addLeft(city1)
        elif 'after' == line[3]:
            if city2.hasRight(city1):
                pass
            elif city2.hasLeft(city1):
                raise 'Incorrect format!'
            else:
                city2.addRight(city1)



