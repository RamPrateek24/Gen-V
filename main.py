import openai
import subprocess
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_manim_code(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a Python expert that writes Manim animation code."},
            {"role": "user", "content": f"Write a Manim script for: {prompt}"}
        ]
    )
    return response.choices[0].message.content.strip()

def save_script(code: str, filename: str = "scene.py") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

def render_video(filename: str = "scene.py") -> None:
    subprocess.run(["manim", "-pql", filename])

def main():
    user_prompt = input("Enter your animation idea: ")
    print("Generating script from prompt...")
    code = prompt_to_manim_code(user_prompt)
    save_script(code)
    print("Rendering animation...")
    render_video()
    print("Done")

if __name__ == "__main__":
    main()
