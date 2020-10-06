import os


# Task 2

def all_files(root: str):
    files_lst = []
    for path, _, files in os.walk(root):
        for f in files:
            files_lst.append(os.path.join(path, f))
    return files_lst


fl = all_files(r"C:\Users\Данила\files")

print("Task #2")
for f in fl:
    print(f)