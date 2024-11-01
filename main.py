from parse_tf import parse_terraform, get_versions_from_terraform
from compare_baseline import load_baseline, compare_versions
from alert_manager import send_email_alert
from report_manager import create_drift_table, save_drift_report
from config import terraform_file_path, baseline_file_path, smtp_email

def main(file_path, baseline_file, alert_method="email", to_email=None):
    # Parse the Terraform file for module versions
    data = parse_terraform(file_path)
    current_versions = get_versions_from_terraform(data)

    # Load baseline versions from JSON
    baseline = load_baseline(baseline_file)

    # Compare current versions to baseline for drift
    drift = compare_versions(current_versions, baseline)

    if drift:
        save_drift_report(drift)
        drift_details = "\n".join(f"{k}: Current {v['current']} vs Expected {v['expected']}" for k, v in drift.items())
        if alert_method == "email" and to_email:
            send_email_alert(drift_details, to_email)
        else:
            print("Email alert method selected but no recipient email provided.")
    else:
        print("No drift detected.")


if __name__ == "__main__":
    # Initialize the drift report table if it hasn't been created
    create_drift_table()  
    # Run main function with specified parameters
    main(terraform_file_path, baseline_file_path, alert_method="email", to_email=smtp_email)
