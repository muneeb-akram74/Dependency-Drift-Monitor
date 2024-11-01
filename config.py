import os

smtp_email = os.getenv("SMTP_EMAIL")
smtp_password = os.getenv("SMTP_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")

terraform_file_path = os.getenv("TF_FILE_PATH")
baseline_file_path = os.getenv("BASELINE_FILE_PATH")