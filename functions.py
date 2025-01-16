import requests


def get_response(url, count=None):
    params = {"count": count}

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response


def get_images():

    SPACEX_URL = 'https://api.spacexdata.com/v5/launches/latest'
    count = 10

    spacex_response = get_response(SPACEX_URL, count)

    spacex_urls = spacex_response.json()["links"]["flickr"]["original"]

    if not spacex_urls:
        SPACEX_URL = 'https://api.spacexdata.com/v5/launches/5eb87ce3ffd86e000604b336'

        spacex_response = get_response(SPACEX_URL, count)

        spacex_urls = spacex_response.json()["links"]["flickr"]["original"]

    images = []

    for url in spacex_urls:
        pic = get_response(url).content
        images.append(pic)

    return images


