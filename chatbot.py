import openai

openai.api_key = "your_api_key"

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("You: ")
    print("Bot:", chat(user_input))
