def pytest_addoption(parser):  # Adding command-line options
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")

