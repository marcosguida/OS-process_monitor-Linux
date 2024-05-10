<h1 align="center" style="font-weight: bold;">OS process monitor 💻</h1>
<h1 align="center" style="font-weight: bold;">
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
</h1>

Python script that aims to monitor running processes on a Linux operating system and alert for those that exceed certain CPU and memory usage limits.

## Behavior 

The script uses the `psutil` library, which provides an interface to retrieve operating system information, including information about running processes, CPU usage, and memory usage.

When the script is executed, it iterates over all running processes and checks the CPU and memory usage of each one. If the CPU or memory usage of a process exceeds the defined limits, the script displays information about that process, including its name, CPU usage, and memory usage.

## Requirements

- Python
- `psutil` library

## Installation

1. Install Python 3 and pip:

```
sudo apt install python3 python3-pip
```

2. Install the `psutil` library:

```
pip install psutil
```

## Usage

1. Download the script and save it with a `.py` extension (e.g., `monitorar_processos.py`).
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script:

```
python3 monitorar_processos.py
```

The script will start monitoring running processes on the system.

## Contributions

This script was developed by me.

*Open for contributions*

## License 

License under [MIT](https://opensource.org/license/mit)
