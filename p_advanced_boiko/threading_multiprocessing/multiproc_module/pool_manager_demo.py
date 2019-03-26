from multiprocessing import Pool, Manager


def factorial(N, dictionary):
    fact = 1
    for i in range(1, N+1):
        fact = fact * i
    dictionary[N] = fact  # store result in dict


if __name__ == '__main__':
    p = Pool(5)
    d = Manager().dict()
    for N in range(1, 1000, 10):
        p.apply_async(factorial, (N, d))

    p.close()
    p.join()

    for k, v in sorted(d.items()):
        print(k, v)