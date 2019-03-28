X = 1


def nester():
    X = 2  # hides global
    print(X)  # local: 2

    class C:
        X = 3  # class C's local X hides global
        print(X)  # local: 3

        def method1(self):
            print(X)  # in enclosing def (not 3 in class!): 2
            print(self.X)  # class local: 3

        def method2(self):
            X = 4  # hides enclosing (nester, not class)
            print(X)  # local: 4
            self.X = 5  # hides class's X
            print(self.X)  # Located in instance: 5

    I = C()
    I.method1()
    I.method2()


print(X)  # global: 1
nester()  # 2, 3, 2, 3, 4, 5
