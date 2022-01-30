def update_hero(hero, power, alive, speed, x, y):

    file = open('hero.ini', 'r+', encoding='utf-8')
    stats = {
        'hero': hero,
        'power': power,
        'alive': alive,
        'speed': speed,
        'X': x,
        'Y': y
    }

    for k, v in stats.items():
        file.write(f'{k} - {v} \n')
    file.close()


if __name__ == '__main__':
    update_hero(hero='Batman', power=123, speed=456, alive=False, x=78, y=90)
