def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        cats_info = []
        
        for line in lines:
            id, name, age = line.strip().split(',')
            cat = {
                "id": id,
                "name": name,
                "age": int(age)
            }
            cats_info.append(cat)
        
        return cats_info
    
    except FileNotFoundError:
        print(f"File {path} not found.")
        return []
    
    except Exception as e:
        print(f"Error: {e}")
        return []

path = 'txt-files/cats.txt'
print(get_cats_info(path))
