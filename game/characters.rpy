init:
    image bg_pg = "images/scenes/playground.jpg"
    image bg_b = "images/scenes/bushes.jpg"
    image bg_r = "images/scenes/room.jpg"
    image bg_sc = "images/scenes/school_corridor.jpg"
    image bg_s = "images/scenes/shop.jpg"
    image bg_gr = "images/scenes/girl_room.jpg"
    image bg_w = "images/scenes/wheelchair.jpg"

define g = Character("[name]", color="#c8ffc8")         # главный герой
define gr = Character("[name]", color="#c8ffc8")         # главный герой
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

image gr smile   = "images/characters/gr_smile.png"
image gr normal  = "images/characters/gr_normal.png"
image gr money  = "images/characters/gr_money.png"

image m normal  = "images/characters/m_normal.png"
image d angry  = "images/characters/d_angry.png"



init:
    $ posR = Position(xalign=0.8, yalign=1)
    $ posL = Position(xalign=0.2, yalign=1)