import openai
import os
from data import communities, amenities, tags, views, property_types

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_autocomplete_suggestions(user_input):
    prompt = f"""
You are a smart real estate search assistant.

Here is the domain knowledge:
- Communities: {', '.join(communities)}
- Amenities: {', '.join(amenities)}
- Views: {', '.join(views)}
- Property Types: {', '.join(property_types)}
- Tags: {', '.join(tags)}

A user typed: "{user_input}"

Generate 5 autocomplete-style full property search phrases based on this data.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{{"role": "user", "content": prompt}}],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content.strip().split("\n")
