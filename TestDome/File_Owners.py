"""
Problem:
https://www.testdome.com/questions/python/file-owners/94848
"""

from collections import defaultdict

def group_by_owners(files):
    owner_file = defaultdict(list)
    for file, owner in files.items():
      owner_file[owner].append(file)
    return owner_file

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))