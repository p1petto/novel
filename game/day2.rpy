label day_2:

    scene bg_r  with fade

    show g normal

    g "Какой прекрасный день, я проснулся богатым!"

    scene bg_sc

    show g normal

    e "Главный герой приходит в школу."

    show g normal

    e "Главный герой шарится в своем шкафчике."

    show g normal

    e "Задира подходит к главному герою"

    show g scared at posR 

    show b normal at posL

    b "Слышь, маленький *****, разминай лицо, сейчас буду тебя бить."

    $end = False
    menu:
        "Твои действия?"
        "Ааа, не бей, пожалуйста!":
            pass
        "Ты не ударишь меня, я стал очень богатым)0000))))000))":
            $ bad_answer += 1
            $ end = True
    if end:
        show g scared at posR
        show b normal at posL
        b "ААААРГРХРХРХРХР!!!"
    else:
        show g scared at posR
        show b normal at posL
        b "ААААРГРХРХРХРХР!!!"
        
    show b normal at posL
    show g beaten at posR with hpunch and vpunch
    b "Не попадайся мне на глаза, ********!"
    g "*Плачет*"
    jump day_3
    return