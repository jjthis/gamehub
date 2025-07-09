from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.borderless = False
window.title = 'Minecraft 3D Mini'

mouse.locked = True

def makeCube(pos):
    cube = Entity(model='cube', texture='hi.jpg', color=color.green, position=pos, collider='box')
    # outline = Entity(model='cube', color=color.black, scale=1.05, position=cube.position)
    return cube

# 바닥 생성
for x in range(-8, 9):
    for z in range(-8, 9):
        makeCube((x,0,z))

def input(key):
    if key == 'left mouse down':
        hit_info = mouse.hovered_entity
        if hit_info:
            pos = hit_info.position + mouse.normal
            makeCube(pos)
    if key == 'right mouse down':
        hit_info = mouse.hovered_entity
        if hit_info and hit_info.position.y > 0:
            destroy(hit_info)
    if key == 'escape':
        mouse.locked = not mouse.locked

player = FirstPersonController(y=2, speed=5)

button_width = 0.25
button_height = 0.12
button_y = -0.45
buttons = []
for i in range(4):
    btn = Button(
        parent=camera.ui,
        scale=(button_width, button_height),
        position=(-0.375 + i*0.25, button_y),
        text=str(i+1),
        background=Entity(model='quad', color=color.rgba(0,0,0,180)),
        on_click=lambda i=i: print(f'Button {i+1} clicked')
    )
    buttons.append(btn)

app.run()