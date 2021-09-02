from ursina import *
from os import listdir
from os.path import isfile, join
import numpy as np
from typing import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.scene import Scene
from pysplendor.models import TableModel, CardModel, ChipModel, FloorModel
from pysplendor.ui_objects import StartPanel

files: List[str] = [f for f in listdir('cards') if isfile(join('cards', f))]

app = Ursina()

# Camera settings

# camera.rotation_x = 70
# camera.y = 6.4
# camera.z = -2.8

class Game(Scene):
    def __init__(self):
        super().__init__()
        
        # Game properties
        self.menu: bool = True
        self.amount_of_players: int = 2

        # Entities
        self.panel: StartPanel = StartPanel(on_click=self.panel_submit)
        self.table: TableModel = TableModel(parent=scene)
        self.floor: FloorModel = FloorModel(parent=scene)
        self.chip: ChipModel = ChipModel(parent = self.table, texture=load_texture("assets/chip/chip.tif"))
        self.cards: List[CardModel] = []

        for x in np.arange(-0.975, 1.05, 0.105):
            card: CardModel = CardModel(parent=self.table, position=(x,0,-0.6), texture = random.choice(files))
            self.cards.append(card)

    def panel_submit(self):
            self.amount_of_players = self.panel.content[1].value
            self.panel.enabled = False
            self.menu = False

            # set table and floor rotation_y to default
            self.table.rotation_y = 0
            self.floor.rotation_y = 0

            # set camera to table
            camera.rotation_x = 70
            camera.y = 6.4
            camera.z = -2.8


#player = FirstPersonController(y=5, origin_y=-.5)

scene = Game()

def update():
    if scene.menu == True:
        scene.table.rotation_y += 10 * time.dt
        scene.floor.rotation_y += 10 * time.dt

    for card in scene.cards:
        if card.dragging:
            card.y = 0.1
        else:
            card.y = -0.02

        

app.run() 