# MetaScope

MetaScope is a Python application that maps out all devices connected to the local network and displays them graphically on Windows. It utilizes `Tkinter` for the GUI and performs network scanning using system utilities like `ping` and `arp`.

## Features

- Scans the local network to identify connected devices.
- Displays IP address, MAC address, and hostname of each device.
- Simple and interactive GUI using Tkinter.

## Requirements

- Python 3.x
- Tkinter (usually included with Python on Windows)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/metascope.git
```

Navigate to the project directory:

```bash
cd metascope
```

## Usage

Run the `metascope.py` file to start the application:

```bash
python metascope.py
```

Click the "Scan Network" button to begin scanning. The devices will be displayed in a table with their IP addresses, MAC addresses, and hostnames.

## Limitations

- This tool only works on Windows due to the use of Windows-specific command-line utilities.
- It assumes a standard /24 subnet, scanning IPs from `.1` to `.254`.
- The MAC address retrieval might be limited based on the network configuration and permissions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.