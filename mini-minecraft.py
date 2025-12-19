from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

blocks = []

grass = load_texture('./textures/grass.jpg')
brick = load_texture('./textures/brick.jpg')
wood = load_texture('./textures/wood.png')
diamond = load_texture('./textures/diamond.png')

block_types = [grass, brick, wood, diamond]

selected_block_index = 0  
def place_block(position, texture=grass):
    block = Entity(
        model='cube',
        texture=texture,
        position=position,
        scale=1,
        collider='box'
    )
    blocks.append(block)

for x in range(50):
    for z in range(50):
        place_block((x, 0, z))

def switch_block():
    global selected_block_index
    if selected_block_index + 1 > len(block_types)-1:
        selected_block_index = 0
    else:
        selected_block_index += 1

block_label = Text(
    text=f'Selected Block: {str(block_types[selected_block_index]).split(".")[0]}',
    position=(-0.5, 0.45),  
    origin=(0, 0),
    color=color.white
)

info_label = Text(
    text='Tab: Change block\nWASD: Move\nLeft click: Place\nRight click: Destroy\nEsc: Exit',
    position=(-0.75, 0.4),  
    origin=(0, 0),
    color=color.white,
    anchor_x='left'
)

def input(key):
    if key == 'left mouse down':  
        if mouse.hovered_entity and mouse.hovered_entity in blocks:
            blocks.remove(mouse.hovered_entity)
            destroy(mouse.hovered_entity)

    if key == 'right mouse down':  
        if mouse.hovered_entity:
            place_block(mouse.hovered_entity.position + mouse.normal, texture=block_types[selected_block_index])

    if key == 'tab':  
        switch_block()
        block_label.text = f'Selected Block: {str(block_types[selected_block_index]).split(".")[0]}'  
   
    if key == 'escape':
        quit()

player = FirstPersonController()
Sky()
respawn_height = -30
respawn_position = (25, 40, 25)

def update():
    if player.y < respawn_height:
        player.position = respawn_position


light = DirectionalLight(
    direction=(0, -1, -1),  
    color=color.white,
    shadows=True  
)

ambient = AmbientLight(color=color.rgb(0.6, 0.6, 0.6))  

app.run()
