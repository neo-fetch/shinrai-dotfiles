# Get programmer dad joke from reddit:
import random
import re
import sys
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


try:
    jsondata = requests.get('https://www.reddit.com/r/ProgrammerDadJokes.json').json()
    # print(jsondata)
    df=pd.DataFrame(jsondata)
    i = random.choice(df['data']['children'])
    # print(f"{i['data']['title']}\n\t{re.sub('&amp;#x200B;', '', i['data']['selftext'])}\n")
    
    img = Image.new('RGB', (2560, 1080), color = (69, 39, 44))
    
    fnt = ImageFont.truetype('/usr/share/fonts/noto/NotoSansMono-Bold.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((960,405), f"{i['data']['title']}\n{re.sub('&amp;#x200B;', '', i['data']['selftext'])}", font=fnt, fill=(248, 228, 215))

    img.save('/tmp/joke.png')
except:
    img = Image.new('RGB', (2560, 1080), color = (69, 39, 44))
    
    fnt = ImageFont.truetype('/usr/share/fonts/noto/NotoSansMono-Bold.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((960,405), get_joke()["joke"], font=fnt, fill=(248, 228, 215))

    img.save('/tmp/joke.png')


background = Image.open("/tmp/screen.png")
overlay = Image.open("/tmp/joke.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("/tmp/screen.png","PNG")