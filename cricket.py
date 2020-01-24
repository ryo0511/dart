# -*- coding:utf-8 -*-
# import darts_bord
# db = darts_bord.Bord()
# POINT = [20, 19, 18, 17, 16, 15, 25]


class Cricket():
    def gameInit(self):
        self.player_point = []
        self.num_player = int(input("何人でやりますか？:"))
        self.player_point = [[3, 3, 3, 3, 3, 3, 3, 0]
                             for i in range(self.num_player)]
        self.blind = [0, 0, 0, 0, 0, 0, 0]

        print(self.player_point)

    def getPoint(self, _point=None):
        if _point is None:
            point = input()
        else:
            point = _point

        if point is "":
            point = 0
        else:
            point = int(point)
        return point

    def changePlayer(self, _player):
        next_player = _player + 1
        if next_player < self.num_player:
            return next_player
        else:
            return 0

    def minus_array(self, _pp, _point, _multiple):
        if self.blind[_point] != 1:
            if _pp[_point] == 0:
                _pp[7] += POINT[_point] * _multiple
            elif _pp[_point] == 1 and _multiple == 3:
                _pp[_point] -= 1
                _pp[7] += POINT[_point] * 2
            elif _pp[_point] == 2 and _multiple == 3:
                _pp[_point] -= 2
                _pp[7] += POINT[_point]
            elif _pp[_point] == 1 and _multiple == 2:
                _pp[_point] -= 1
                _pp[7] += POINT[_point]
            else:
                _pp[_point] -= _multiple

        blind = True
        for num in range(self.num_player):
            if self.player_point[num][_point] != 0:
                blind = False
        if blind is True:
            self.blind[_point] = 1

        return _pp

    def minusPoint(self, _player, _point):
        pp = self.player_point[_player]

        if _point in [20, 201]:
            self.minus_array(pp, 0, 1)
        elif _point == 202:
            self.minus_array(pp, 0, 2)
        elif _point == 203:
            self.minus_array(pp, 0, 3)
        elif _point in [19, 201]:
            self.minus_array(pp, 1, 1)
        elif _point == 192:
            self.minus_array(pp, 1, 2)
        elif _point == 193:
            self.minus_array(pp, 1, 3)
        elif _point in [18, 181]:
            self.minus_array(pp, 2, 1)
        elif _point == 182:
            self.minus_array(pp, 2, 2)
        elif _point == 183:
            self.minus_array(pp, 2, 3)
        elif _point in [17, 171]:
            self.minus_array(pp, 3, 1)
        elif _point == 172:
            self.minus_array(pp, 3, 2)
        elif _point == 173:
            self.minus_array(pp, 3, 3)
        elif _point in [16, 161]:
            self.minus_array(pp, 4, 1)
        elif _point == 162:
            self.minus_array(pp, 4, 2)
        elif _point == 163:
            self.minus_array(pp, 4, 3)
        elif _point in [15, 151]:
            self.minus_array(pp, 5, 1)
        elif _point == 152:
            self.minus_array(pp, 5, 2)
        elif _point == 153:
            self.minus_array(pp, 5, 3)
        elif _point in [25, 251]:
            self.minus_array(pp, 6, 1)
        elif _point in [50, 501]:
            self.minus_array(pp, 6, 2)

        self.player_point[_player] = pp
        print("     |", end="")
        for pn in range(self.num_player):
            print(pn + 1, end="  |")
        print()
        print("------", end="")
        for pn in range(self.num_player):
            print(end="----")
        print()
        for i, num in enumerate(["20", "19", "18", "17",
                                 "16", "15", "B "]):
            print(num, end="   |")
            for p in range(self.num_player):
                if self.player_point[p][i] == 3:
                    print("  ", end=" |")
                elif self.player_point[p][i] == 2:
                    print(" /", end=" |")
                elif self.player_point[p][i] == 1:
                    print(" X", end=" |")
                elif self.player_point[p][i] == 0:
                    print(" @", end=" |")
            print()
        print("pt   |", end="")
        for p in range(self.num_player):
            if self.player_point[p][7] < 10:
                print(self.player_point[p][7], end="  |")
            elif self.player_point[p][7] < 100:
                print(self.player_point[p][7], end=" |")
            else:
                print(self.player_point[p][7], end="|")
        print()

        print(self.player_point[_player][0:7])
        if self.player_point[_player][0:7] == [0, 0, 0, 0, 0, 0, 0]:
            print("Game　Set！")
            return True

    def cricket(self):
        self.gameInit()
        player = 0
        for _round in range(20):
            print("プレイヤー", player + 1, "の番です")
            for i in range(3):
                while 1:
                    if db.point():
                        if self.minusPoint(player, db.point_pass):
                            return
                        else:
                            break
            player = self.changePlayer(player)
        print("ゲーム終了です。")
        print("お疲れ様でした。")
        print("最終結果")
        print(self.player_point)


if __name__ == '__main__':
    c = Cricket()
    c.cricket()
