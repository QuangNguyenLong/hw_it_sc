import math

def code(m, L):
    c = ''
    for _ in range(L):
        m *= 2
        c += str(int(m))
        m -= int(m)
    return c

def c_(x):
    return sum([math.pow(0.5, i + 1) 
                if x[i] == '1' 
                else 0 
                for i in range(len(x))])


def ideal_arithmetic_code(x : list, p0):
    n = len(x)
    l = 0
    h = 1
    for i in range(n):
        if x[i] == '0':
            h = l + p0 * (h - l)
        else:
            l = l + p0 * (h - l)

    m = (h + l) / 2
    L = math.ceil(-math.log2(h - l)) + 1

    return code(m, L)

def ideal_arithmetic_decode(code : str, p0, N):
    l = 0
    h = 1
    c_x = c_(code)

    x = ''

    for i in range(N):
        if c_x < l + p0 * (h - l) and c_x > l:
            x += '0'
            h = l + p0 * (h - l)
        else:
            x += '1'
            l = l + p0 * (h - l)
    return x

# filename = 'declaration.txt'

# with open(filename, 'rb') as f:
#     data = f.read()
# bits = ''.join(f'{byte:08b}' for byte in data)
# p0 = bits.count('0') / len(bits)

# N = 20

# raw = bits[:N]

N = 20
raw = '0' * N + '1'
p0 = 0.9

print(f'uncompressed:\t{raw}')

encoded = ideal_arithmetic_code(raw, p0)

print(f'compressed:\t{encoded}')

decoded = ideal_arithmetic_decode(encoded, p0, len(raw))

print(f'decompressed:\t{decoded}')