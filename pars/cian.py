from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

# https://vologda.cian.ru/kupit-kvartiru/


PAUSE_DURATION_SECONDS = 1
# city1= str(input('Введите : '))
# room1 = str(input('Введите кол-во комнат: '))
# price_low1 = str(input('Введите минимальную цену: '))
# price_high1 = str(input('Введите максимальную цену: '))

def gett_data(city,room,price_low,price_high):


    driver = webdriver.Chrome(executable_path='HomePar\\pars\\chromedriver.exe')
    URL = f'https://{city}.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=1&maxprice={price_high}&minprice={price_low}&offer_type=flat&region=4708&room{room}=1'
    try:
        driver.get(URL)
        with open('homeparapp\\static\\homeparapp\\parsfile\\indcian.html', 'w', encoding="utf-8") as file:
            file.write(driver.page_source)
        sleep(PAUSE_DURATION_SECONDS)
    
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
    return URL



def get_items_urls(file_path):
    with open(file_path, encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', class_='_93444fe79c--general--BCXJ4')

    urls = []
    for item in items_divs:
        item_url = item.find('div', class_='_93444fe79c--container--kZeLu _93444fe79c--link--DqDOy').find('a').get('href')
        urls.append(item_url)

    with open('homeparapp\\static\\homeparapp\\parsfile\\infocian.txt', 'w', encoding="utf-8") as file:
        for url in urls:
            file.write(f'{url}\n')
    return 'Вы собрали данные'

def maincian(city2,room2,price_low2,price_high2):
    global city1
    global room1
    global price_low1
    global price_high1 
    city1=city2
    room1=room2
    price_low1=price_low2
    price_high1 =price_high2
    gett_data(city2,room2,price_low2,price_high2)
    print(get_items_urls(file_path='homeparapp\\static\\homeparapp\\parsfile\\indcian.html'))

if __name__ == '__main__':
    
    maincian(city1,room1,price_low1,price_high1)