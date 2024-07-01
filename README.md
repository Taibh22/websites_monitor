# Website Monitoring Script

## Overview

This script monitors websites and reports their availability. It is designed for web administrators to detect issues on their sites by periodically checking the status and content of specified web pages.

## Features

- Reads a list of web pages (HTTP URLs) and their corresponding content requirements from an external configuration file.
- Periodically makes HTTP requests to each page.
- Verifies that the content received from the server matches the expected content specified in the configuration.
- Measures the time it took for the web server to complete the whole request.
- Logs the progress of the periodic checks, including URL status, content matching, and response times.
- Distinguishes between connection problems (e.g., website is down) and content problems (e.g., content requirements not match).

## Configuration

The script uses a configuration file (`config.ini`) to specify the checking period and URLs to monitor.

### `config.ini` 

```ini
[settings]
checking_period = 60

[urls]
url_1 = https://www.google.com,Google
url_2 = https://www.wikipedia.org,The Free Encyclopedia
url_3 = https://www.github.com,Built for developers
url_4 = https://www.python.org,Incorrect Text
url_5 = https://www.reddit.com,Dive into anything
url_6 = https://www.example.com,Example Domain
```
### Installation
1- Ensure you have Python installed on your system.
2- Install the required Python package using pip:

```
pip install requests configparser
```

### Usage
Create a config.ini file in the same directory as the script with your desired settings.
Run the script:
```
python websites_monitor.py
```

