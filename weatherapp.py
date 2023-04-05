import json
import requests
from datetime import date
from PIL import Image, ImageFont, ImageDraw

api_key = "5ded225ec6db21c6c91f3cbbb2866acd"
position = [300, 430, 555, 690, 825]

us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
jp_list = ["Tokyo", "Fukushima", "Kyoto", "Sapporo", "Nagoya"]
uk_list = ["London", "Birmingham", "Manchester", "York", "Edinburgh"]
de_list = ["Berlin", "Hamburg", "Cologne", "Munich", "Leipzig"]
ua_list = ["Kyiv", "Kherson", "Kharkiv", "Mariupol", "Luhansk"]

#countrydict = {
#    "us": {"country": [us_list]},
#    "jp": {"country": [jp_list]},
#    "uk": {"country": [uk_list]},
#    "de": {"country": [de_list]},
#    "ua": {"country": [ua_list]}
#}

def countryfunc(us_list, country):
    for cities in us_list:
        image = Image.open("post.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Inter.ttf", size = 50)
        content = "Latest Weather Forecast"
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 77,)
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size = 30)
        today = date.today()
        content = date.today().strftime("%A - %B %D, %Y")
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 145)
        draw.text((x, y), content, color, font=font)

    index = 0

    for city in cities:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        #city
        font = ImageFont.truetype("Inter.ttf", size=50)
        color = "rgb(0, 0, 0)"
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        #temperature
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["temp"]) + "\u00b0"
        color = "rgb(255, 255, 255)"
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        #humidity
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["humidity"]) + "%"
        color = "rgb(255, 255, 255)"
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
    image.save(country + "cities_pd9.png")

countryfunc([us_list], "us")
countryfunc([uk_list], "uk")
countryfunc([ua_list], "ua")
countryfunc([de_list], "de")
countryfunc([jp_list], "jp")
print("Images saved to /home/autumn/PycharmProjects/school")