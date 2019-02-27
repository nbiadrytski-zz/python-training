from dive_into_p3.pluralize_nouns.plurals import build_match_and_apply_functions


class LazyRules:

    rules_filename = 'rules.txt'  # class var

    def __init__(self):
        self.pattern_file = open(self.rules_filename)
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        func = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(func)
        return func


rules = LazyRules()
for n in rules:
    print(n)
