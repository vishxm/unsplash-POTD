# libraries
import os
import requests
from bs4 import BeautifulSoup

# url to get the photo of the day id
url = "https://unsplash.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
photo_id = soup.find_all('a', '_2Mc8_ _3ZLHW _1HV49 _2WvKc')[0]['href'][8:]

# url for getting the photo from unsplash API
base_url = "https://source.unsplash.com/"
photo_url = base_url + photo_id + '/1920x1080'

# saving the photo 
image = requests.get(photo_url)

with open(os.path.expanduser('~/us-scraper/image.png'), 'wb') as f:
    f.write(image.content)
