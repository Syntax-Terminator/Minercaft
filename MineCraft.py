from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time

    
app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.rgb(0, random.uniform(150, 230), 0),
            highlight_color = color.lime,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x,0,z))


player = FirstPersonController()

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)

def update():

    if held_keys["r"]: # Respawn
        player.y = player.x = player.z = 0

    if held_keys["e"]: # Floating
        player.y += 1

    if held_keys["q"] and player.y > 0: # Coming Down
        player.y -= 0.5


sky = Sky()
app.run()