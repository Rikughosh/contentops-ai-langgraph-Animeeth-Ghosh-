from openai import OpenAI
from dotenv import load_dotenv
import os
from memory.memory_store import load_memory, save_memory

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def drafting_agent(idea, content_type):
    history = load_memory()

    context = ""
    if history:
        context = f"Previous examples: {history[-2:]}"

    prompt = f"""
    {context}
    Create a {content_type}:
    {idea}
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = res.choices[0].message.content

    save_memory({
        "idea": idea,
        "content_type": content_type,
        "output": output
    })

    return output