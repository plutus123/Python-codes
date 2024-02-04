import math
def paint(height,width,coverage):
    test_h=int(input("The height of the wall: "))
    test_w=int(input("The width of the wall: "))
    cover=5
    paint_can=math.ceil((test_h*test_w)/cover)
    print(f"The number of paint can needed is {paint_can}")
paint(height="test_h",width="test_width",coverage="cover")