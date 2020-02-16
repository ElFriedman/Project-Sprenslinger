import arcade
import os
import PIL
import threading

#1 or 2, 1 is blue and left, 2 is red and right
CV = 1

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Move Mouse Example"
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
image = PIL.Image.open("doge.jpg")
blep, blop = image.size

prepTime = 10
runTime = 20
runInterval = 1/8
reactiveTime = 5

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)


        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        arcade.set_background_color(arcade.color.ASH_GREY)
        self.needs_update = False
        self.arrayLength = 16
        self.arrayHeight = 16
        self.array = [[0 for x in range(self.arrayLength)] for y in range(self.arrayHeight)]        
        self.xUnit = (int)(SCREEN_WIDTH/self.arrayLength)
        self.yUnit = (int)(SCREEN_HEIGHT/self.arrayHeight)
        self.moving = False
        self.timeTracker = prepTime
        self.timer = threading.Timer(1, self.increment)
        self.timer.start()
        self.counter = 0
        self.income = 10
        self.orbX1 = (int) (self.arrayLength/8)
        self.orbX2 = (int) (self.arrayLength*7/8)
        self.orbY1 = (int) (self.arrayHeight*3/4)
        self.orbY2 = (int) (self.arrayHeight/2)
        self.orbY3 = (int) (self.arrayHeight/4)
        if (CV == 1):
            self.orbX = self.orbX1
        else:
            self.orbX = self.orbX2
        self.rounds = 0
        self.array[self.orbX1][self.orbY1] = 1
        self.array[self.orbX1][self.orbY2] = 1
        self.array[self.orbX1][self.orbY3] = 1
        self.array[self.orbX2][self.orbY1] = 2
        self.array[self.orbX2][self.orbY2] = 2
        self.array[self.orbX2][self.orbY3] = 2

        
        self.array[0][1] = 1
        self.array[1][1] = 1.1
        self.array[2][1] = 1.2
        self.array[3][1] = 1.3
        self.array[4][1] = 1.4
        self.array[5][1] = 1.5
        self.array[6][1] = 1.6
        self.array[7][1] = 1.7
        self.array[8][1] = 1.8
        self.array[9][1] = 1.9
        
        self.array[13][7] = 1
        self.array[13][8] = 1
        self.array[13][9] = 1
        self.array[12][9] = 1
        self.array[12][7] = 1
        
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.draw_array(self.array)
        #if(self.moving):
        #    self.array = self.updateLife()
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        clickX = (int) (x/self.xUnit)
        clickY = (int) (y/self.yUnit)
        if (self.counter < self.income):
            if (not self.checkOrb(clickX, clickY)):
                if (CV == 1 and clickX < self.arrayLength/2):
                    self.counter+=1
                    if(not self.moving):
                        if(self.array[clickX][clickY] == 0):
                            self.array[clickX][clickY] = CV
                        else:
                            self.array[clickX][clickY] = 0
                elif (CV == 2 and clickX >= self.arrayLength/2):
                    self.counter+=1
                    if(not self.moving):
                        if(self.array[clickX][clickY] == 0):
                            self.array[clickX][clickY] = CV
                        else:
                            self.array[clickX][clickY] = 0

            
    def draw_array(self, arr):
        # shape_list = arcade.ShapeElementList()
        sprite_list = arcade.SpriteList()
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                color = arr[i][j]
                if(color == 0):
                    newSprite = arcade.Sprite("doge.jpg", (self.xUnit+0.0)/blep)
                    newSprite.center_x = (i+.5)*self.xUnit
                    newSprite.center_y = (j+.5)*self.yUnit
                    sprite_list.append(newSprite)
                    if (self.checkOrb(i, j)):
                        orbSprite = arcade.Sprite("gold.png", (self.xUnit+0.0)/blep)
                        orbSprite.center_x = (i+.5)*self.xUnit
                        orbSprite.center_y = (j+.5)*self.yUnit
                        sprite_list.append(orbSprite)
                else:
                    if (color < 1.05):
                        newSprite = arcade.Sprite("doge1.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.1):
                        newSprite = arcade.Sprite("doge2.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.15):
                        newSprite = arcade.Sprite("doge3.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.2):
                        newSprite = arcade.Sprite("doge4.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.25):
                        newSprite = arcade.Sprite("doge5.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.3):
                        newSprite = arcade.Sprite("doge6.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.35):
                        newSprite = arcade.Sprite("doge7.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.4):
                        newSprite = arcade.Sprite("doge8.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.45):
                        newSprite = arcade.Sprite("doge9.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.5):
                        newSprite = arcade.Sprite("doge10.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.55):
                        newSprite = arcade.Sprite("doge11.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.6):
                        newSprite = arcade.Sprite("doge12.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.65):
                        newSprite = arcade.Sprite("doge13.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.7):
                        newSprite = arcade.Sprite("doge14.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.75):
                        newSprite = arcade.Sprite("doge15.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.8):
                        newSprite = arcade.Sprite("doge16.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.85):
                        newSprite = arcade.Sprite("doge17.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.9):
                        newSprite = arcade.Sprite("doge18.jpg", (self.xUnit+0.0)/blep)
                    elif (color < 1.95):
                        newSprite = arcade.Sprite("doge19.jpg", (self.xUnit+0.0)/blep)
                    else:
                        newSprite = arcade.Sprite("doge20.jpg", (self.xUnit+0.0)/blep)
                    newSprite.center_x = (i+.5)*self.xUnit
                    newSprite.center_y = (j+.5)*self.yUnit
                    sprite_list.append(newSprite)
                    if (self.checkOrb(i, j)):
                        orbSprite = arcade.Sprite("gold.png", (self.xUnit+0.0)/blep)
                        orbSprite.center_x = (i+.5)*self.xUnit
                        orbSprite.center_y = (j+.5)*self.yUnit
                        sprite_list.append(orbSprite)
                    
        sprite_list.draw()
        #             shape = arcade.create_rectangle_filled((i+.5)*self.xUnit, (j+.5)*self.yUnit, self.xUnit-1, self.yUnit-1, arcade.color.BLUSH)
        #             shape_list.append(shape)
        # shape_list.draw()

    def checkOrb(self, x, y):
        if (x == self.orbX1 or x == self.orbX2):
            if (y == self.orbY1 or y == self.orbY2 or y == self.orbY3):
                return True
        return False
        
    def updateLife(self):
        grid = self.array
        y = self.arrayHeight
        x = self.arrayLength
        newGrid = [[0 for a in range(self.arrayLength)] for b in range(self.arrayHeight)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                summ = 0
                color = 0
                startY = -1
                endY = 2
                startX = -1
                endX = 2
                if (i == 0):
                    startY = 0
                if (i == y-1):
                    endY = 1
                if (j == 0):
                    startX = 0
                if (j == x-1):
                    endX = 1
                for a in range (startY,endY):
                    for b in range (startX,endX):
                        if (not(a == 0 and b == 0)):
                            if(grid[i+a][j+b] > 0 and not(self.checkOrb(i+a,j+b))):
                                summ+=1
                                color+=grid[i+a][j+b]-1.5
                if (self.checkOrb(i,j)):
                    if (summ != 3):
                        newGrid[i][j] = grid[i][j]
                    else:
                        if (i < (int (self.arrayLength/2))):
                            newGrid[i][j] = grid[i][j] + (((color/summ) + 0.5)/3) + summ * 0.01
                        else:
                            newGrid[i][j] = grid[i][j] + (((color/summ) - 0.5)/3) - summ * 0.01
                else:
                    if (grid[i][j]>0):
                        if (summ == 2 or summ ==3):
                            nextt = 1.5 + color/summ
                            newGrid[i][j] = nextt
                        else:
                            newGrid[i][j] = 0
                    else:
                        if (summ == 3):
                            nextt = 1.5 + color/summ
                            newGrid[i][j] = nextt
                        else:
                            newGrid[i][j] = 0
        return newGrid
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.moving = True
        if key == arcade.key.DOWN:
            self.moving = False
    def increment(self):
        if(self.moving):
            self.timeTracker -= runInterval
        else:
            self.timeTracker -= 1
            #if (self.timeTracker < reactiveTime):
              #  merge(self)
        if(self.timeTracker <= 0):
            self.moving = not self.moving
            if(self.moving):
                self.timeTracker = runTime
                self.timer = threading.Timer(runInterval, self.increment)
                self.timer.start()
            else:
                self.rounds += 1
                self.counter = 0
                self.income = 10 + 2 * self.rounds + (int)(self.income * 4)
                self.timeTracker = prepTime
                self.timer = threading.Timer(1, self.increment)
                self.timer.start()
        elif (self.moving):
            self.timer = threading.Timer(runInterval, self.increment)
            self.timer.start()
            self.array = self.updateLife()
        else:
            self.timer = threading.Timer(1, self.increment)
            self.timer.start()
    def orbHealth (self):
        summ = grid[orbY1][orbX] + grid[orbY2][orbX] + grid[orbY3][orbX]
        if (CV == 1):
            return (summ - 3)
        else:
            return (6 - summ)
            
    def merge(self):
        arr = synchGame(self)
        if (CV == 1):
           for i in range(len(arr)):
               for j in range(len(arr[0])/2,len(arr[0])):
                   self.array[i][j] = arr[i][j]
        if (CV == 2):
            for i in range(len(arr)):
                for j in range(len(arr[0])/2):
                    self.array[i][j] = arr[i][j]
        
def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
