# Find set where the element exists
def find_parent(parent, element):
    # If the element is not root
    if parent[element] != element:
        return find_parent(parent, parent[element])
    # else
    return element

# Union two sets where each element exists
def union_parent(parent, element1, element2):
    element1_root = find_parent(parent, element1)
    element2_root = find_parent(parent, element2)

    if element1_root < element2_root:
        parent[element2_root] = element1_root
    else:
        parent[element1_root] = element2_root

# Get input: verticies, edges
V, E = map(int, input().split())
parent = [0] * (V + 1)
# Initialize parent table
for i in range(1, V + 1):
    parent[i] = i

# Union
for i in range(E):
    element1, element2 = map(int, input().split())
    union_parent(parent, element1, element2)

# Set that each element exists in
print("Set that each element exists in: ", end="")
for v in range(1, V + 1):
    print(find_parent(parent, v), end=' ')
print()

# Print parent table
print(f"Parent table:", end="")
for v in range(1, V + 1):
    print(parent[v], end=' ')



