import os

from tennews.base import APINewsSource, News

class NewsAPISource(APINewsSource):
    url = "https://newsapi.org/v2/everything"
    parameters = {"apiKey": os.environ.get("NEWS_API_TOKEN")}
    query = "tech"

    def get_news(self, limit: int) -> list[News]:
        if self.parameters["apiKey"] is None:
            msg = "Missing API key for NewsAPI.org"
            raise ValueError(msg)
        news_resp = self.session.get(self.url, params={"q": self.query})
        news_resp.raise_for_status()
        news = news_resp.json()["articles"]
        return [
            News(
                address=article["url"],
                source=self,
                title=article["title"],
            )
            for article in news[:limit]
        ]


if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    news_api = NewsAPISource()
    print(news_api.get_news(1))
