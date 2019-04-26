from design_patterns.command.command_abc import AbsCommand
from design_patterns.command.oder_command_abc import AbsOrderCommand


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = description = 'CreateOrder'

    def execute(self):
        raise NotImplementedError
