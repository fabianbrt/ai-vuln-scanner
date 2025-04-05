import os
import openai
from dotenv import load_dotenv

# Încarcă cheia din .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Exemplu de vulnerabilitate (poate fi luat și din combined_report.json)
vuln = {
    "name": "Missing Anti-clickjacking Header",
    "severity": "Medium",
    "url": "http://testphp.vulnweb.com",
    "description": "The X-Frame-Options header is missing, making the site vulnerable to clickjacking attacks."
}

prompt = f"""
You are a cybersecurity expert. Explain this web vulnerability and provide a remediation plan.

Name: {vuln['name']}
Severity: {vuln['severity']}
URL: {vuln['url']}
Description: {vuln['description']}

Format your output as:
1. 🔍 Explanation
2. 🛠️ Remediation steps
"""

print("🔄 Sending to OpenAI...")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5
)

print("\n✅ Response from GPT-3.5-turbo:")
print(response.choices[0].message.content.strip())
