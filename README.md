> # Del56

Hello, we're back with an exciting IP connection monitoring tool. This code monitors all incoming connections to your server and displays real-time information about who is connecting, including their geographical location.

> ## Prerequisites:

- Install Python on your system
- Install the required libraries after Python installation
- Run the code and it will automatically start monitoring
- A log file will be created where you can view all connection details

> ## Installation Steps:

```bash
# Install required libraries
pip install requests psutil
```

> ## Usage:

After running the code, the monitor will automatically start tracking all incoming connections to your server. The tool will display:

- Real-time connection attempts
- Geographical location (country/city) of each connection
- Local and remote port information
- Timestamp of each connection

> ## Features:

- **Real-time Connection Monitoring**: Tracks all established connections
- **Geographical Identification**: Shows country and city for each IP
- **Automatic Logging**: Saves all connection data to a log file
- **Multi-port Support**: Monitors connections on all ports
- **Live Display**: Shows connections in real-time with detailed information

The tool will continuously monitor your server connections and provide comprehensive logs of all incoming traffic for security analysis and monitoring purposes.
