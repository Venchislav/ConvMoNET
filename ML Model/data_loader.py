import os
from quickdraw import QuickDrawDataGroup
from quickdraw import QuickDrawData
import quickdraw

qd = QuickDrawData()

def download(doodle_groups):
    for group in doodle_groups:
        try:
            os.mkdir(f'E:/ConvMoNET/Data/{group}s')
        except:
            continue
        for i in range(10_000):
            drawing = qd.get_drawing(group[:-1])
            while drawing.recognized != True:
                drawing = qd.get_drawing(group[:-1])
            drawing_img = drawing.get_image(stroke_color=(255, 255, 255), stroke_width=6, bg_color=(0, 0, 0))
            drawing_img.save(f'E:/ConvMoNET/Data/{group}s/{str(drawing.key_id) + "-" + str(drawing.recognized)}.jpg')

categories = ['apples', 'basketballs', 'cakes', 'cameras', 'cars', 'cats',
              'clocks', 'cookies', 'crowns', 'cups', 'eyeglassess', 'faces', 'house plants',
              'houses', 'ice creams', 'keys', 'lollipops', 'mushrooms', 'pizzas', 'skulls', 
              'windmills']
# download(categories)
