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

## Usage

```bash
github_trending --duration <day|week|month|year> --limit <n>
```

### Options

| Option       | Description                                      | Default |
|-------------|--------------------------------------------------|---------|
| `--duration` | Time range to filter trending repos by.          | `week`  |
| `--limit`    | Number of repositories to display.               | `10`    |

### Examples

Fetch the top 20 trending repositories of the month:

```bash
github_trending --duration month --limit 20
```

Fetch the top 5 trending repositories of the day:

```bash
github_trending --duration day --limit 5
```

Run it with no arguments to use the defaults (`week`, limit `10`):

```bash
github_trending
```

## Features

- Fetches trending repositories from the GitHub API (no authentication required).
- Sorts repositories by star count.
- Displays repository name, description, number of stars, and primary language.
- Robust error handling for invalid input and API errors.
