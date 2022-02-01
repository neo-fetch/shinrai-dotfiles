import requests
import sys

# Get the joke from the website
def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Something went wrong: {}".format(response.status_code))
        sys.exit()


# print the joke
print(get_joke()["joke"])
