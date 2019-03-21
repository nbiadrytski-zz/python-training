def maker(N):  # outer function that generates and returns a nested function, without calling it

    def action(X):
        return X + N
    return action


nested_func = maker(3)  # nested_func is actually action() returned by maker(); pass 3 to arg N
print(nested_func(2))  # pass 2 to X, N remembers 3: 2 + 3 = 5
print(nested_func(10))  # 13