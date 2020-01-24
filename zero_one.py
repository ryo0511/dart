# -*- coding:utf-8 -*-
# import darts_bord
# db = darts_bord.Bord()


class Zero_one():
    def __init__(self):
        self.round = 10

    def gameInit(self):
        self.player_point = []
        gamePoint = [301, 501, 701, 901, 1001]
        print("何点で開始しますか？以下から選択してください。")
        for i, g in enumerate(gamePoint):
            print("番号", i, ":点数", g)
        select_point = gamePoint[int(input("番号を入力してください。:"))]
        self.num_player = int(input("何人でやりますか？:"))

        if select_point == 301 or 501:
            self.round = 10
        elif select_point == 701 or 901:
            self.round = 15
        else:
            self.round = 20

        self.player_point = [select_point for i in range(self.num_player)]
        print(self.player_point)

    def getPoint(self, _point=None):
        if _point is None:
            point = input()
        else:
            point = _point

        if point is "":
            point = 0
        if point == "50":
            point = int(point)
        else:
            point = int(point)
        return point

    def minusPoint(self, _player, _point):
        point = self.player_point[_player]
        self.player_point[_player] -= _point
        if self.player_point[_player] == 0:
            print("player", _player + 1, "  Win!")
            return True
        elif self.player_point[_player] < 0:
            self.player_point[_player] = point
        else:
            print("残り点", self.player_point)

    def changePlayer(self, _player):
        next_player = _player + 1
        if next_player < self.num_player:
            return next_player
        else:
            return 0

    def zero_one(self):
        self.gameInit()
        player = 0
        for r in range(self.round):
            print("Round", r + 1)
            print("プレイヤー", player + 1, "の番です[", self.player_point[player], "]")
            for i in range(3):
                while 1:
                    if db.point():
                        if self.minusPoint(player, db.point_nomal):
                            return
                        else:
                            break
            player = self.changePlayer(player)
        print("終了")


if __name__ == '__main__':
    z = Zero_one()
    z.zero_one()
