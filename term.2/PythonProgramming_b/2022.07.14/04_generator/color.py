class ColorPalette:

    def __init__(self, color_list):
        self.color_list = color_list
        self._i = 0

    def __next__(self):
        if self._i >= len(self.color_list):
            raise StopIteration()

        color = self.color_list[self._i]
        self._i += 1
        return color

    def __iter__(self):
        return self

    def get_color(self):
        for col in self.color_list:
            return col

    def get_colors(self):
        for col in self.color_list:
            yield col
