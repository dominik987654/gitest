#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:



    def act(self, game):

        def czy_wejscie(poz):
            if 'spawn' in rg.loc_types(poz):
                return True
            return False



             # ilu_wrogow = 0
        lista_wrogow_obok = []

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:           #rozpoznanie wroga
                if rg.dist(poz, self.location) <= 1:
                    lista_wrogow_obok.append(poz)
                    # ilu_wrogow += 1
                    # return ['attack', poz]
        print(lista_wrogow_obok)


        if len(lista_wrogow_obok) > 2:
            return['suicide']                                     #samobojstwo
        elif len(lista_wrogow_obok):
            return['attack', lista_wrogow[0]]                             #atak

        print(game.robots)

        if self.location == rg.CENTER_POINT:
            return ['guard']                                            #obrona

        if czy_wejscie(self.poz):
        # idź do środka planszy, ruch domyślny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
