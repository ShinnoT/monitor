# Monitor

<div align="center" style="margin-bottom:10px;margin-top:10px;">
    <img src="https://img.shields.io/badge/Made%20with-Python-green" />
    <img src="https://img.shields.io/badge/Powered%20by-psutil-purple" />
    <img src="https://img.shields.io/badge/Animated%20with-rich-orange" />
    <img src="https://img.shields.io/badge/Charts%20with-asciichartpy-blue" />
</div>

![Monitor-card](https://github.com/ShinnoT/portfoliov1/assets/26269548/24706a12-287f-4ef3-a7da-ed27bef3fd18)

---

Monitor is a dynamic command-line tool that visualizes complex system statistics for instant insights into your computer's performance.

This tool provides real-time monitoring of key performance metrics, including:

-   CPU usage
-   Memory usage
-   Disk usage
-   Network data
-   Running processes
-   System uptime
-   Swap memory usage

It also includes a live ASCII chart displaying CPU usage trends over the past 60 seconds.

## Installation

### Windows

1. Download `monitor.exe` from the `/downloads` directory.
2. Copy the file path of the directory containing `monitor.exe` and add it to your system's PATH:
    - Press `Win + X` and choose `System`.
    - Click on `Advanced system settings`.
    - In the `System Properties` window that appears, on the `Advanced` tab, click `Environment Variables...`.
    - In the `Environment Variables` window, scroll down in the `System variables` section and select the `Path` variable, then click `Edit...`.
    - In the `Edit Environment Variable` window, click `New` and then `Browse`.
    - Navigate to the location of `monitor.exe`, select it, and click `OK`.
3. Open the Command Prompt or PowerShell and type `monitor`.

### Linux/Mac

Coming soon...

## Usage

Simply type `monitor` in your command line to start the app.

## To run it locally

Git clone the repository and run the `main.py` file in `/src` directory after installing all requirements (sorry, still need to clear unused requirements... 😅).

```bash
git clone https://github.com/ShinnoT/monitor.git
cd monitor
pip install
```

## License

This project is licensed under the terms of the MIT license.
