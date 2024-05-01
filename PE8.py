from bs4 import BeautifulSoup
from urllib.request import urlopen
import functools
import operator
import requests
from euler_lib import *
def get_problem_attr(url):
    with urlopen(url) as page:
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
    return soup.find(["div","p"], class_="monospace center").get_text()
def euler_8():
    url = "https://projecteuler.net/problem=8"
    digits = ''
    string_lines = get_problem_attr(url)
    for line in string_lines:
        digits += line.strip()
    print(f"digits: {digits}")
    #take digits 13 at a time, starting at idx 0
    #take the product
    #if product bigger than current max, set to new max
    max_product = 1

    for attempt in range(len(digits)-13):
        product = 1
        for i in range(13):
            product *= int(digits[attempt + i])
        max_product = max(max_product, product)
    print(max_product)
def euler_11():
    string_lines = get_problem_attr('https://projecteuler.net/minimal=11')
    #ingest 2-d array
    arr = []
    
    for line in string_lines.strip().splitlines():
        row = []
        for s in line.split():
            row.append(int(s))
        arr.append(row)
        #print(arr)
    print(arr)
    #use 2-d array to find valid 4-length sequences of up,left,down,right, diagonal
    #vert, horiz, diagonals
    #lists are of the form list[y][x]
    candidates = set()
    #horizontals
    for y in range(20):
        for x in range(20-4):
            candidates.add(tuple(arr[y][x:x+4]))
    #verticals
    for y in range(20-4):
        for x in range(20):
            candidates.add((
                arr[y][x]
                ,arr[y+1][x]
                ,arr[y+2][x]
                ,arr[y+3][x]
            )
            )
    #diagonals
    for y in range(20-4):
        for x in range(20-4):
                candidates.add((
                arr[y][x]
                ,arr[y+1][x+1]
                ,arr[y+2][x+2]
                ,arr[y+3][x+3]
            )
            )
        #diagonals
    for y in range(20-4):
        for x in range(3,20):
                candidates.add((
                arr[y][x]
                ,arr[y+1][x-1]
                ,arr[y+2][x-2]
                ,arr[y+3][x-3]
            )
            )
    max_prod = 1
    for adjacents in candidates:

        product = functools.reduce(operator.mul, adjacents.values())
        max_prod = max(product, max_prod)
    print(f"max prod: {max_prod}")

def euler_13():
    url = "https://projecteuler.net/minimal=13"
    text = get_problem_attr(url)
    numbers = text.split()
    first_12s = [int(number[:12])for number in numbers]

    print(first_12s)
    sigma = sum(first_12s)
    print(f"first 10 digits = {sigma:,}")
def euler_42():
    base_url = 'https://projecteuler.net'
    problem_url = '/minimal=42'
    
    with urlopen(base_url+problem_url) as page:
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html,"html.parser")
    link = soup.find("a")
    print(link["href"])
    doc_url = '/'+link["href"]
    file_name = 'words.txt'
    words = requests.get(base_url+doc_url)
    with open(file_name,"w") as save_file:
        save_file.write(words.text)
    with open(file_name) as word_file:
        words = []
        csvreader = csv.reader(word_file,delimiter=',')
        for row in csvreader:
            words.extend(row)
    word_scores = [name_score(word) for word in words]
    are_triangles = list(filter(is_triangle_number, word_scores))
    print(len(are_triangles))
if __name__ == "__main__":
    euler_42()
    
    