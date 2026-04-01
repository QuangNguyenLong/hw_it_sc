def memoryless_model(filename):
    file = open(filename, 'r')
    content = file.read()

    prob_arr = [0] * 256 # 256 symbol

    for c in content:
        prob_arr[ord(c)] += 1

    file.close()

    return [cnt / len(content) for cnt in prob_arr]

def first_order_markov_model(filename):
    file = open(filename, 'r')
    content = file.read()

    transition_matrix = [[0] * 256 for _ in range(256)]

    for i in range(len(content) - 1):
        transition_matrix[ord(content[i])][ord(content[i + 1])] += 1

    for i in range(256):
        if sum(transition_matrix[i]) != 0:
            transition_matrix[i] = [e / sum(transition_matrix[i]) for e in transition_matrix[i]]

    file.close()
    return transition_matrix    
