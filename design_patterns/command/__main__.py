from design_patterns.command.create_oder import CreateOrder
from design_patterns.command.update_order import UpdateOrder
from design_patterns.command.ship_order import ShipOrder
from design_patterns.command.no_command import NoCommand
import sys


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print('Usage: python -m Command CommandName [arguments]')
    print('Commands:')
    for command in commands.values():
        print(f'    {command.description}')


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()

if len(sys.argv) < 2:
    print_usage(commands)
    exit()

# Find and execute the command
command = parse_command(commands, sys.argv[1:])
command.execute()