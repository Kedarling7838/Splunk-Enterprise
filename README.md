# AWS Splunk Log Monitoring with Python Application

## Project Overview

This project demonstrates centralized log monitoring using **Splunk Enterprise** deployed on **AWS EC2**. A Python application generates logs that are collected and indexed by Splunk for real-time monitoring and analysis.

The project showcases cloud deployment, log management, monitoring, and security concepts commonly used in enterprise environments.

---

## Architecture

```text
+-----------------------+
| Python Application    |
| (Generates Logs)      |
+----------+------------+
           |
           v
+-----------------------+
| Linux Log Files       |
| /var/log/             |
+----------+------------+
           |
           v
+-----------------------+
| Splunk Enterprise     |
| Port 8000 (Web UI)    |
| Port 9997 (Receiver)  |
+----------+------------+
           |
           v
+-----------------------+
| Search & Reporting    |
| Dashboards            |
| Log Analytics         |
+-----------------------+
```

---

## Technologies Used

* AWS EC2
* Amazon Linux
* Splunk Enterprise
* Python 3
* Linux Log Monitoring
* Git & GitHub

---

## Features

* Centralized log monitoring
* Real-time log collection
* Search and reporting
* Dashboard visualization
* Python application log generation
* Web-based monitoring interface
* Cloud deployment on AWS

---

## AWS Configuration

### EC2 Instance

* Operating System: Amazon Linux
* Instance Type: t3.medium
* Storage: 20 GB+

### Security Group Rules

| Port | Purpose              |
| ---- | -------------------- |
| 22   | SSH                  |
| 8000 | Splunk Web Interface |
| 8089 | Splunk Management    |
| 9997 | Splunk Data Receiver |

---

## Splunk Installation

### Download Splunk

```bash
wget -O splunk.rpm "https://download.splunk.com/products/splunk/releases/latest/linux/splunk.x86_64.rpm"
```

### Install Splunk

```bash
yum install splunk.rpm -y
```

### Start Splunk

```bash
cd /opt/splunk/bin
./splunk start --accept-license --answer-yes
```

### Enable Auto Start

```bash
./splunk enable boot-start
```

### Enable Receiver Port

```bash
./splunk enable listen 9997
```

---

## Python Log Generator

### app.py

```python
import logging
import time

logging.basicConfig(
    filename='/var/log/my_python_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

while True:
    logging.info("Application is running successfully")
    time.sleep(10)
```

Run:

```bash
python3 app.py
```

---

## Monitor Log File

```bash
./splunk add monitor /var/log/my_python_app.log
```

---

## Search Queries

View all logs:

```spl
index=*
```

View Python application logs:

```spl
source="/var/log/my_python_app.log"
```

Search application messages:

```spl
"Application is running successfully"
```

---

## Screenshots

Add screenshots inside the `screenshots` folder.

Examples:

* EC2 Instance
* Splunk Dashboard
* Search Results
* Python Log File
* Splunk Monitoring Configuration

---

## Project Structure

```text
aws-splunk-log-monitoring/
│
├── app.py
├── README.md
├── screenshots/
│   ├── dashboard.png
│   ├── search-results.png
│   ├── ec2-instance.png
│   └── python-logs.png
│
└── architecture.png
```

---

## Learning Outcomes

* AWS EC2 Deployment
* Splunk Enterprise Administration
* Log Collection and Monitoring
* Python Logging
* Linux Administration
* Cloud Security Configuration
* GitHub Project Management

---

## Future Enhancements

* Grafana Integration
* CloudWatch Integration
* Splunk Universal Forwarder
* Real-time Alerts
* Email Notifications
* Security Event Monitoring
* Multi-Server Log Aggregation

---

## Author

Kedarling Ashok Kanade

MCA Project – GM University, Davangere
