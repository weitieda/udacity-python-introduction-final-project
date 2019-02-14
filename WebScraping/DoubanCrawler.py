import requests
from expanddouban import getHtml
from bs4 import BeautifulSoup
import csv

my_fav_movie_categories = ["歌舞", "冒险", "历史"]


class Movie:
    def __init__(self, name, rate, category, location, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.category = category
        self.location = location
        self.info_link = info_link
        self.cover_link = cover_link


def getMovieUrl(category, location, minRateValue=0):
    return f"https://movie.douban.com/tag/#/?sort=U&range={minRateValue},10&tags=电影,{category},{location}".strip(",")


def getMovies(category, location, minRateValue=0):
    html = getHtml(getMovieUrl(category, location, minRateValue), True)
    soup = BeautifulSoup(html, "html.parser")
    movie_tags = soup.find_all("a", class_="item")

    def construct_movie(movie_tag, location, category):
        name = movie_tag.find("span", class_="title").text
        rate = movie_tag.find("span", class_="rate").text
        info = movie_tag["href"]
        cover = movie_tag.find("img")["scr"]
        return Movie(name, rate, category, location, info, cover)

    return [construct_movie(tag, location, category) for tag in movie_tags]


def get_all_locations():
    html = getHtml(getMovieUrl("", ""))
    soup = BeautifulSoup(html, "html.parser")
    categories = soup.find_all("ul", class_="category")
    locations_tags = categories[2].find_all("span", class_="tag")[1:]
    return [location.text for location in locations_tags]


def export_fav_categories_csv():
    with open("movies.csv", mode="w") as movies_file:
        writer = csv.writer(movies_file)
        for category in my_fav_movie_categories:
            for location in get_all_locations():
                [writer.writerow([movie.name, movie.rate, movie.category, movie.location,
                                  movie.info_link, movie.cover_link]) for movie in getMovies(category, location, 9)]


def find_top_three_countries(category, movies):
    result: dict = {}
    movie_list = [movie for movie in movies if movie[2] == category]
    for movie in movie_list:
        if movie[3] in result:
            result[movie[3]] += 1
        else:
            result[movie[3]] = 1
    result_sorted = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
    top_3_ratios = [i[1] / len(movie_list) * 100 for i in result_sorted[0:3]]
    return list(zip(result_sorted[0:3], top_3_ratios))


def format_string(movies, category):
    result_string = ""
    for item in movies:
        result_string += f"{item[0][0]} {item[0][1]} 部, 占比 {item[1]:.2f}%\n"
    return f"{category}:\n{result_string}"


def count_fav_categories():
    with open("movies.csv") as file:
        reader = csv.reader(file)
        movie_list = list(reader)
        return [format_string(find_top_three_countries(category, movie_list), category) for category in my_fav_movie_categories]


# 执行下行会打开浏览器抓取自选的 3 类电影的所有信息
# export_fav_categories_csv()

with open('output.txt', 'w') as file:
    [file.write("%s\n" % item) for item in count_fav_categories()]
