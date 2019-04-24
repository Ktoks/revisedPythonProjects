import math

class Movable:
    def __init__(self, mX, mY, mDX, mDY, mWorldWidth, mWorldHeight):
        self.mX = mX
        self.mY = mY
        self.mDX = mDX
        self.mDY = mDY
        self.mWWidth = mWorldWidth
        self.mWHeight = mWorldHeight
        self.mActive = True

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getWorldWidth(self):
        return self.mWWidth

    def getWorldHeight(self):
        return self.mWHeight

    def getActive(self):
        return self.mActive

    def setActive(self,active):
        self.mActive = active

    def move(self, dt):
        x = self.getX() + (self.getDX() * dt)
        y = self.getY() + (self.getDY() * dt)
        x %= self.getWorldWidth()
        y %= self.getWorldHeight()
        self.mX = x
        self.mY = y

    def hits(self,other):
        if not self.getActive() or not other.getActive():
            return False
        rad = self.getRadius() + other.getRadius() 
        d = math.sqrt(( other.getX() - self.getX())**2 + (other.getY() - self.getY())**2)
        if d <= rad:
            return True
        return False

    def accelerate(self, delta_velocity):
        raise NotImplementedError

    def evolve(self, dt):
        raise NotImplementedError

    def draw(self, surface):
        raise NotImplementedError

    def getRadius(self):
        raise NotImplementedError