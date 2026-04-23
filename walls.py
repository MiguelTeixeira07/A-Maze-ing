class Walls():

    # 0 -> 0000
    def empty():
        print('  ')

    # 1 -> 0001
    def top():
        print('═\n\n')

    # 2 -> 0010
    def right():
        print('  ║')

    # 3 -> 0011
    def right_top_corner():
        print(' ╗')

    # 4 -> 0100
    def bottom():
        print('\n\n═')

    # 5 -> 0101
    def top_bottom():
        print('═\n\n═')

    # 6 -> 0110
    def right_bottom_corner():
        print(' ╝')

    # 7 -> 0111
    def top_right_bottom():
        print('═\n ║\n═')

    # 9 -> 1001
    def left_top_corner():
        print('╔ ')

    # 12 -> 1100
    def left_bottom_corner():
        print('╚ ')

    def vertical_line():
        print(' ║ ')

    def horizontal_line():
        print(' ═ ')


Walls.top_right_bottom()
