import subprocess
import os

def run_nikto_scan(target_url: str):
    reports_dir = os.path.abspath("reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, "nikto_report.txt")

    command = [
        "nikto",
        "-h", target_url,
        "-o", report_path,
        "-Format", "txt"
    ]

    print(f"[+] Running Nikto scan (local) on {target_url} ...")
    subprocess.run(command)
    print(f"[+] Nikto scan complete. Report saved to: {report_path}")
