def compare_maps(map1, map2):
    same = True
    for k in range(len(map1)):
        if map1[k] != map2[k]:
            same = False
            break
    return same


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


def set_point(a_map, x, y, char):
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]
