from rich.table import Table


def get_system_table(metric, percent, total, used, name, color):
    table = Table(expand=True)

    table.add_column("Metric", justify="center", style=f"{color}", no_wrap=True)
    table.add_column("Value", justify="center", style=f"{color}", no_wrap=True)

    table.add_row(f"{name} Usage", f"{percent}%")
    table.add_row("Total", f"{total / (1024.0 ** 3):.2f} GB")
    table.add_row("Used", f"{used / (1024.0 ** 3):.2f} GB")
    table.add_row("Usage Percentage", f"{percent}%")

    return table


def get_uptime_table(uptime):
    table = Table(expand=True)
    table.add_column(
        "Uptime (in seconds)", style="purple", justify="center", no_wrap=True
    )
    table.add_row(f"{uptime:.2f}")
    return table


def get_network_table(network_info):
    table = Table(expand=True)
    table.add_column("Sent (GB)", style="red", justify="center", no_wrap=True)
    table.add_column("Received (GB)", style="red", justify="center", no_wrap=True)
    table.add_row(
        f"{network_info.bytes_sent / (1024.0 ** 3):.2f}",
        f"{network_info.bytes_recv / (1024.0 ** 3):.2f}",
    )
    return table


def get_processes_table(processes):
    table = Table(expand=True)
    table.add_column("Running processes", style="green", justify="center", no_wrap=True)
    table.add_row(f"{processes}")
    return table


def get_swap_table(swap_info):
    table = Table(expand=True)
    table.add_column("Total (GB)", style="yellow", justify="center", no_wrap=True)
    table.add_column("Used (GB)", style="yellow", justify="center", no_wrap=True)
    table.add_row(
        f"{swap_info.total / (1024.0 ** 3):.2f}",
        f"{swap_info.used / (1024.0 ** 3):.2f}",
    )
    return table
