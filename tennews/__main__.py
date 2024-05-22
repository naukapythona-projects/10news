from __future__ import annotations

from argparse import ArgumentParser

from tennews.base import NewsSource
from tennews.sources.developertech import DeveloperTechSource
from tennews.sources.devto import DevToSource
from tennews.sources.newsapi import NewsAPISource
from tennews.sources.thehackernews import TheHackerNewsSource


def get_urls(news_sources: list[NewsSource], limit: int) -> list[str]:
    urls: list[str] = []
    per_source, remainder = divmod(limit, len(news_sources))
    for news_source in news_sources:
        urls.extend(news.address for news in news_source.get_news(per_source + remainder))
        remainder = 0
    return urls


def main(limit: int) -> None:
    sources = [
        DeveloperTechSource(),
        DevToSource(),
        NewsAPISource(),
        TheHackerNewsSource(),
    ]
    urls: list[str] = get_urls(sources, limit=limit)
    for i, url in enumerate(urls, start=1):
        print(i, url)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("limit", nargs="?", default=10, type=int)
    args = parser.parse_args()
    main(args.limit)
