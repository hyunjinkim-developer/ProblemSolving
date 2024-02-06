"""
Problem:
https://www.testdome.com/questions/python/merge-names/94855
"""

def unique_names(names1, names2):
    names = set()
    for name in names1:
      names.add(name)
    for name in names2:
      names.add(name)
    return list(names)

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia