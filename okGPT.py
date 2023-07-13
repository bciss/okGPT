import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ""

# Main loop
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)
