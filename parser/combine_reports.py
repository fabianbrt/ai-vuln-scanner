from parser.zap_parser import parse_zap_report
from parser.nikto_parser import parse_nikto_report

def combine_reports(zap_path: str, nikto_path: str) -> list[dict]:
    zap_vulns = parse_zap_report(zap_path)
    nikto_vulns = parse_nikto_report(nikto_path)

    return zap_vulns + nikto_vulns
