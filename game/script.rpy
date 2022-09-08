init:
    image bg_pg = "images/scenes/playground.jpg"
    image bg_b = "images/scenes/bushes.jpg"
    $ answers = 0
    $ end = False
label start:

    scene bg room

    $ name = renpy.input("Как вас зовут?")

    show g normal

    #$ name = renpy.input("Боец, как тебя зовут?", length=5, allow="input")

    show bg_pg

    g "О нет, мяч улетел в кусты...{w=3}\nПойду за ним"
    
    g "Что это лежит, похожу на какую-то сумку{w=3}\nХмм"

    show bg_b

    menu:
        "Что же делать?"
        "Взять сумку":
            $ answers += 1
        "Сообщить в полицию":
            $ end = True
    if end:
        pass
        return
    else:
        g "Что же тут, оооо, бабки, кайфффф"
        g "Пойду куплю шмар"

    return
