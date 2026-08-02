# GUA — GitHub Trending CLI

A small CLI that fetches and displays trending repositories from GitHub.

Sample solution for the [GitHub Trending CLI](https://roadmap.sh/projects/github-trending-cli)
challenge from [roadmap.sh](https://roadmap.sh).

## Installation

Requires Python 3.9+.

```bash
pip install -e .
```

This installs the `github_trending` command.

## Hello Test

run

```bash
github_trending greet
```

## Usage

```bash
github_trending --duration <day> --limit <n>
```

### Options

| Option       | Description                                      | Recommendation |
|-------------|--------------------------------------------------|---------|
| `--duration` | Time range to filter trending repos by.          | `7`  |
| `--limit`    | Number of repositories to display.               | `10`    |

### Examples

Fetch the top 20 trending repositories of last 10 days:

```bash
github_trending --duration 10 --limit 20
```

Fetch the top 5 trending repositories from yesterday to today:

```bash
github_trending --duration 1 --limit 5
```

Run it with no arguments to use the defaults (`7`, limit `10`):

```bash
github_trending
```

## Features

- Fetches trending repositories from the GitHub API (no authentication required).
- Sorts repositories by star count.
- Displays repository name, number of stars, and their html_URL.
- Robust error handling for invalid input and API errors.
