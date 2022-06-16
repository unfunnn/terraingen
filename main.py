import random
import time

map_size = 100
map_size += 2

intensity = 0.5
animation = False

map=[]
for i in range(map_size):
    col = []
    for j in range(map_size):
        if j == map_size-1:
            col.append(0)
        elif i == map_size-1:
            col.append(0)
        elif i == 0:
            col.append(0)
        elif j == 0:
            col.append(0)
        else:
            random_list = random.choices([0,1], weights=(50, 50), k=5)
            col.append(random_list[0])
    map.append(col)

def flowers(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                surrounding_pixels = [
                    map[i][j + 1],
                    map[i][j - 1],
                    map[i + 1][j],
                    map[i - 1][j],
                ]
                num_forest = 0
                for surrounding_pixel in surrounding_pixels:
                    if surrounding_pixel == 5:
                        num_forest += 1
                percent_forest = num_forest / len(surrounding_pixels)
                if map[i][j] == 5:
                    if percent_forest >= 0.5:
                        map[i][j] = 6
                    else:
                        map[i][j] = 5
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Beaches")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp


def ocean(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                surrounding_pixels = []
                surrounding_pixels += [
                    map[i][j + 1],
                    map[i][j - 1],
                    map[i + 1][j],
                    map[i - 1][j]
                ]
                num_ocean = 0
                for surrounding_pixel in surrounding_pixels:
                    if surrounding_pixel == 0 or surrounding_pixel == -1 or surrounding_pixel == -2:
                        num_ocean += 1
                percent_ocean = num_ocean / len(surrounding_pixels)
                if map[i][j] == 0:
                    if percent_ocean >= 1:
                        map[i][j] = -1
                    else:
                        map[i][j] = 0
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Oceans")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp
def forest(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                forest_range = 3
                try:
                    surrounding_pixels = []
                    for iteration in range(forest_range):
                        surrounding_pixels += [
                            map[i][j + iteration],
                            map[i][j - iteration],
                            map[i + iteration][j],
                            map[i - iteration][j]
                        ]
                    num_grass = 0
                    for surrounding_pixel in surrounding_pixels:
                        if surrounding_pixel == 1 or surrounding_pixel == 5:
                            num_grass += 1
                    percent_grass = num_grass / len(surrounding_pixels)
                    if map[i][j] == 1 or map[i][j] == 5:
                        if percent_grass >= 1:
                            map[i][j] = 5
                        else:
                            map[i][j] = 1
                except IndexError:
                    pass
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Forest")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp


def beaches(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                surrounding_pixels = [
                    map[i][j + 1],
                    map[i][j - 1],
                    map[i + 1][j],
                    map[i - 1][j],
                ]
                num_black = 0
                for surrounding_pixel in surrounding_pixels:
                    if surrounding_pixel == 0:
                        num_black += 1
                percent_black = num_black / len(surrounding_pixels)
                if map[i][j] == 1:
                    if percent_black >= 0.1:
                        map[i][j] = 2
                    else:
                        map[i][j] = 1
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Beaches")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp

def mountains(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                mountain_range = 5
                try:
                    surrounding_pixels = []
                    for iteration in range(mountain_range):
                        surrounding_pixels += [
                            map[i][j + iteration],
                            map[i][j - iteration],
                            map[i + iteration][j],
                            map[i - iteration][j]
                        ]
                    num_white = 0
                    for surrounding_pixel in surrounding_pixels:
                        if surrounding_pixel == 1 or surrounding_pixel == 3 or surrounding_pixel == 4:
                            num_white += 1
                    percent_white = num_white / len(surrounding_pixels)
                    if map[i][j] == 1:
                        if percent_white >= 1:
                            map[i][j] = 3
                        else:
                            map[i][j] = 1
                except IndexError:
                    pass

                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Mountains")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp

def snow(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                snow_range = 3
                try:
                    surrounding_pixels = []
                    for iteration in range(snow_range):
                        surrounding_pixels += [
                            map[i][j + iteration],
                            map[i][j - iteration],
                            map[i + iteration][j],
                            map[i - iteration][j]
                        ]
                    num_mount = 0
                    for surrounding_pixel in surrounding_pixels:
                        if surrounding_pixel == 3 or surrounding_pixel == 4:
                            num_mount += 1
                    percent_mount = num_mount / len(surrounding_pixels)
                    if map[i][j] == 3 or map[i][j] == 4:
                        if percent_mount >= 1:
                            map[i][j] = 4
                        else:
                            map[i][j] = 3
                except IndexError:
                    pass
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Snow")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp





def render():
    for i in range(1, map_size - 2):
        output_str = ""
        for j in range(1, map_size - 2):
            if map[i][j] == 0:
                output_str += "\033[1;34m██\033[0m"
            elif map[i][j] == 1:
                output_str += "\033[1;32m██\033[0m"
            elif map[i][j] == 2:
                output_str += "\033[1;33m██\033[0m"
            elif map[i][j] == 3:
                output_str += "\033[1;30m██\033[0m"
            elif map[i][j] == 4:
                output_str += "\033[1;37m██\033[0m"
            elif map[i][j] == 5:
                output_str += "\033[0;32m██\033[0m"
            elif map[i][j] == 6:
                output_str += "\033[1;35m██\033[0m"
            elif map[i][j] == -1:
                output_str += "\033[0;34m██\033[0m"
            elif map[i][j] == -2:
                output_str += "\033[1;36m██\033[0m"
            else:
                output_str += map[i][j]
        print(output_str.replace("�", ""))


def step(loops=1):
    for loop in range(0, loops):
        for i in range(0, map_size - 1):
            for j in range(0, map_size - 1):
                surrounding_pixels = [
                    map[i][j + 1],
                    map[i][j - 1],
                    map[i + 1][j],
                    map[i - 1][j],
                    map[i + 1][j + 1],
                    map[i - 1][j + 1],
                    map[i + 1][j - 1],
                    map[i - 1][j - 1]
                ]
                num_white = 0
                num_black = 0
                for surrounding_pixel in surrounding_pixels:
                    if surrounding_pixel == 0:
                        num_black += 1
                    elif surrounding_pixel == 1:
                        num_white += 1
                percent_white = num_white / len(surrounding_pixels)
                percent_black = num_black / len(surrounding_pixels)
                if map[i][j] == 0:
                    if percent_black >= intensity:
                        map[i][j] = 0
                    else:
                        map[i][j] = 1

                elif map[i][j] == 1:
                    if percent_white >= intensity:
                        map[i][j] = 1
                    else:
                        map[i][j] = 0
                if animation:
                    tmp = map[i][j]
                    map[i][j] = "\033[0;31m██"
                    render()
                    print("Pos:", i, j)
                    print("Current Task: Step")
                    print("On loop:", loop)
                    time.sleep(2 / map_size)
                    import os
                    os.system('cls')
                    map[i][j] = tmp


step(5)
ocean()
mountains()
beaches()
snow()
forest()
flowers()

render()
