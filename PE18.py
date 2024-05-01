from bs4 import BeautifulSoup
from urllib.request import urlopen
import functools
import operator
from collections import deque
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.v = value
    def __repr__(self):
        return f"{self.v=} self.left: {self.left!r} self.right: {self.right!r}"
def euler_18():
    url = "https://projecteuler.net/problem=18"
    triangle_base = 15
    position = 0
    with open("euler_18.txt") as page:
        html = page.read()
        soup = BeautifulSoup(html, "html.parser")
    potential_matches = soup.findAll(["div","p"], class_="monospace center")
    tree_string = potential_matches[1].get_text()
    root = build_list_from_string(tree_string)
    entire_triangle = [elem for elem in root]
    sum_row = entire_triangle[position:position + triangle_base]
    position += triangle_base
    triangle_base -=1
    curr_row = entire_triangle[position:position + triangle_base]
    while position < len(entire_triangle):      
        for i, num in enumerate(curr_row):
            if sum_row[i] > sum_row[i+1]:
                curr_row[i] += sum_row[i]
            else:
                curr_row[i] += sum_row[i+1]
        print(curr_row)

        sum_row = curr_row
        position += triangle_base
        triangle_base -= 1
        curr_row = entire_triangle[position:position + triangle_base]
        print(curr_row)
def build_list_from_string(tree_string: str) -> list:
    if not tree_string:
        return None
    values = tree_string.split()
    values = map(int, values)
    print(values)
    return reversed([value for value in values])
if __name__ == "__main__":
    euler_18()
"""
0 1,2
1 3,4
2 4,5
3 6,7
4 7,8
5 8,9
6 10,11
"""