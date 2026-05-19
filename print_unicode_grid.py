import requests
from bs4 import BeautifulSoup


def unicode_print(doc_url):
    html = requests.get(doc_url).text
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    pts = {}
    max_x = max_y = 0

    for row in rows[1:]:
        #print(row)
        cols = row.find_all('td')
        if len(cols) >= 3:
            x = int(cols[0].get_text(strip=True))
            char = cols[1].get_text()
            y = int(cols[2].get_text(strip=True))
            pts[(x, y)] = char
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    if not pts:
        print("No valid coordinates found.")
        return
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for (x, y), char in pts.items():
        grid[y][x] = char

    for y in range(max_y, -1, -1):
        print(''.join(grid[y]))

unicode_print("https://docs.google.com/document/d/e/2PACX-1vQQ6StxOq57qWhoZW6kM6jEKEkmNIiPpXTfHfbuWvwHft4mg2crttFte4i-YCQEczR0p_BVqbLfBqwl/pub")

"""
Example of the raw table data being extracted:

x-coordinate
Character
y-coordinate
0
█
0
0
█
1
0
█
2
1
▀
1
1
▀
2
2
▀
1
2
▀
2
3
▀
2

"""