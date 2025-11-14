import random
import string

def random_function(min=1,max=50):
    length = random.randint(min,max)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print("Функція рандом відпрацювала.")

def tf9_creation(file_name = "TF9_1.txt",lines = 13):
    with open(file_name,"w",encoding="utf-8") as f:
        for _ in range(lines):
            f.write(random_function(1,120) + "\n")
        
print("Файл TF9_1.txt створено.")

    
    
    