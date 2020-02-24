import csv
import json

books_list = []

with open('books.csv') as books:
    reader = csv.reader(books)
    for i, b in enumerate(reader):
        chapters = int(b[2])
        if chapters == 0:
            chapters = 1
        books_list.append({
            'index': i + 1,
            'short': b[0],
            'name': b[1],
            'chapters': chapters,
            'part': 'ot' if i < 39 else 'nt',
        })

d = {
    'books': books_list
}

with open('books.json', 'w', encoding='utf-8') as books:
    json.dump(d, books, indent=2, ensure_ascii=False)
