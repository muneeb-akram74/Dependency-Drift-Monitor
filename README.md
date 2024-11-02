# Dependency Drift Monitor

## Overview

The **Dependency Drift Monitor** is a Python-based tool designed to detect and manage drift in infrastructure as code (IaC) using Terraform. Drift refers to the differences between the expected and actual states of your infrastructure, which can lead to discrepancies and potential issues. This tool helps you identify these differences and alert you via email, ensuring that your infrastructure remains in the desired state.

## Features

- Parses Terraform configuration files to extract module versions.
- Compares current versions with a predefined baseline.
- Detects any drift in the dependency versions.
- Saves drift reports to a SQLite database.
- Sends email alerts for detected drift, using SMTP.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Contributing](#contributing)

## Installation

To get started with the Dependency Drift Monitor, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/muneeb-akram74/Dependency-Drift-Monitor.git
   cd dependency-drift-monitor

2. **Set up a Python virtual environment (optional but recommended)**:
    python -m venv venv
    source venv/bin/activate # On Windows use venv\Scripts\activate (sometimes activate.bat or activate.ps1 works for windows)    

3. **Install dependencies**:
    pip install -r requirements.txt


## Usage

1. **Prepare your Terraform and baseline files**:
    -Create a Terraform configuration file (e.g., sample_file.tf) that contains your infrastructure code.
    -Create a baseline JSON file (e.g., baseline.json) that defines the expected versions of your modules.

2. **Run the Dependency Drift Monitor**: 
*Use the following command to execute the drift detection*:

python main.py --terraform-file /path/to/sample_file.tf --baseline-file /path/to/baseline.json --alert-method email --to-email your-email@example.com

Replace /path/to/sample_file.tf and /path/to/baseline.json with the actual paths to your files, and update your-email@example.com to the email address where you want to receive alerts.


## Configuration

To configure email alerts, you need to set the following environment variables:

- `SMTP_EMAIL`: Your email address used for sending alerts.
- `SMTP_PASSWORD`: The password for your email account (consider using an app password for security).
- `SMTP_PORT`: The SMTP port number (typically 587 for TLS).
- `SMTP_SERVER`: The SMTP server address (e.g., smtp.gmail.com for Gmail).


## Example of running in Docker

docker run --name drift-monitor-container -d \
  -v "C:\path\to\sample_file.tf:/app/sample_file.tf" \
  -v "C:\path\to\baseline.json:/app/baseline.json" \
  --env SMTP_EMAIL='your-email@example.com' \
  --env SMTP_PASSWORD='your-email-password' \
  --env SMTP_PORT='587' \
  --env SMTP_SERVER='smtp.gmail.com' \
  drift-monitor-image \
  python main.py \
  --terraform-file /app/sample_file.tf \
  --baseline-file /app/baseline.json \
  --alert-method email \
  --to-email your-email@example.com

## if you are using VS code powershell use

docker run --name drift-monitor-container -d `
  -v "C:\path\to\sample_file.tf:/app/sample_file.tf" `
  -v "C:\path\to\baseline.json:/app/baseline.json" `
  --env SMTP_EMAIL="your-email@example.com" `
  --env SMTP_PASSWORD="your-email-password" `
  --env SMTP_PORT="587" `
  --env SMTP_SERVER="smtp.gmail.com" `
  drift-monitor-image `
  python main.py `
  --terraform-file /app/sample_file.tf `
  --baseline-file /app/baseline.json `
  --alert-method email `
  --to-email "your-email@example.com"


## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Contributing

Contributions are welcome! If you'd like to contribute:

    -Please see the CONTRIBUTING.md file for guidelines on how to contribute to this project.

    -Please fork the repository and create a pull request. You can also submit issues for any bugs or feature requests.

    -For larger contributions, please consider discussing your changes before submitting a pull request to ensure they align with the project's goals.


## Code of Conduct

This project adheres to a CODE_OF_CONDUCT.md to ensure a welcoming environment for all contributors. Please review it to understand the expectations for participation.


## Contact

For any inquiries, please contact me at muneeburrehman0055@gmail.com.

---

Thank you for using Dependency Drift Monitor! Happy coding!

## Notes:
- Replace placeholders (like `yourusername`, `your-email@example.com`, and file paths) with actual information relevant to your project.
- Feel free to customize any sections further to match your project's specifics or your personal style!
