import cProfile


def get_fibonacci(index):
    results = [0, 1]
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
        results.append(b)
    return results


profiler = cProfile.Profile()
profiler.enable()

print(get_fibonacci(40000))

profiler.disable()
profiler.print_stats()
