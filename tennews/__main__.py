from __future__ import annotations


def get_urls() -> list[str]:
    return []


def main() -> None:
    urls: list[str] = ["https://wp.pl/"]  # here we get the news
    for url in urls:
        print(url)


if __name__ == "__main__":
    main()
