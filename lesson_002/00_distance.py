#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2)**0.5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2)**0.5
london_paris = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Paris'] = moscow_paris

print(distances)
# Обратите внимание - я удалил лишние расчёты (расстояние между двумя городами всегда одно)
#зачет!
