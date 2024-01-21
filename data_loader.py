
from quickdraw import QuickDrawDataGroup

apples = QuickDrawDataGroup("apple", max_drawings=10_000)
print(apples.drawing_count)

cnt = 0
for drawing in apples.drawings:
    drawing.image.save(f'Data/apples/apple{cnt}.png')
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt)


apples = QuickDrawDataGroup("airplane", max_drawings=10_000)
print(apples.drawing_count)

cnt = 0
for drawing in apples.drawings:
    drawing.image.save(f'Data/airplanes/airplanes{cnt}.png')
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt)

print('Data Load Done!')