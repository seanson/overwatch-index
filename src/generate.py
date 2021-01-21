#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

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
hero_match = {}
for key, value in heroes.items():
    for match in value["matches"]:
        hero_match[match] = key

comp_set = set(["qp", "bronze", "silver", "gold", "plat", "diamond"])


def parse_results():
    results = {}
    results["heroes"] = copy(heroes)
    results["comps"] = {key: [] for key in comp_set}

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
        comp_tags = comp_set.intersection(title_tags)
        for tag in title_tags:
            if tag in hero_match:
                hero_tags.add(hero_match[tag])
        item["heroes"] = hero_tags
        item["comp"] = comp_tags
        for hero in hero_tags:
            results["heroes"][hero].setdefault("videos", [])
            results["heroes"][hero]["videos"].append(item)
        for comp in comp_tags:
            results["comps"][comp].append(item)

    return results


def main():
    results = parse_results()
    with open("templates/index.html.jinja2", "r") as template_file:
        template = Template(template_file.read())
    with open("dist/index.html", "w") as html_file:
        print("Writing index.html")
        html = template.render(results=results, current_hero="ana")
        html_file.write(html)
    for current_hero in results["heroes"].keys():
        print(f"Writing {current_hero}.html")
        html = template.render(results=results, current_hero=current_hero)
        with open(f"dist/{current_hero}.html", "w") as html_file:
            html_file.write(html)


main()
