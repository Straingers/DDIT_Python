from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

camera.orthographic = True
camera.fov = 20

background = Entity(
    model='cube',
    texture='background.png',
    scale=(40, 20, 1),
    z=2
)

ground = Entity(
    model='cube',
    color=color.rgb(50, 180, 50),
    z=0.1,
    y=-8,
    scale=(100, 5, 10),
    collider='box'
)

wall = Entity(
    model='cube',
    color=color.rgb(50, 180, 50),
    collider='box',
    position=(-3, 0),
    scale=(5, 1)
)

player = PlatformerController2d(
    position=(-15, -5),
    texture='boshy.png',
    color=color.white,
    scale=1,
    max_jumps=2
)

spikes = []

for i in range(10):
    spike = Entity(
        model='cube',
        texture='spike.png',
        color=color.white,
        collider='box',
        position=(random.randint(-10, 10), -5),
        scale=1
    )

    spikes.append(spike)

def update():
    hit_info = player.intersects()

    if hit_info.hit:
        if hit_info.entity in spikes:
            player.position = (-15, -5)

app.run()
