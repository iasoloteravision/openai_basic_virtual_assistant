import openai

openai.api_key = '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'


# Set your OpenAI API key


def generate_response(prompt):
    # Use the Openai API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7,
        n=1,
        stop=None)

    return response.choices[0].text.strip()
