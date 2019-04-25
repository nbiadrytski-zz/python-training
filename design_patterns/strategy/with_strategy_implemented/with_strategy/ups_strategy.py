from design_patterns.strategy.with_strategy_implemented.with_strategy.strategy_abc import AbsStrategy


class UPSStrategy(AbsStrategy):

    def calculate(self, order):
        return 4.00
