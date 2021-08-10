import requests

BASE = 'http://127.0.0.1:5000/'
img_url = r'https://upload.wikimedia.org/wikipedia/commons/1/17/Sudoku_puzzle_hard_for_brute_force.jpg'

response = requests.get(BASE+'process',{'img_url':img_url})
print(response.json())