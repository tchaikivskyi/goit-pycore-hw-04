def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))
            if not salaries:
                return 0, 0
            total = float(sum(salaries))
            average = float(total / len(salaries))
            return total, average
    except FileNotFoundError:
        print("File not exist.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None
        
print(total_salary('task1/developers.txt'))