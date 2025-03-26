import requests, webbrowser, json, lxml, time
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

#18.Збір даних з html сторінок. Робота з модулем request та бібліотекою lxml.
def del_data():
    with open("db/links.json", "w", encoding="utf-8") as file:
        pass

def get_data(url):
    attempts = 0
    while attempts < 3:
        try:
            ua = UserAgent()
            headers = {
                "Accept": "*/*" ,
                "User-Agent":ua.random
            }
            req = requests.get(url, headers=headers)
            req.raise_for_status()
            src = req.text
            with open(f"db/index.html", "w", encoding="utf-8") as file:
                file.write(src)
            return src
        except requests.exceptions.RequestException as e:
            if attempts < 3:
                 print(f"Ошибка при запросе {url}: {e}")
                 if input("do you want to try again? y/n: ").lower() != "y":
                    return None
                 print(f"attempts {attempts+1}/3")
                 attempts+=1
            else:
                print(f"attempts {attempts+1}/3")
                return None

def search(pg_num):
    del_data()
    if pg_num>50:
        pg_num = 50
    elif pg_num<=0:
        pg_num = 1

    data = {}
    for page in range(1,pg_num+1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        gt_dt = get_data(url)
        if gt_dt is None:
            print(f"Error on page {page}, stopping...")
            return
        with open(f"db/index.html", "r") as file:
            src = file.read()

        soup = bs(src, "lxml")
        products_class = soup.find_all(class_="product_pod")
        dictionary = {}

        for product in products_class:
            h3 = product.find("h3")
            title = h3.get_text().replace("...", "").strip()
            link = url[:-11] + h3.find("a")["href"]
            dictionary[title]=link

        data[f"page_{page}"]=dictionary
        print(f"page {page}/{pg_num} done\nwith {len(dictionary)} ellements\n{"#"*20}")

    with open("db/links.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    time.sleep(1)

if __name__ == "__main__":
    search(int(input("enter page quantity: ")))
