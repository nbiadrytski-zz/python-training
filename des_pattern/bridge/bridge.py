# circle square
# vector raster implementations
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RusterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):  # pass renderer here
        super().__init__(renderer)
        self.radius = radius

    def draw(self):  # this is bridge connecting shape and renderer
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RusterRenderer()
    vector = VectorRenderer()

    circle1 = Circle(vector, 5)
    circle1.draw()
    circle1.resize(2)
    circle1.draw()

    circle2 = Circle(raster, 10)
    circle2.draw()
    circle2.resize(2)
    circle2.draw()

# Drawing a circle of radius 5
# Drawing a circle of radius 10
# Drawing pixels for a circle of radius 10
# Drawing pixels for a circle of radius 20