#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from copy import copy
from jinja2 import Template
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

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
    "grandmasters": {"name": "GrandMasters", "colour": "black"},
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


def generate_search_data(results):
    data = []
    for hero, hero_data in results["heroes"].items():
        data += [
            {
                "title": item["snippet"]["title"],
                "url": f"{hero}.html",
            }
            for item in hero_data.get("videos", [])
        ]
    return data


def sort_by_time(results):
    all_videos = [data.get("videos", []) for data in results["heroes"].values()]
    # Magic flatten incantiation
    all_videos = [item for sublist in all_videos for item in sublist]
    all_videos.sort(key=lambda d: d["snippet"]["publishedAt"])
    return all_videos


def main():
    results = parse_results()
    search_data = generate_search_data(results)
    sorted_results = sort_by_time(results)
    print(sorted_results[0:2])
    env = Environment(loader=FileSystemLoader("templates/"))
    template = env.get_template("index.html.jinja2")
    template.globals["now"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    template.globals["rank_to_colour"] = rank_to_colour

    renders = ["index"] + list(results["heroes"].keys()) + list(ranks)
    if not os.path.isdir("dist"):
        os.mkdir("dist")
    for active in renders:
        print(f"Writing {active}.html")
        html = template.render(
            results=results,
            active=active,
            search_data=search_data,
            sorted_results=sorted_results,
        )
        with open(f"dist/{active}.html", "w") as html_file:
            html_file.write(html)


main()
