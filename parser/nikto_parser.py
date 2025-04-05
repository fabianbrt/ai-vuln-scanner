import os
import re

def parse_nikto_report(report_path: str) -> list[dict]:
    vulnerabilities = []

    if not os.path.exists(report_path):
        print(f"[!] Nikto report not found at {report_path}")
        return vulnerabilities

    with open(report_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("+") and not line.startswith("++") and line != "+":
                # Curăță liniile de prefixul "+" și spațiile
                content = line[1:].strip()
                
                # Optional: caută URL în linie
                urls = re.findall(r"http[s]?://[^\s]+", content)

                vulnerabilities.append({
                    "source": "Nikto",
                    "message": content,
                    "urls": urls if urls else None
                })

    return vulnerabilities
