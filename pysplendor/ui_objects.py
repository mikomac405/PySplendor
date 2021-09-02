from ursina import *


# wp = WindowPanel(
#     title='Custom Window',
#     content=(
#         Text('Amount of players:'),
#         Slider(min=2,max=4,step=1),
#         Button(text='Submit', color=color.azure),
#         ),
#         #popup=True,
#         enabled=False
#     )

class StartPanel(WindowPanel):
    def __init__(self, on_click):
            super().__init__(
                title='Custom Window',
                content=(
                    Text('Amount of players:'),
                    Slider(min=2,max=4,step=1),
                    Button(text='Submit', color=color.azure, on_click=on_click),
                ),
                enabled = True
            )
            self.amount_of_players = 2
            camera.rotation_x = 40
            camera.y = 6
            camera.z = -7

            
            

    
        