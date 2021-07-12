from ursina import *


# 10. Create player hand
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,                 # Specifies parent of hand which is the player
            model = 'resources/arm',
            texture = 'resources/arm_texture.png',
            scale = 0.2,
            rotation = Vec3(160,-5,0),
            position = Vec2(0.5,-0.6)
        )

    # 11. Hand "animations"
    def active(self):
        self.rotation = Vec3(160,-5,0)
        self.position = Vec2(0.4,-0.5)
    
    def passive(self):
        self.position = Vec2(0.5,-0.6)
