import statistic as st

def least_probable_indices(p):
    i, j = -1, -1
    for k in range(len(p)):
        if i == -1 or p[k] < p[i]:
            j = i
            i = k
        elif j == -1 or p[k] < p[j]:
            j = k
    if i > j:
        i, j = j, i  # ensure i < j
    return i, j

def huffman(p : list):
    if len(p) == 1:
        return ["0"]
    if len(p) == 2:
        return ["0", "1"]

    i, j = least_probable_indices(p)

    p_ = p[:]
    p_[i] += p[j]
    p_.pop(j)

    C_ = huffman(p_)

    C = C_[:]
    C.insert(j, C_[i] + '1')
    C[i] = C_[i] + '0'
    
    return C

prob = st.memoryless_model("declaration.txt")

print(huffman(prob))
