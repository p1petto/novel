# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

init:
    #image bg = "images"
    $ answers = 0
    $ end = False
label start:

    scene bg room

    show g normal

    g "О нет, мяч улетел в кусты...{w=3}\nПойду схожу за ним"
    
    g "Что это лежит, похожу на какую-то сумку{w=3}\nХмм"

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
        pass

    return
