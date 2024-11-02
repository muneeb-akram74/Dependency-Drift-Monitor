import argparse
from parse_tf import parse_terraform, get_versions_from_terraform
from compare_baseline import load_baseline, compare_versions
from alert_manager import send_email_alert
from report_manager import initialize_database, save_drift_report

def main(terraform_file, baseline_file, alert_method="email", to_email=None):
    try:
        # Initialize the database
        initialize_database()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        return  # Exit if the database can't be initialized

    # Parse the Terraform file for module versions
    data = parse_terraform(terraform_file)
    print(f"Parsed Data: {data}")

    current_versions = get_versions_from_terraform(data)
    print(f"Current Versions from Terraform: {current_versions}")

    baseline = load_baseline(baseline_file)
    print(f"Baseline Loaded: {baseline}")

    drift = compare_versions(current_versions, baseline)
    print(f"Drift Detected: {drift}")

    if drift:
        try:
            save_drift_report(drift)
            print("Drift report saved successfully.")
        except Exception as e:
            print(f"Error saving drift report: {e}")
            return  # Exit if unable to save drift data

        drift_details = "\n".join(f"{k}: Current {v['current']} vs Expected {v['expected']}" for k, v in drift.items())
        if alert_method == "email" and to_email:
            send_email_alert(drift_details, to_email)
            print("Email alert sent.")
        else:
            print("Email alert method selected but no recipient email provided.")
    else:
        print("No drift detected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Terraform Drift Detection Tool")
    parser.add_argument("--terraform-file", required=True, help="Path to the Terraform file to check.")
    parser.add_argument("--baseline-file", required=True, help="Path to the baseline JSON file.")
    parser.add_argument("--alert-method", default="email", help="Alert method: 'email' or 'console'. Default is 'email'.")
    parser.add_argument("--to-email", help="Email address to send alerts to, if alert method is 'email'.")

    args = parser.parse_args()
    main(args.terraform_file, args.baseline_file, args.alert_method, args.to_email)
