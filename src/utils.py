import psutil
import time


def get_system_info():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage("/")
    uptime = time.time() - psutil.boot_time()
    network_info = psutil.net_io_counters()
    processes = len(psutil.pids())
    swap_info = psutil.swap_memory()

    return (
        cpu_percent,
        memory_info,
        disk_info,
        uptime,
        network_info,
        processes,
        swap_info,
    )
