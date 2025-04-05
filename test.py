from together import Together
import os
from dotenv import load_dotenv

load_dotenv()
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

prompt = """
You are a cybersecurity expert. Explain this web vulnerability and provide a remediation plan.

Name: Cross-Site Scripting (XSS)
Severity: High
URL: http://example.com/search
Description: Reflected XSS vulnerability via 'q' parameter.

Format your output as:
1. 🔍 Explanation
2. 🛠️ Remediation steps
"""

print("🔄 Sending to Together.ai...")
response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5
)

print("✅ Response:")
print(response.choices[0].message.content)
