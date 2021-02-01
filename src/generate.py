#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from copy import copy
from pprint import pprint
from jinja2 import Template

heroes = {
    "ana": {"name": "Ana", "matches": ["ana"]},
    "ashe": {"name": "Ashe", "matches": ["ashe"]},
    "baptiste": {"name": "Baptiste", "matches": ["baptiste", "bap"]},
    "bastion": {"name": "Bastion", "matches": ["bastion"]},
    "brigitte": {"name": "Brigitte", "matches": ["brig", "brigitte"]},
    "dva": {"name": "D.Va", "matches": ["dva", "d.va"]},
    "doomfist": {"name": "Doomfist", "matches": ["doom", "fist", "doomfist"]},
    "echo": {"name": "Echo", "matches": ["echo"]},
    "genji": {"name": "Genji", "matches": ["genji"]},
    "hanzo": {"name": "Hanzo", "matches": ["hanzo"]},
    "junkrat": {"name": "Junkrat", "matches": ["junk", "rat", "junkrat"]},
    "lucio": {"name": "Lucio", "matches": ["lucio"]},
    "mccree": {"name": "McCree", "matches": ["mccree"]},
    "mei": {"name": "Mei", "matches": ["mei"]},
    "mercy": {"name": "Mercy", "matches": ["mercy"]},
    "moira": {"name": "Moira", "matches": ["moira"]},
    "orisa": {"name": "Orisa", "matches": ["orisa"]},
    "pharah": {"name": "Pharah", "matches": ["pharah"]},
    "reaper": {"name": "Reaper", "matches": ["reaper"]},
    "reinhardt": {"name": "Reinhardt", "matches": ["reinhardt", "rein"]},
    "roadhog": {"name": "Roadhog", "matches": ["roadhog", "hog"]},
    "sigma": {"name": "Sigma", "matches": ["sigma"]},
    "soldier": {"name": "Soldier: 76", "matches": ["soldier", "soldier:76"]},
    "sombra": {"name": "Sombra", "matches": ["sombra"]},
    "symmetra": {"name": "Symmetra", "matches": ["symmetra"]},
    "torbjorn": {"name": "Torbjorn", "matches": ["torb", "torbjorn"]},
    "tracer": {"name": "Tracer", "matches": ["tracer"]},
    "widowmaker": {"name": "Widowmaker", "matches": ["widow", "widowmaker"]},
    "winston": {"name": "Winston", "matches": ["winston", "ape", "monkey", "bubble"]},
    "wreckingball": {
        "name": "Wrecking Ball",
        "matches": ["ball", "hammond", "hamster"],
    },
    "zarya": {"name": "Zarya", "matches": ["personalbubble", "zarya"]},
    "zenyatta": {"name": "Zenyatta", "matches": ["zenyatta", "zen"]},
}

ranks = {
    "qp": {"name": "Quick Play", "colour": "blue"},
    "newbie": {"name": "Newbie", "colour": "blue"},
    "bronze": {"name": "Bronze", "colour": "brown"},
    "silver": {"name": "Silver", "colour": "grey"},
    "gold": {"name": "Gold", "colour": "yellow"},
    "plat": {"name": "Plat", "colour": "teal"},
    "diamond": {"name": "Diamond", "colour": "white"},
    "masters": {"name": "Masters", "colour": "black"},
}

hero_match = {}
for key, value in heroes.items():
    for match in value["matches"]:
        hero_match[match] = key


def rank_to_colour(rank):
    return ranks[rank].get("colour", "black")


rank_set = set(ranks.keys())


def parse_results():
    results = {}
    results["heroes"] = copy(heroes)
    results["ranks"] = copy(ranks)
    with open("results.json", "r") as results_file:
        base = json.load(results_file)
    for item in base:
        title = (
            item["snippet"]["title"]
            .lower()
            .replace("/", " ")
            .replace("&#39;", "'")
            .replace("soldier: 76", "soldier:76")
            .replace("personal bubble", "personalbubble")
            .replace("quick play", "qp")
            .replace("'s", "")
        )
        title_tags = set(title.split(" "))
        hero_tags = set()
        rank_tags = rank_set.intersection(title_tags)
        for tag in title_tags:
            if tag in hero_match:
                hero_tags.add(hero_match[tag])
        item["heroes"] = hero_tags
        item["rank"] = rank_tags
        for hero in hero_tags:
            results["heroes"][hero].setdefault("videos", [])
            results["heroes"][hero]["videos"].append(item)
        for rank in rank_tags:
            results["ranks"][rank].setdefault("videos", [])
            results["ranks"][rank]["videos"].append(item)
    return results


def main():
    results = parse_results()
    with open("templates/index.html.jinja2", "r") as template_file:
        template = Template(template_file.read())
    renders = ["index"] + list(results["heroes"].keys()) + list(ranks)
    if not os.path.isdir('dist'):
        os.mkdir('dist')
    for active in renders:
        print(f"Writing {active}.html")
        html = template.render(
            results=results, active=active, rank_to_colour=rank_to_colour
        )
        with open(f"dist/{active}.html", "w") as html_file:
            html_file.write(html)


main()
