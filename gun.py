from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time as pytime

app = Ursina()
window.borderless = False
window.title = '총게임 예제'
mouse.locked = True

# 바닥
for x in range(-8, 9):
    for z in range(-8, 9):
        Entity(model='cube', color=color.green, position=(x,0,z), collider='box')

targets = []

class Target(Entity):
    def __init__(self, **kwargs):
        super().__init__(model='cube', color=color.red, collider='box', **kwargs)
        self.max_health = 100
        self.health = 100
        self.health_bar = Entity(
            parent=self,
            model='quad',
            color=color.lime,
            scale=(1, 0.2, 1),
            position=(0, 1.0, 0),
        )
        self.health_bar2 = Entity(
            parent=self,
            model='quad',
            color=color.lime,
            scale=(1, 0.2, 1),
            rotation_y=180,
            position=(0, 1.0, 0), 
        )
        self.update_health_bar()
    def take_damage(self, dmg):
        self.health -= dmg
        self.update_health_bar()
        if self.health <= 0:
            destroy(self)
            if self in targets:
                targets.remove(self)
    def update_health_bar(self):
        self.health_bar.scale_x = max(0.01, self.health/self.max_health)
        self.health_bar2.scale_x = max(0.01, self.health/self.max_health)
        if self.health > 60:
            self.health_bar.color = color.lime
            self.health_bar2.color = color.lime
        elif self.health > 30:
            self.health_bar.color = color.yellow
            self.health_bar2.color = color.yellow
        else:
            self.health_bar.color = color.red
            self.health_bar2.color = color.red
            
        

for _ in range(15):
    x, z = random.randint(-7,7), random.randint(-7,7)
    y = 1
    t = Target(position=(x,y,z))
    targets.append(t)

player = FirstPersonController(y=2, speed=5)


crosshair = Entity(parent=camera.ui, model='quad', color=color.black, scale=(0.01,0.01), position=(0,0))

bullets = []

class Bullet(Entity):
    def __init__(self, pos, dir):
        super().__init__(model='sphere', color=color.azure, scale=0.2, position=pos, collider='sphere')
        self.dir = dir.normalized()
        self.speed = 20
        self.life = 2  # 2초 후 자동 소멸
        bullets.append(self)
    def update2(self, dt):
        self.position += self.dir * dt * self.speed
        self.life -= dt
        if self.life <= 0:
            destroy(self)
            if self in bullets:
                bullets.remove(self)

        for t in targets[:]:
            if self.intersects(t).hit:
                t.take_damage(20)
                print('적 명중!')
                destroy(self)
                if self in bullets:
                    bullets.remove(self)
                break

def input(key):
    if key == 'left mouse down':
        Bullet(camera.world_position + camera.forward*1.5, camera.forward)
    if key == 'escape':
        mouse.locked = not mouse.locked

_last_time = pytime.time()
def update():
    global _last_time
    now = pytime.time()
    dt = now - _last_time
    _last_time = now
    for b in bullets[:]:
        b.update2(dt)

app.run()
