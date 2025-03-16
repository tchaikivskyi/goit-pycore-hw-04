def get_cats_info(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                id, name, age = line.strip().split(',')
                cats.append({
                    "id": id,
                    "name": name,
                    "age": age,
                })
            return cats
    except FileNotFoundError:
        print("File not exist.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    
list_cats = get_cats_info('task2/cats.txt')
for cat in list_cats:
    print(cat)