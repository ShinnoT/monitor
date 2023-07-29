from rich.text import Text
from asciichartpy import plot


def get_cpu_chart(cpu_data):
    return Text(plot(list(cpu_data), {"height": 18}), style="cyan")
