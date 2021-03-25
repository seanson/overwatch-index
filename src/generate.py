#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from copy import copy
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


heroes = {
    "ana": {
        "name": "Ana",
        "icon": "syringe",
        "class": "support",
        "matches": ["ana"],
    },
    "ashe": {
        "name": "Ashe",
        "icon": "bullseye",
        "class": "dps",
        "matches": ["ashe"],
    },
    "baptiste": {
        "name": "Baptiste",
        "icon": "clone outline",
        "class": "support",
        "matches": ["baptiste", "bap"],
    },
    "bastion": {
        "name": "Bastion",
        "icon": "whmcs",
        "class": "dps",
        "matches": ["bastion"],
    },
    "brigitte": {
        "name": "Brigitte",
        "icon": "flag outline",
        "class": "support",
        "matches": ["brig", "brigitte", "brigs"],
    },
    "dva": {
        "name": "D.va",
        "icon": "hand peace outline",
        "class": "tank",
        "matches": ["dva", "d.va"],
    },
    "doomfist": {
        "name": "Doomfist",
        "icon": "hand rock",
        "class": "dps",
        "matches": ["doom", "fist", "doomfist"],
    },
    "echo": {"name": "Echo", "icon": "clone outline", "class": "dps", "matches": ["echo"]},
    "genji": {"name": "Genji", "icon": "star outline", "class": "dps", "matches": ["genji"]},
    "hanzo": {"name": "Hanzo", "icon": "redo", "class": "dps", "matches": ["hanzo"]},
    "junkrat": {
        "name": "Junkrat",
        "icon": "bomb",
        "class": "dps",
        "matches": ["junk", "rat", "junkrat"],
    },
    "lucio": {"name": "Lucio", "icon": "music", "class": "support", "matches": ["lucio"]},
    "mccree": {
        "name": "McCree",
        "icon": "clock outline",
        "class": "dps",
        "matches": ["mccree"],
    },
    "mei": {"name": "Mei", "icon": "snowflake", "class": "dps", "matches": ["mei"]},
    "mercy": {"name": "Mercy", "icon": "medkit", "class": "support", "matches": ["mercy"]},
    "moira": {"name": "Moira", "icon": "circle outline", "class": "support", "matches": ["moira"]},
    "orisa": {"name": "Orisa", "icon": "sticker mule", "class": "tank", "matches": ["orisa"]},
    "pharah": {
        "name": "Pharah",
        "icon": "rocket",
        "class": "dps",
        "matches": ["pharah", "phara"],
    },
    "reaper": {
        "name": "Reaper",
        "icon": "cloudversify",
        "class": "dps",
        "matches": ["reaper"],
    },
    "reinhardt": {
        "name": "Reinhardt",
        "icon": "shield",
        "class": "tank",
        "matches": ["reinhardt", "rein"],
    },
    "roadhog": {
        "name": "Roadhog",
        "icon": "linkify",
        "class": "tank",
        "matches": ["roadhog", "hog"],
    },
    "sigma": {"name": "Sigma", "icon": "socks", "class": "tank", "matches": ["sigma"]},
    "soldier": {"name": "Soldier: 76", "icon": "dna", "class": "dps", "matches": ["soldier", "soldier:76"]},
    "sombra": {
        "name": "Sombra",
        "icon": "bug",
        "class": "dps",
        "matches": ["sombra"],
    },
    "symmetra": {
        "name": "Symmetra",
        "icon": "ethereum",
        "class": "dps",
        "matches": ["symmetra"],
    },
    "torbjorn": {
        "name": "Torbjorn",
        "icon": "hammer",
        "class": "dps",
        "matches": ["torb", "torbjorn"],
    },
    "tracer": {
        "name": "Tracer",
        "icon": "history",
        "class": "dps",
        "matches": ["tracer"],
    },
    "widowmaker": {
        "name": "Widowmaker",
        "icon": "eye",
        "class": "dps",
        "matches": ["widow", "widowmaker"],
    },
    "winston": {
        "name": "Winston",
        "icon": "sign language",
        "class": "tank",
        "matches": ["winston", "ape", "monkey", "bubble"],
    },
    "wreckingball": {
        "name": "Wrecking Ball",
        "icon": "bowling ball",
        "class": "tank",
        "matches": ["ball", "hammond", "hamster"],
    },
    "zarya": {
        "name": "Zarya",
        "icon": "arrow alt circle right",
        "class": "tank",
        "matches": ["personalbubble", "zarya", "beam"],
    },
    "zenyatta": {
        "name": "Zenyatta",
        "icon": "hand pointer outline",
        "class": "support",
        "matches": ["zenyatta", "zen"],
    },
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
            .replace("?", "")
            .replace("!", "")
            .replace(",", "")
            .replace(" gm ", " grandmasters ")
            .replace("gm ", "grandmasters ")
            .replace(" gm", "grandmasters ")
        )
        title_tags = set(title.split(" "))
        hero_tags = set()
        rank_tags = rank_set.intersection(title_tags)
        for tag in title_tags:
            if tag in hero_match:
                hero_tags.add(hero_match[tag])
        if not hero_tags:
            print(f"Warning: No hero tags found in {title_tags}")
        if not rank_tags:
            print(f"Warning: No rank tags found in {title_tags}")

        item["heroes"] = hero_tags
        item["rank"] = rank_tags
        for hero in hero_tags:
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
    all_videos.sort(key=lambda d: d["snippet"]["publishedAt"], reverse=True)
    return all_videos


def main():
    results = parse_results()
    search_data = generate_search_data(results)
    sorted_results = sort_by_time(results)
    env = Environment(loader=FileSystemLoader("templates/"))
    template = env.get_template("index.html.jinja2")
    template.globals["now"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    template.globals["rank_to_colour"] = rank_to_colour

    renders = ["index"] + list(results["heroes"].keys()) + list(ranks)
    if not os.path.isdir("dist"):
        os.mkdir("dist")
    with open("hero_results.json", "w") as json_file:
        json.dump(results, json_file, cls=SetEncoder)
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
