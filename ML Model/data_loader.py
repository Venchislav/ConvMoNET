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
        for i in range(500):
            drawing = qd.get_drawing(group[:-1])
            while drawing.recognized != True:
                drawing = qd.get_drawing(group[:-1])
            drawing_img = drawing.get_image(stroke_color=(255, 255, 255), stroke_width=6, bg_color=(0, 0, 0))
            drawing_img.save(f'E:/ConvMoNET/Data/{group}s/{str(drawing.key_id) + "-" + str(drawing.recognized)}.jpg')

categories = ['airplanes', 'apples', 'bananas', 'basketballs', 'bears', 'beds', 'bees', 'bicycles', 'birds', 'books', 'brains', 'breads', 'buckets', 'buss', 'cactuss', 'cakes', 'calculators', 'camels', 'cameras', 'campfires', 'candles', 'carrots', 'cars', 'castles', 'cats', 'chairs', 'churchs', 'circles', 'clocks', 'clouds', 'compasss', 'computers', 'cookies', 'couchs', 'cows', 'crabs', 'crocodiles', 'crowns', 'cups', 'diamonds', 'dogs', 'dolphins', 'doors', 'dragons', 'dumbbells', 'elephants', 'eyeglassess', 'eyes', 'faces', 'feathers', 'fences', 'fireplaces', 'fishs', 
'flowers', 'flying saucers', 'frogs', 'frying pans', 'giraffes', 'grapess', 'grasss', 'guitars', 'hamburgers', 'hammers', 'hats', 'headphoness', 'hedgehogs', 'helicopters', 'horses', 'hot air balloons', 'hot dogs', 'house plants', 'houses', 'ice creams', 'keys', 'knifes', 'laptops', 'leafs', 'light bulbs', 'lightnings', 'lions', 'lollipops', 'maps', 'microphones', 'monkeys', 'mountains', 'mushrooms', 'oceans', 'octopuss', 'onions', 'owls', 'palm trees', 'pandas', 'pantss', 'pears', 'pencils', 'pigs', 'pineapples', 'pizzas', 'potatos', 'power outlets', 'purses', 'rabbits', 'radios', 'remote controls', 'rifles', 'sailboats', 'sandwichs', 'saws', 'scissorss', 'sea turtles', 'sheeps', 'shoes', 'shortss', 'shovels', 'skateboards', 'skulls', 'smiley faces', 'snails', 'snakes', 'snowflakes', 'snowmans', 'soccer balls', 'spiders', 'squares', 
'stars', 'stitchess', 'stop signs', 'strawberrys', 'submarines', 'suitcases', 'suns', 'swans', 'swords', 't-shirts', 'tables', 'teddy-bears', 'telephones', 'televisions', 'tents', 'The Eiffel Towers', 'The Mona Lisas', 'tigers', 'toilets', 'tooths', 'tractors', 'traffic lights', 'trees', 'triangles', 'trucks', 'umbrellas', 'underwears', 'watermelons', 'whales', 'wheels', 'windmills', 'wristwatchs', 'zigzags']

# download(categories)
