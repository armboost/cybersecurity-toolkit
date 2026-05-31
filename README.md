# cybersecurity-toolkit

A comprehensive automation toolkit for cybersecurity operations, featuring YARA scanning, OSINT data collection, port scanning, and website monitoring.

## Overview

This toolkit automates key security operations through scheduled workflows and push-triggered automation. It integrates multiple security tools and platforms to streamline threat detection, intelligence gathering, and network monitoring.

## Features

- **YARA Scanning**: Automated malware pattern detection and analysis
- **OSINT Lookup**: Intelligence gathering from open sources
- **Port Scanning**: Network port enumeration and service detection
- **Website Monitoring**: Uptime and availability checking
- **Automated Workflows**: Scheduled and push-triggered security operations

## Requirements

### System Dependencies

- Ubuntu/Linux environment
- YARA
- jq (JSON processor)
- Python 3.x

### Python Packages

```bash
pip install requests splunk-sdk
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/armboost/cybersecurity-toolkit.git
cd cybersecurity-toolkit
```

2. Install dependencies:
```bash
sudo apt update
sudo apt install yara jq -y
pip install requests splunk-sdk
```

## Usage

### Automated Workflow

The repository includes GitHub Actions workflows that run:

- **On Push**: Triggered when code is pushed to the `main` branch
- **Scheduled**: Daily at 3 AM UTC

### Manual Execution

Run individual security modules:

#### Python Scripts

```bash
# YARA Scan
python scripts/python/yara_scan.py

# OSINT Lookup
python scripts/python/osint_lookup.py

# Port Scanner
python scripts/python/port-scanner.py
```

#### Bash Scripts

```bash
# Check Website Availability
bash scripts/bash/check_website.sh

# Port Scanner
bash scripts/bash/port_scanner.sh
```

## Project Structure

```
cybersecurity-toolkit/
├── .github/
│   └── workflows/
│       └── cybersecurity-automation.yml
├── scripts/
│   ├── python/
│   │   ├── yara_scan.py
│   │   ├── osint_lookup.py
│   │   └── port-scanner.py
│   └── bash/
│       ├── check_website.sh
│       └── port_scanner.sh
├── README.md
└── ...
```

## Configuration

### Environment Variables

Ensure the following are configured for proper operation:

- **YARA Rules**: Ensure YARA rule definitions are in place
- **API Keys**: Set up any required API keys for OSINT sources
- **Target Hosts**: Configure target hosts for port scanning and website monitoring

## Workflow Details

### Cybersecurity Automation Workflow

- **Trigger**: Push to `main` and daily at 3 AM UTC
- **Platform**: Ubuntu Latest
- **Steps**:
  1. Checkout repository
  2. Install dependencies (YARA, jq, Python packages)
  3. Run YARA malware scanning
  4. Fetch OSINT data
  5. Execute port scanning

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

[Add your license information here]

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Repository ID**: 927753321
