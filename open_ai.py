import openai

openai.api_key = "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"


# create a completion
completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="how to boost my cibil score",
  max_tokens=3000,
  temperature=0
)

# print the completion
print(completion["choices"][0]["text"])
