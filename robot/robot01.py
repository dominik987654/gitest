#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):
        ilu_wrogow = 0
        lista_wrogow = []

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                 if rg.dist(poz, self.location) <= 1:
                    lista_wrogow.append(poz)
                      #return ['attack', poz]
        if len(lista_wrogow) > 2:
            return['suicide']

        elif len(lista_wrogow):
            return ['attack', lista_wrogow[0]]

        print(game.robots)

        if self.location == rg.CENTER_POINT:
            return ['guard']


        # idź do środka planszy, ruch domyślny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]


