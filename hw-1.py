def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        total_sum = 0
        count = 0
        
        for line in lines:
            name, salary = line.strip().split(',')
            total_sum += int(salary)
            count += 1
        
        average_salary = total_sum / count if count != 0 else 0
        result = f"Total - {total_sum}, Average - {average_salary}"
        return result
    
    except FileNotFoundError:
        return f"File {path} not found."
        
    except Exception as e:
        return f"Error: {e}"

path = 'txt-files/salaries.txt'
print(total_salary(path))
