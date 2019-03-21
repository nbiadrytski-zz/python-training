def tester(start):

    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start
    return nested


f = tester(0)
f('spam')  # spam 0
f('ham')  # ham 1
print(f.state)  # 2