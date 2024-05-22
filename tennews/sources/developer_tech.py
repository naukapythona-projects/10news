import pprint
from tennews.base import RSSNewsSource, News


class DeveloperTechSource(RSSNewsSource):
    url = "https://www.developer-tech.com/feed/"

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
    dt = DeveloperTechSource()
    pprint.pprint(dt.get_news(2))
