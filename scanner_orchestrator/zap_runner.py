import subprocess
import os

def run_zap_scan(target_url: str):
    reports_dir = os.path.abspath("reports")
    command = [
        "docker", "run", "--rm",
        "-v", f"{reports_dir}:/zap/wrk",
        "ghcr.io/zaproxy/zaproxy:latest",
        "zap-baseline.py",
         "-t", target_url,
        "-J", "zap_report.json",
        "-r", "zap_report.html"    
    ]

    print(f"[+] Scanning {target_url} ...\n")
    subprocess.run(command)
    print("\n[+] Scan complete. Check the 'reports/' folder.")
