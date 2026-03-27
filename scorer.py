from openai import OpenAI
client = OpenAI()

def evaluate_content(text):
    prompt = f"Score content (0-10) for Clarity, Engagement, Compliance. Return JSON. Content: {text}"
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
