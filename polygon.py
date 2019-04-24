from rotatable import Rotatable
import math
import pygame

class Polygon(Rotatable):

    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)
        self.mPoly = []
        self.mColor = (255,255,255)

    def getPolygon(self):
        return self.mPoly

    def getColor(self):
        return self.mColor

    def setPolygon(self, points_list):
        self.mPoly = points_list

    def setColor(self, color):
        self.mColor = color

    def draw(self, surface):
        polyPoints = self.getPolygon()  # Fixes a timing issue where sometimes objects don't draw properly
        newpoints = self.rotateAndTranslatePointList(polyPoints)
        pygame.draw.polygon(surface, self.getColor(), newpoints)


    ##PART 2!!!!!!!!!!
    def getRadius(self):
        totaldistance = 0
        numOfPoints = 0
        # loop over the polygon and return the average distance away from the center location of the object
        for x, y in self.getPolygon():
            distance = math.sqrt(x**2 + y**2)
            totaldistance += distance
            numOfPoints += 1
        if numOfPoints > 0: # prevents division by zero
            return totaldistance / numOfPoints
        return totaldistance