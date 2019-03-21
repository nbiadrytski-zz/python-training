def maker(N):
    return lambda X: X + N


nested_lambda = maker(3)
print(nested_lambda(2))  # 5