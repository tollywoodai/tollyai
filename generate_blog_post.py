import openai
import datetime
import os

# Set your OpenAI API key here or load from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(prompt, tags):
    today = datetime.date.today().isoformat()
    print(f"Generating blog post for: {prompt}")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Tollywood movie blogger who writes insightful and engaging articles."},
            {"role": "user", "content": f"Write a blog post about: {prompt}"}
        ],
        temperature=0.8,
        max_tokens=1000
    )

    content = response['choices'][0]['message']['content']
    filename = f"blog_{today}_{prompt.replace(' ', '_')[:20]}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {prompt}\n\n")
        f.write(f"*Tags: {', '.join(tags)}*\n\n")
        f.write(content)

    print(f"Blog post saved to: {filename}")

# Example usage
if __name__ == "__main__":
    generate_blog_post("AI predictions for Pushpa 2 box office", ["AI", "Tollywood", "Pushpa"])