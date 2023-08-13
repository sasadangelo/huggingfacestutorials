from transformers import pipeline

# We’ll start by tackling a more challenging task where we need to classify texts that haven’t been labelled. 
# This is a common scenario in real-world projects because annotating text is usually time-consuming and 
# requires domain expertise. For this use case, the zero-shot-classification pipeline is very powerful: it 
# allows you to specify which labels to use for the classification, so you don’t have to rely on the labels of 
# the pretrained model.

classifier = pipeline("zero-shot-classification")
result=classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
print(result)
