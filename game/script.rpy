init:
    $ answers = 0
    $ end = False
label start:

    scene bg room

    $ name = renpy.input("Как вас зовут?")

    scene bg_pg
    show g normal

    g "О нет, мяч улетел в кусты...{w=3}\nПойду за ним"
    
    g "Что это лежит, похожу на какую-то сумку{w=3}\nХмм"

    hide g normal
    scene bg_b

    menu:
        "Что же делать?"
        "Взять сумку":
            $ answers += 1
        "Сообщить в полицию":
            $ end = True
    if end:

        return
    else:
        g "Что же тут, оооо, деньги, кайфффф"
        g "Пойду куплю покушаю"
    jump day_2

    return
