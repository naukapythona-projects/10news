import pprint
from tennews.base import RSSNewsSource, News


class DevToSource(RSSNewsSource):
    url = "https://dev.to/feed"

    def get_news(self, limit: int) -> list[News]:
        return [
            News(
                address=entry["link"],
                source=self,
                title=entry["title"],
            )
            for entry in self.feed["entries"][:limit]
        ]


if __name__ == "__main__":
    devto = DevToSource()
    pprint.pprint(devto.get_news(2))
