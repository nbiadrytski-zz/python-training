from design_patterns.observer.before_observer.kpi_data import KPI_Data


for kpi in KPI_Data:
    if kpi.name == 'open':
        print(f'Current open tickets: {kpi.value}')
    elif kpi.name == 'new':
        print(f'New tickets in last hour: {kpi.value}')
    elif kpi.name == 'closed':
        print(f'Tickets closed in last hour: {kpi.value}')