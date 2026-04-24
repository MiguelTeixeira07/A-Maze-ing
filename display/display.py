from walls import Walls


def file_to_data():
    data = []
    with open('../maze.txt', 'r') as hex_maze:
        for line in hex_maze:
            if not line.strip():
                break
            for char in line:
                if char != '\n':
                    data.append(char)
    return data


def getting_widht():
    with open('../config.txt', 'r') as config_file:
        for line in config_file:
            if line.startswith('WIDTH'):
                return int(line.split('=')[1].strip())


def indexing_wall():
    list_walls = []
    for item in Walls:
        list_walls.append(item.value)
    return list_walls


def width_table(width, eol):
    i = 1
    while i < width:
        if width * i == eol:
            return True
        i += 1
    return False


if __name__ == '__main__':
    hex_data = file_to_data()
    list_walls = indexing_wall()

    width = getting_widht()
    eol = 0
    for data in hex_data:
        if width_table(width, eol):
            print()
        print(*list_walls[int(data, 16) % 16], end='', sep='')
        eol += 1
    print()
