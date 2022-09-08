
label day_2:

    scene bg room

    show g normal

    g "Какой прекрасный день, я проснулся богатым!"

    scene school

    show g normal

    e "Главный герой приходит в школу."

    scene school_coridor

    show g normal

    e "Главный герой шарится в своем шкафчике."

    scene school_coridor

    show g normal

    e "Задира подходит к главному герою"

    scene school_coridor

    show g scared at posR

    show b normal at posL

    b "Слышь, маленький *****, разминай лицо, сейчас буду тебя бить."

    $answer = 0
    $end = False
    menu:
        "Твои действия?"
        "Ааа, не бей, пожалуйста!":
            $answer += 1
        "Ты не ударишь меня, я стал очень богатым)0000))))000))":
            $end = True
    if end:
        scene school_coridor
        show g scared at posR
        show b angry at posL
        b "ААААРГРХРХРХРХР!!!"
    if answer == 1:
        scene school_coridor
        show g scared at posR
        show b angry at posL
        b "ААААРГРХРХРХРХР!!!"
    scene school_coridor
    show b angry at posL
    show g beaten at posR
    b "Не попадайся мне на глаза, ********!"
    g "*Плачет*"
    return