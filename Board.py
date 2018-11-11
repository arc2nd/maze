#!/usr/bin/env python

import types

import Tile

import numpy as np

class MazeBoard(object):
    def __init__(self, lenX, lenY):
        self.lenX = lenX
        self.lenY = lenY
        self.array = []
        for i in range((lenX * lenY)+1):
            self.array.append(None)
        self.matrix = np.arange(lenX * lenY).reshape(lenX,lenY)

    def find_free(self):
        freeX = freeY = None
        i = 0
        for c in self.array:
            if isinstance(c, types.NoneType): # not isinstance(c, Tile.MazeTile):
                freeX = i % self.lenX
                freeY = i / self.lenY
                return freeX, freeY
            i+=1
        return freeX, freeY
