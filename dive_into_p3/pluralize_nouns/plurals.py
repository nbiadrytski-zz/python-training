import re


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)
    return matches_rule, apply_rule


def rules(rules_filename):  # generator which generates matches_rule and apply_rule funcs
    with open(rules_filename) as pattern_file:
        for line in pattern_file:
            # split on any whitespace (tabs or spaces, no matter).
            # split on whitespace 3 times
            pattern, search, replace = line.split(None, 3)
            # pass pattern, search, and replace to the build_match_and_apply_functions() function
            # which returns a tuple of functions
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError(f'No matching rule for {noun}')


print(plural('test'))