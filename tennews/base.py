from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import ClassVar

import bs4
import feedparser  # type: ignore[import-untyped]
import requests


@dataclass
class News:
    address: str
    source: NewsSource
    title: str


class NewsSource(metaclass=ABCMeta):
    @abstractmethod
    def get_news(self, limit: int) -> list[News]:
        """Interface for getting news from a new source."""


class RSSNewsSource(NewsSource, metaclass=ABCMeta):
    url: ClassVar[str]

    def __init__(self) -> None:
        self.doc = requests.get(self.url).text
        self.feed = feedparser.parse(self.doc)


class APINewsSource(NewsSource, metaclass=ABCMeta):
    url: ClassVar[str]
    headers: dict[str, str | bytes] = {}
    parameters: dict[str, str | None] = {}

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.params.update(self.parameters)  # type: ignore[union-attr]


class BS4NewsSource(APINewsSource, metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
        self.bs4 = bs4.BeautifulSoup()
