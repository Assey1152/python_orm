from core import create_tables, load_data, find_books, easy_load_data

if __name__ == "__main__":
    create_tables()
    # load_data()
    easy_load_data()
    target = input("Insert id or name of publisher: ")
    data = find_books(target)
    for r in data:
        print(f'{r[0]} | {r[1]} | {r[2]}  | {r[3]}')
