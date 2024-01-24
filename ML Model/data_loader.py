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
            drawing = qd.get_drawing(group)
            while drawing.recognized != True:
                drawing = qd.get_drawing(group)
            drawing_img = drawing.get_image(stroke_color=(255, 255, 255), stroke_width=6, bg_color=(0, 0, 0))
            drawing_img.save(f'E:/ConvMoNET/Data/{group}s/{str(drawing.key_id) + "-" + str(drawing.recognized)}.jpg')

categories = qd.drawing_names[:65]
print(categories)

# download(categories)
