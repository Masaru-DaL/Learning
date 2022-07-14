class ColorPalette:
    
    def __init__(self, color_list):
        self.color_list = color_list
        self.i = 0
        
    def __next__(self):
        if self.i >= len(self.color_list):
            raise StopIteration()
        
        color = self.color_list[self.i]
        self.i += 1
        return color

    def __iter__(self):
        return self

