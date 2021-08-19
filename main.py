from os import pardir
import numpy as np
from ursina import *     
from ursina import shaders
from ursina.prefabs.first_person_controller import FirstPersonController
from os import listdir
from os.path import isfile, join

files = [f for f in listdir('cards') if isfile(join('cards', f))]

app = Ursina()


def random_card():
    pass

class Card(Draggable):
    def __init__(self, position = (10,15,0), texture = None):
            super().__init__(
            parent = table,
            position = position,
            model = 'assets/crd/crd',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.lime,
            rotation = (0,180,0),
            scale = 0.07,
            plane_direction = (0,1,0),
            lock = Vec3(0,1,0),
            tooltip = Tooltip("Onyx\nPrice: 2x diamond, 2x emerald")
        )

    # def input(self, key):
    #     if self.hovered:
    #         if key == 'left mouse down':
    #             self.x = mouse.x
    #             self.z = mouse.y

class Chip(Draggable):
    def __init__(self, position = (0.9,1.23,0), texture = 'assests/chip/chip.tif'):
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
            lock = Vec3(0,1,0),
            collision  = True
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



cube = Entity(
    parent = scene,
    model = 'cube',
    collider = 'box',
    color = color.gray,
    scale = (30,1,30),
    position = (0,-1,0)
)

chip = Chip(texture=load_texture("assets/chip/chip.tif"))

camera.rotation_x = 80
camera.y = 9
camera.z = -1.5
#player = FirstPersonController(y=5, origin_y=-.5)

#c1 = Card(position=(-0.95,0.78,-0.65))

for x in np.arange(-0.975, 1.05, 0.105):
    print(x)
    card = Card(position=(x,0.78,-0.6), texture = random.choice(['assets/crd/c3.jpg','assets/crd/c4.jpg','assets/crd/c5.jpg']))

app.run() 