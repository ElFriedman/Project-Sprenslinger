
import arcade
import os
import PIL
import socket
import threading
import numpy
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SCREEN_TITLE = "server"
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
image = PIL.Image.open("doge.jpg")
blep, blop = image.size
CV = 1
serverRunning = True

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)


        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        arcade.set_background_color(arcade.color.ASH_GREY)
        self.needs_update = False
        self.arrayLength = 40
        self.arrayHeight = 40
        self.array = [[0 for x in range(self.arrayLength)] for y in range(self.arrayHeight)]
        self.array[0][1] = 1.0
        self.xUnit = (int)(SCREEN_WIDTH/self.arrayLength)
        self.yUnit = (int)(SCREEN_HEIGHT/self.arrayHeight)
        self.moving = False
        self.serversocket = socket.socket(
        	        socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        self.host =  '172.20.10.5'

        self.port = 9999

        # bind to the port
        self.serversocket.bind((self.host, self.port))

        # queue up to 5 requests
        self.serversocket.listen(500000)
        self.serverThread = threading.Thread(target = self.run_server, args = (self.serversocket,))
        self.serverThread.start()
    def set_array(self, new_grid):
        self.array = new_grid
    def run_server(self, serversocket):
        while serverRunning:
            # establish a connection
            clientsocket,addr = serversocket.accept()

            msg = numpy.array(self.array, dtype = 'float32').tobytes()
            clientsocket.send(msg)
            clientsocket.close()
        print("done")
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.draw_array(self.array)
        if(self.moving):
            self.array = self.updateLife()
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if(self.array[(int)(x/self.xUnit)][(int)(y/self.yUnit)] == 0):
            self.array[(int)(x/self.xUnit)][(int)(y/self.yUnit)] = 1.0
        else:
            self.array[(int)(x/self.xUnit)][(int)(y/self.yUnit)] = 0.0
    def draw_array(self, arr):
        # shape_list = arcade.ShapeElementList()
        sprite_list = arcade.SpriteList()
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if(arr[i][j] == 0):
                    newSprite = arcade.Sprite("doge.jpg", (self.xUnit+0.0)/blep)
                    newSprite.center_x = (i+.5)*self.xUnit
                    newSprite.center_y = (j+.5)*self.yUnit
                    sprite_list.append(newSprite)
        sprite_list.draw()
        #             shape = arcade.create_rectangle_filled((i+.5)*self.xUnit, (j+.5)*self.yUnit, self.xUnit-1, self.yUnit-1, arcade.color.BLUSH)
        #             shape_list.append(shape)
        # shape_list.draw()
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
                        if (not(a==0 and b==0)):
                            if(grid[i+a][j+b] > 0):
                                summ+=1
                                color+=grid[i+a][j+b]-1.5
                if (grid[i][j]>0):
                    if (summ == 2 or summ ==3):
                        nextt = 1.5 + color/summ
                        newGrid[i][j] = 1.5 + nextt
                    else:
                        newGrid[i][j] = 0
                else:
                    if (summ == 3):
                        nextt = 1.5 + color/summ
                        newGrid[i][j] = 1.5 + nextt
                    else:
                        newGrid[i][j] = 0
        return newGrid
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.moving = True
        if key == arcade.key.DOWN:
            self.moving = False
        if key == arcade.key.LEFT:
            print("mew")
            msg = numpy.array(self.array).tobytes()
            print("asdf")
            as_array = numpy.array(self.array)
            array_data_type = as_array.dtype.name
            array_shape = as_array.shape
            reconstituted = numpy.frombuffer(msg, dtype = array_data_type).reshape(array_shape)
            print("asdfdd")
            print(reconstituted)
            print(self.array)
            print(self.array == reconstituted)
        if key == arcade.key.RIGHT:
            # create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # get local machine name
            host = '172.20.10.8'

            port = 9998

            # connection to hostname on the port.
            s.connect((host, port))

            # Receive no more than 999... bytes
            msg = s.recv(99999999)

            as_array = numpy.array(self.array, dtype = 'float32')
            array_data_type = as_array.dtype.name
            array_shape = as_array.shape
            print(msg)
            print(numpy.array(self.array).tobytes())
            print(numpy.frombuffer(msg, dtype = array_data_type))
            testArray = numpy.frombuffer(msg, dtype = array_data_type).reshape(array_shape)
            print(testArray)
            print(testArray.tolist())
            self.array = testArray.tolist()
            s.close()
            # serverRunning = False
            # self.serversocket.close()
            # #self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.serversocket = socket.socket(
            # 	        socket.AF_INET, socket.SOCK_STREAM)
            #
            # # queue up to 5 requests
            # self.serversocket.listen(500000)
            # self.serverThread = threading.Thread(target = self.run_server, args = (self.serversocket,self.array,))
            # self.serverThread.start()
    def synchGame(self):
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = '172.20.10.8'

        port = 9998

        # connection to hostname on the port.
        s.connect((host, port))

        # Receive no more than 999... bytes
        msg = s.recv(99999999)

        as_array = numpy.array(self.array, dtype = 'float32')
        array_data_type = as_array.dtype.name
        array_shape = as_array.shape
        testArray = numpy.frombuffer(msg, dtype = array_data_type).reshape(array_shape)
        s.close()
        return testArray.tolist()
class PopUp(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_text("Text!", 10, 20, arcade.color.BLACK, 12)

def main():
    PopUp(100, 50, "Test")
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()


if __name__ == "__main__":
    main()
