import math
from movable import Movable


class Rotatable(Movable):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        Movable.__init__(self, x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation

    def getRotation(self):
        return self.mRotation

    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        if self.mRotation < 0:
            self.mRotation += 360
        elif self.mRotation >= 360:
            self.mRotation -= 360

    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        rads = math.radians(rotation)
        newX = delta_velocity * math.cos(rads)
        newY = delta_velocity * math.sin(rads)
        return newX, newY

    def accelerate(self, delta_velocity):
        r = self.getRotation()
        x, y = self.splitDeltaVIntoXAndY(r, delta_velocity)
        self.mDX += x#
        self.mDY += y#

    def rotatePoint(self, x, y):
        distance = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        angle = math.radians(self.getRotation())
        newtheta = theta + angle
        dx = distance * math.cos(newtheta)
        dy = distance * math.sin(newtheta)
        return dx, dy

    def translatePoint(self, x, y):
        x += self.getX()
        y += self.getY()
        return x, y

    def rotateAndTranslatePoint(self, x, y):
        xr, yr = self.rotatePoint(x, y)
        xt, yt = self.translatePoint(xr, yr)
        return xt, yt

    def rotateAndTranslatePointList(self, point_list):
        newlist = []
        for point in point_list:
            newpoint = self.rotateAndTranslatePoint(point[0], point[1])
            newlist.append(newpoint)
        return newlist
