from design_patterns.command.command_abc import AbsCommand
from design_patterns.command.oder_command_abc import AbsOrderCommand


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = description = 'ShipOrder'

    def execute(self):
        raise NotImplementedError