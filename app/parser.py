from bs4 import BeautifulSoup

def parse_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    # title of the page
    title = soup.title.text.strip() if soup.title else None
    # meta description of the page
    meta_description = soup.find("meta", attrs={"name": "description"})["content"].strip() if soup.find("meta", attrs={"name": "description"}) else None
    # h1
    h1 = len(soup.find_all("h1")) if soup.find_all("h1") else 0
    # img with no alt attribute
    img = soup.find_all("img")
    img_no_alt = 0
    for image in img:
        if  not image.has_attr("alt"):
            img_no_alt += 1
    # word count
    text = soup.body.get_text() if soup.body else soup.get_text()
    words =text.split()
    word_count = len(words)



    return {
        "title": title,
        "meta_description": meta_description,
        "h1_count": h1,
        "img_no_alt": img_no_alt,
        "word_count": word_count
    }