from scanner_orchestrator.zap_runner import run_zap_scan
from scanner_orchestrator.nikto_runner import run_nikto_scan
from parser.combine_reports import combine_reports
import json
from ai_module.generator import get_ai_summary

target = input("Enter the target URL (e.g., http://testphp.vulnweb.com): ").strip()

print(f"[+] Scanning {target} ...\n")
run_zap_scan(target)
run_nikto_scan(target)


combined = combine_reports("reports/zap_report.json", "reports/nikto_report.txt")
print(f"[+] Total vulnerabilities found: {len(combined)}")

with open("reports/combined_report.json", "w") as f:
    json.dump(combined, f, indent=2)
    print("[+] Combined report saved to: reports/combined_report.json")

print("🧠 Generating AI-based summary...")
summary = get_ai_summary(combined)

with open("reports/ai_summary.txt", "w") as f:
    f.write(summary)
    print("[+] AI summary saved to: reports/ai_summary.txt")
