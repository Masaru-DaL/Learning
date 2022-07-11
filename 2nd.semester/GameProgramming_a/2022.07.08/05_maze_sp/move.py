class Move:
    
    def __init__(self, maze_map):
        self.key = ""
        self.release = True
        self.moved = False
        self.maze_map = maze_map
        
    def key_down(self, key):
        if self.release:
            self.key = key
            self.moved = False

    def key_up(self):
        if self.key == "" and self.moved == True:
            self.release = True
    
    def move(self, my_x, my_y):
        
        if self.moved == False:
            if self.key == "Down" and self.maze_map[my_y+1][my_x] == 0:
                my_y += 1
                self.key = ""
                self.release = False
                self.moved = True
            if self.key == "Up" and self.maze_map[my_y-1][my_x] == 0:
                my_y -= 1
                self.key = ""
                self.release = False
                self.moved = True
            if self.key == "Right" and self.maze_map[my_y][my_x+1] == 0:
                my_x += 1
                self.key = ""
                self.release = False
                self.moved = True
            if self.key == "Left" and self.maze_map[my_y][my_x-1] == 0:
                my_x -= 1    
                self.key = ""
                self.release = False
                self.moved = True
        return (my_x, my_y)