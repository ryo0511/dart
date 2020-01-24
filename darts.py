# -*- coding:utf-8 -*-
import cricket
import zero_one
cr = cricket.Cricket()
zo = zero_one.Zero_one()


while 1:
    print("1:ゼロワン")
    print("2:クリケット")
    print("ゲームを選んでください:", end="")
    game = int(input())
    while 1:
        if game == 1:
            zo.zero_one()
        elif game == 2:
            cr.cricket()
        if input("なにか入力するとゲーム選択に戻る") == "":
            continue
        else:
            print("aaa")
            break
    if input("なにか入力すると終了") == "":
        continue
    else:
        print("bbb")
        break
