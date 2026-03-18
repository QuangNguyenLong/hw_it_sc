import random

file = open("declaration.txt", "r")

content = file.read()

total = len(content)

count_memoryless = {}
for c in content:
    count_memoryless[c] = 0

for c in content:
    count_memoryless[c] += 1

prob_memoryless = {k: c / total for k, c in count_memoryless.items()}

for k, v in prob_memoryless.items():
    print(f"P({repr(k)}): {v:.6f}")

count_first_order = {}

for i in range(total - 1):
    count_first_order[content[i], content[i + 1]] = 0

for i in range(total - 1):
    count_first_order[content[i], content[i + 1]] += 1


prob_first_order = {(i, j) : c / count_memoryless[i] for (i, j), c in count_first_order.items()}

for (i, j), v in prob_first_order.items():
    print(f"P({repr(j)}|{repr(i)}): {v:.6f}")

# generated_len = 1000

# current = random.choice(list(count_memoryless.keys()))
# generated = current

# for i in range(generated_len):
#     candidates = {c: prob_first_order[(current, c)]
#                   for (prev, c) in prob_first_order
#                   if prev == current}

#     if not candidates:
#         break

#     current = random.choices(list(candidates.keys()), weights=list(candidates.values()))[0]
#     generated += current

# print(generated)

file.close()