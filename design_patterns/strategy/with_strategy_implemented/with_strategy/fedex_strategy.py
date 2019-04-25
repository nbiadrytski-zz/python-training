from design_patterns.strategy.with_strategy_implemented.with_strategy.strategy_abc import AbsStrategy


class FedExStrategy(AbsStrategy):

    def calculate(self, order):
        return 3.0
