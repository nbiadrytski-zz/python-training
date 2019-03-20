import code  # Utilities needed to emulate Python's interactive interpreter

interpretator = code.InteractiveConsole()

try:
    while True:
        code_string = interpretator.raw_input('>>>')
        interpretator.push(code_string)
except EOFError:
    print('\nExiting\n')