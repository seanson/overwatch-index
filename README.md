# overwatch-index

[Overwatch Index][https://seanson.github.com/overwatch-index]

This is a project for generating indexes of YouTube Overwatch gameplay and tagging them with the appropriate hero, rank, etc.

It is a very basic side-project at the moment and will likely see little development unless I find a proper use case for it.


## Development

This project uses Python Poetry for environment management.
Authentication requires setting up the YouTube API and generating an OAuth client secret  to `.client_secret.json`, which is a painful process and outside the scope of this project.

Data from YouTube is pulled with:

``` shell
poetry run python src/fetch.py
```

Static HTML is generated with:

``` shell
poetry run python src/generate.py
```

And deployment is done via `ghp-import`:

``` shell
ghp-import -p dist
```
