from transformers import pipeline

# The question-answering pipeline answers questions using information from a 
# given context:
question_answerer = pipeline("question-answering")
result=question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
print(result)
