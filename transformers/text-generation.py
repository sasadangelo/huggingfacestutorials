from transformers import pipeline

# you can also choose a particular model from the Hub to use in a pipeline for a specific task — say, text generation. 
# Let’s try the distilgpt2 model!

generator = pipeline("text-generation", model="distilgpt2")
result = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(result)
