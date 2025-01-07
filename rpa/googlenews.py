import requests
from bs4 import BeautifulSoup


def main(keyword):
    url = f"https://news.google.com/search?q={keyword}=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        news = data_extract(soup)

        for item in news:
            for k, v in item.items():
                print(f"{k}:{v}")
            print()


def data_extract(soup):
    base_url = "https://news.google.com"

    news = []

    articles = soup.select("article")

    for article in articles:
        new_item = {}
        element = article.find("a", class_="JtKRv")

        title = element.text.strip()

        link = base_url + element["href"][1:]

        writer = article.find("div", class_="bInasb")
        if writer:
            writer = writer.text.strip()
        else:
            writer = ""

        datetime = article.find("time", class_="hvbAAd")["datetime"].split("T")
        date = datetime[0]
        time = datetime[1]

        new_item["title"] = title
        new_item["link"] = link
        new_item["writer"] = writer
        new_item["date"] = date
        new_item["time"] = time
        news.append(new_item)

    return news


if __name__ == "__main__":
    main("파이썬")
