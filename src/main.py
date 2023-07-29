import time
from collections import deque

from utils import get_system_info
from tables import (
    get_system_table,
    get_swap_table,
    get_network_table,
    get_processes_table,
    get_uptime_table,
)
from charts import get_cpu_chart
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel

console = Console()
layout = Layout()
cpu_data = deque(maxlen=60)

# Define layout structure
layout.split_column(Layout(name="upper"), Layout(name="middle"), Layout(name="lower"))

layout["upper"].split_row(
    Layout(name="cpu"), Layout(name="memory"), Layout(name="disk")
)

layout["middle"].split_row(
    Layout(name="uptime"),
    Layout(name="network"),
    Layout(name="processes"),
    Layout(name="swap"),
)


def main():
    with Live(
        console=console, refresh_per_second=2, screen=True
    ) as live:  # use screen=True for full screen
        while True:
            (
                cpu_percent,
                memory_info,
                disk_info,
                uptime,
                network_info,
                processes,
                swap_info,
            ) = get_system_info()

            cpu_data.append(cpu_percent)

            cpu_table = get_system_table(
                cpu_percent,
                cpu_percent,
                memory_info.total,
                memory_info.used,
                "CPU",
                "cyan",
            )
            memory_table = get_system_table(
                memory_info.percent,
                memory_info.percent,
                memory_info.total,
                memory_info.used,
                "Memory",
                "green",
            )
            disk_table = get_system_table(
                disk_info.percent,
                disk_info.percent,
                disk_info.total,
                disk_info.used,
                "Disk",
                "yellow",
            )
            uptime_table = get_uptime_table(uptime)
            network_table = get_network_table(network_info)
            processes_table = get_processes_table(processes)
            swap_table = get_swap_table(swap_info)

            # Define layout structure
            layout.split_column(
                Layout(name="upper"),
                Layout(name="middle"),
                Layout(
                    Panel(
                        get_cpu_chart(cpu_data),
                        title="CPU Usage Graph",
                        style="bold cyan",
                    ),
                    ratio=2,
                ),
            )

            layout["upper"].split_row(
                Layout(Panel(cpu_table, title="CPU Usage", style="bold cyan")),
                Layout(Panel(memory_table, title="Memory Usage", style="bold green")),
                Layout(Panel(disk_table, title="Disk Usage", style="bold yellow")),
            )

            layout["middle"].split_row(
                Layout(Panel(uptime_table, title="Uptime", style="bold purple")),
                Layout(Panel(network_table, title="Network Usage", style="bold red")),
                Layout(Panel(processes_table, title="Processes", style="bold green")),
                Layout(Panel(swap_table, title="Saw Memory", style="bold yellow")),
            )

            live.update(layout)

            time.sleep(1)


if __name__ == "__main__":
    main()
