
define g = Character("[name]", color="#c8ffc8")         # главный герой
define girl = Character("Маша", color="#ffe9c8")        # девушка
define b = Character("Гопник", color="#ffe9c8")         # гопник
define m = Character("Мама", color="#ffe9c8")           # мама
define d = Character("Директор", color="#ffe9c8")       # директор
define s = Character("Охранник", color="#ffe9c8")       # охранник

# слова автора
define n = Character(None, kind=nvl)
define e = Character(None)

image g smile   = "images/characters/g_smile.png"
image g normal  = "images/characters/g_normal.png"
image g beaten  = "images/characters/g_beaten.png"
image g scared  = "images/characters/g_scared.png"


init:
    $ posR = Position(xalign=0.8, yalign=1)
    $ posL = Position(xalign=0.2, yalign=1)