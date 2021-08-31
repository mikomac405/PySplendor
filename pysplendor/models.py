from ursina import *     
from ursina import shaders

class FloorModel(Entity):
    def __init__(self, parent = None): # parent -> scene
        super().__init__(
            parent = parent,
            model = 'cube',
            collider = 'box',
            color = color.gray,
            scale = (30,1,30),
            position = (0,-2,0),
        )

class TableModel(Entity):
    def __init__(self, parent = None, ): # parent -> scene
        super().__init__(
            parent = parent,
            model = load_model('assets/table/table'),
            double_sided = True,
            texture = load_texture('assets/table/table.tif'),
            rotation = (0,0,0),
            scale = 2,
            position = (0, 0, 0),
            shader=shaders.basic_lighting_shader,
            origin_y = 0.78
        )

class CardModel(Draggable): # parent -> table
    def __init__(self, position = (10,15,0), texture = None, parent = None):
            super().__init__(
            parent = parent,
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

class ChipModel(Draggable): # parent -> table
    def __init__(self, position = (0.9,1.23,0), texture = 'assests/chip/chip.tif', parent = None):
        super().__init__(
            parent = parent,
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