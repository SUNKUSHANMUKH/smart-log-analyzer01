import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def analyze_log(log_text: str) -> str:
    prompt = f"""
    You are a DevOps expert. Analyze this log entry and respond ONLY in JSON format:
    Log: {log_text}

    Return exactly this structure:
    {{
        "severity": "LOW or MEDIUM or HIGH or CRITICAL",
        "issue": "brief description of what went wrong",
        "action": "what the engineer should do",
        "alert_needed": true or false
    }}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # fast, good for most log analysis,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    log = "CRITICAL: Database connection timeout after 30s"
    print(analyze_log(log))
