# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.\n'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Хммм подумала утка, у меня же никогда не было зонта.\n'
        'Остаться дома?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_stay_home()
    return step3_no_stay_home()


def step2_no_umbrella():
    print(
        'ИИИИИИИИтааакк сойдёт, я же утка в конце концов.\n'
        'Одной идти?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_alone()
    return step3_friends()


def step3_stay_home():
    print(
        'Нафиг ваш бар, пойду спать.\n'
        'Всем пока.'
    )


def step3_no_stay_home():
    print(
        'До бара далеко, поплавать у дома в болоте?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step4_swamp()
    return step3_stay_home()


def step3_alone():
    print(
        'Никома я не нужна.'
    )
    return step3_stay_home()


def step3_friends():
    print(
        'У меня же нет друзей.'
    )
    return step3_stay_home()


def step4_swamp():
    print(
        'Вы серьезно?\n'
        'Обиделась, не пишите!'
    )


if __name__ == '__main__':
    step1()