from transformers import pipeline

# This test classify the sentence as positive or negative. The test use, by default, the 
# distilbert-base-uncased-finetuned-sst-2-english model. The output is a JSON like this:
#
# [{'label': 'POSITIVE', 'score': 0.9598047137260437}]
classifier = pipeline("sentiment-analysis")
result=classifier("I've been waiting for a HuggingFace course my whole life.")
print(result)

# This test classify two sentences as positive or negative. The test use, by default, the
# distilbert-base-uncased-finetuned-sst-2-english model. The output is a JSON like this:
#
# [{'label': 'POSITIVE', 'score': 0.9598047137260437}, {'label': 'NEGATIVE', 'score': 0.9994558691978455}]
result=classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)
print(result)
