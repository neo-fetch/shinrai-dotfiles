# Get programmer dad joke from reddit:
import random
import re
import sys
# from turtle import width
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Something went wrong: {}".format(response.status_code))
        sys.exit()

background = Image.open("/tmp/screen.png")
width, height = background.size

try:
    jsondata = requests.get('https://www.reddit.com/r/ProgrammerDadJokes.json').json()
    # print(jsondata)
    df=pd.DataFrame(jsondata)
    i = random.choice(df['data']['children'])
    # print(f"{i['data']['title']}\n\t{re.sub('&amp;#x200B;', '', i['data']['selftext'])}\n")
    
    img = Image.new('RGB', (width, height), color = (69, 39, 44))
    
    fnt = ImageFont.truetype('/usr/share/fonts/liberation/LiberationMono-Bold.ttf', 17)
    d = ImageDraw.Draw(img)
    punchline = re.sub('&amp;#x200B;', '', i['data']['selftext'])
    d.text((((width-len(punchline)*10)/2),height/2), f"{i['data']['title']}\n{punchline}", font=fnt, fill=(248, 228, 215))

    img.save('/tmp/joke.png')
except:
    img = Image.new('RGB', (width, height), color = (69, 39, 44))
    
    fnt = ImageFont.truetype('/usr/share/fonts/liberation/LiberationMono-Bold.ttf', 17)
    d = ImageDraw.Draw(img)
    joke = get_joke()["joke"]
    d.text((((width - len(joke)*10)/2),height/2), joke, font=fnt, fill=(248, 228, 215))

    img.save('/tmp/joke.png')


overlay = Image.open("/tmp/joke.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("/tmp/screen.png","PNG")