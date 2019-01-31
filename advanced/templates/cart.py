from string import Template


class MyTemplate(Template):

    delimiter = '#'  # override delimiter from $ to #


def template_demo_cart():
    cart = [dict(item='Coke', price=8, qty=2),
            dict(item='Cake', price=12, qty=3),
            dict(item='Fish', price=32, qty=4)]

    t = MyTemplate("#qty * #item = #price")
    total = 0

    print("Cart:")
    for data in cart:
        print(t.substitute(data))  # use safe_substitute to ignore key errors
        total += data['price']

    print("Total price: " + str(total))


if __name__ == "__main__":
    template_demo_cart()
