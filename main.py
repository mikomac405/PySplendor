from os import pardir
from ursina import *   
from ursina import shaders
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


card1_texture = load_texture("assets/crd/c3.jpg")
card2_texture = load_texture("assets/crd/c4.jpg")
card3_texture = load_texture("assets/crd/c5.jpg")

class Card(Draggable):
    def __init__(self, position = (10,15,0), texture = card1_texture):
            super().__init__(
            parent = table,
            position = position,
            model = 'assets/crd/crd',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.lime,
            rotation = (0,180,0),
            scale = 0.1,
            plane_direction = (0,1,0),
            lock = Vec3(0,1,0)
        )

    # def input(self, key):
    #     if self.hovered:
    #         if key == 'left mouse down':
    #             self.x = mouse.x
    #             self.z = mouse.y

class Chip(Draggable):
    def __init__(self, position = (0.9,1.23,0), texture = None):
        super().__init__(
            parent = table,
            position = position,
            model = 'assets/chip/chip',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.lime,
            rotation = (0,0,0),
            scale = 1,
            plane_direction = (0,1,0),
            lock = Vec3(0,1,0)
        )

table = Entity(
    parent = scene,
    model = load_model('assets/table/table'),
    double_sided = True,
    texture = load_texture('assets/table/table.tif'),
    rotation = (0,0,0),
    scale = 2,
    position = (0, 0, 0),
    shader=shaders.basic_lighting_shader
)

c1 = Card(position=(1,0.78,0))

cube = Entity(
    parent = scene,
    model = 'cube',
    collider = 'box',
    scale = (30,1,30),
    position = (0,-1,0)
)

chip = Chip(texture=load_texture("assets/chip/chip.tif"))

camera.rotation_x = 80
camera.y = 9
camera.z = -1.5
#player = FirstPersonController(y=5, origin_y=-.5)


app.run() 