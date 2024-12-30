# Python URL Monitor with PyShark

Python URL Monitor with PyShark is a URL monitoring script that uses PyShark, a Python wrapper for Tshark, allowing python packet parsing using Wireshark dissectors. The script analyzes network packets and monitors HTTP/HTTPS requests in real time.

## Installation

To use this script, you need to have Python and PyShark installed. If not, you can install them using the commands below:

```bash
pip install pyshark
```

## Usage

To use this script, go to the directory where the script is located and run:

```bash
python url_monitor.py
```

By default, it monitors the 'eth0' interface. If you want to monitor a different interface, modify the 'interface' argument in the 'monitor_url' function call within the 'main' function.

```python
if __name__=='__main__':
    monitor_url('your_interface_here')
```

## License

This project is licensed under the terms of the MIT license.

## Contribution

Contributions are welcome! Please feel free to submit a Pull Request.