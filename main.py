import requests,time
import bs4
from clint.textui import progress
import zipfile
from os import listdir
import os.path
from os.path import isfile, join

url_search = "https://www.mangageko.com/manga/"
url_read = "https://www.mangageko.com/reader/en/"
url_sample_search = "https://www.mangageko.com/manga/i-can-snatch-999-types-of-abilities/"
url_sample_read = "https://www.mangageko.com/reader/en/becoming-a-legendary-ace-employee-chapter-0-eng-li/"

def get_manga_info(url,name):
    try:
        mangageko = requests.get(url)

        source = bs4.BeautifulSoup(mangageko.text,'lxml')

        Synopsis = source.find('p', class_="description")

        Stats = source.find('div', class_="header-stats")
        
        entry_point = source.find('a', id="readchapterbtn")
        entry_point = ((str(entry_point).split('"')[5]).split("-")[0]).split(" ")[1]
        
        book_stats = (Stats.text).split()
        total_chapters = book_stats[1].split('-')[0]
        book_info = {
            "Name": name,
            book_stats[2]:total_chapters,
            book_stats[6]:book_stats[4],
            book_stats[11]:book_stats[10],
            "Reader":str(entry_point)+" to "+str(total_chapters),
            "Synopsis":(Synopsis.text).replace('\n','')
        }
        
        print(book_info)
        
        select_chapter = input("Select chapter("+str(entry_point)+" to "+str(total_chapters)+"): ")
        
        if int(select_chapter) < int(entry_point) or int(select_chapter) > int(total_chapters):
            print("Chapter not found")
            exit()
        else:
            manga_name = "-".join(name.split(" "))
            url_read_ = url_read+manga_name+"-chapter-"+str(select_chapter)+"-eng-li/"
            print(url_read_)
            get_manga_chapters(url_read_,select_chapter)
            
        
        
    except Exception as e:
        print("Manga not found")
        print(e)
        exit()

def get_manga_chapters(url,chapter):    
    try:
        mangageko = requests.get(url)
        source = bs4.BeautifulSoup(mangageko.text,'lxml')
        chapters = source.find('div', id="chapter-reader")

        images = chapters.find_all('img')
        for image in images:
            image_url = str(image).split('"')[5]
            download_file(image_url,chapter)
    except Exception as e:
        print("Chapter not found")
        print(e)
        exit()


def download_file(url,chapter):
    try:
        req = requests.get(url)
        filename = req.url[url.rfind('/')+1:]
        file_name = "Downloads/chapter"+str(chapter)+"_"+filename
        with open(file_name, 'wb') as f:
            total_length = int(req.headers.get('content-length'))
            for chunk in progress.bar(req.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
        
    except Exception as e:
        print(e)

manga_name = input("Enter manga name: ").lower()
get_manga_info(url_sample_search,manga_name)


# i can snatch 999 types of abilities