from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "t 0.1, s, q"
tags = "skeleton, animation"

import cocos
from cocos.director import director
from cocos.sprite import Sprite
from cocos import skeleton
import pyglet

import sample_skeleton

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()

        x,y = director.get_window_size()
        self.skin = skeleton.ColorSkin(sample_skeleton.skeleton,
                                        (255,0,0,255))
        self.add( self.skin )
        x, y = director.get_window_size()
        self.skin.position = x//2, y//2

def main():
    director.init()
    test_layer = TestLayer()
    bg_layer = cocos.layer.ColorLayer(255,255,255,255)
    main_scene = cocos.scene.Scene()
    main_scene.add(bg_layer, z=-10)
    main_scene.add(test_layer, z=10)
    director.run(main_scene)

if __name__ == '__main__':
    main()
