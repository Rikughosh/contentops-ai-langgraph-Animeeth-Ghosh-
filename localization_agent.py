from openai import OpenAI
client = OpenAI()

def localization_agent(text, language):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Translate to {language}: {text}"}]
    )
    return res.choices[0].message.content
