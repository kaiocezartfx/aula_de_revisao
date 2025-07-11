def fibonacci_3(n):
    seq = [0, 1, 1]
    for i in range(3, n):
        proximo = seq[-1] + seq[-2] + seq[-3]
        seq.append(proximo)
    return seq

print(fibonacci_3(10))