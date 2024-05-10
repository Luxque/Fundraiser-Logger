import requests, re
from bs4 import BeautifulSoup


def getProgress(id: str) -> tuple:
    url = "https://camp-fire.jp/projects/view/" + id
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    titleData = soup.find('meta', attrs={'property': 'og:title'})
    title = re.sub(r'<meta content="|".*>', '', str(titleData))

    ownerData = soup.find('meta', attrs={'property': 'note:owner'})
    owner = re.sub(r'<meta content="|".*>', '', str(ownerData))

    fundData = soup.find_all('strong', attrs={'class': 'number'})
    raised = int(re.sub(r'\D', '', str(fundData[0])))
    goal = int(re.sub(r'\D', '', str(fundData[1])))

    return (title, owner, raised, goal)


if __name__ == '__main__':
    print("This is not the main Python script. Please use 'main.py' in this directory.")