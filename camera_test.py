from ursina import *
from ursina import shaders

app = Ursina()

cube = Entity(
            parent = scene,
            model = 'cube',
            collider = 'box',
            color = color.red,
            scale = (1,1,1),
            position = (0,-5,0),
            shader=shaders.basic_lighting_shader,
        )

camera.rotation_x = 10


def update():
  camera.animate_rotation

app.run()