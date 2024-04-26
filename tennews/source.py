from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NewsURL:
    address: str
    source: NewsSource


class NewsSource:
    def get_news(self, limit: int) -> list[NewsSource]:
        return []
