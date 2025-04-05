# ai_module/generator.py

import os
from together import Together
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key)

def get_ai_summary(vulnerabilities):
    summaries = []
    for vuln in vulnerabilities:
        print(f"🔄 Sending prompt for: {vuln.get('name') or vuln.get('title', 'Unknown vulnerability')}")
        prompt = f"""
You are a cybersecurity expert. Explain this web vulnerability and provide a remediation plan.

Name: {vuln.get('name') or vuln.get('title')}
Severity: {vuln.get('severity') or vuln.get('risk')}
URL: {vuln.get('url')}
Description: {vuln.get('description')}

Format your output as:
1. 🔍 Explanation
2. 🛠️ Remediation steps
"""
      
        try:
            response = client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.1",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            summaries.append({
                "vulnerability": vuln,
                "ai_summary": response.choices[0].message.content
            })
        except Exception as e:
            print(f"❌ Error for {vuln['name']}: {e}")
            summaries.append({
                "vulnerability": vuln,
                "ai_summary": "Error generating summary."
            })

    return summaries
