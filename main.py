from os import pardir
from ursina import *  
from ursina import shaders
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


card1_texture = load_texture("assets/crd/c3.jpg")
card2_texture = load_texture("assets/crd/c4.jpg")
card3_texture = load_texture("assets/crd/c5.jpg")

class Card(Button):
     def __init__(self, position = (0,0,0), texture = card1_texture):
            super().__init__(
            parent = table,
            position = position,
            model = 'assets/crd/crd',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.95,1)),
            highlight_color = color.white,
            rotation = (90,90,90),
            scale = 0.1
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

c1 = Card(position=(0,0,0))

cube = Entity(
    parent = scene,
    model = 'cube',
    collider = 'box',
    scale = (30,1,30),
    position = (0,-1,0)
)

player = FirstPersonController(y=5, origin_y=-.5)


app.run() 