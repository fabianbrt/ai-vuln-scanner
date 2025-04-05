import json

def parse_zap_report(report_path: str):
    with open(report_path, 'r') as file:
        data = json.load(file)

    alerts = data.get("site", [])[0].get("alerts", [])

    if not alerts:
        print("⚠️  Nu au fost găsite vulnerabilități.")
        return []

    print(f"\n📋 Vulnerabilități găsite: {len(alerts)}\n")
    parsed = []
    for alert in alerts:
        name = alert.get("alert", "N/A")
        severity = alert.get("riskdesc", "N/A")
        description = alert.get("desc", "N/A")
        url = alert.get("instances", [{}])[0].get("uri", "N/A")

        print("─" * 50)
        print(f"🔐  {name}")
        print(f"🛑  Severitate: {severity}")
        print(f"🌐  URL afectat: {url}")
        print(f"📝  Descriere: {description.strip()[:200]}...")

        parsed.append({
            "source": "ZAP",
            "name": name,
            "severity": severity,
            "url": url,
            "description": description.strip()
        })

        return parsed
