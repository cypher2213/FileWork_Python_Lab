from utils import tf9_creation

tf9_creation()

input_file = "TF9_1.txt"
output_file = "TF9_2.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    for line in fin:
        line = line.rstrip("\n")

        if len(line) < 20:
            new_line = line + " " * (20 - len(line))
        else:
            new_line = line[:20]

        fout.write(new_line + "\n")
        
with open(output_file, "r", encoding="utf-8") as f:
    print("Виводимо значення TF9_2.txt:")
    for row in f:
        print(repr(row.rstrip("\n")))

