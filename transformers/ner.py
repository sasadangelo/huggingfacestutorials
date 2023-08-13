from transformers import pipeline

# Named entity recognition (NER) is a task where the model has to find which parts of the input text correspond to entities such as persons, 
# locations, or organizations. Here the model correctly identified that Sylvain is a person (PER), Hugging Face an organization (ORG), and 
# Brooklyn a location (LOC).
#
# We pass the option grouped_entities=True in the pipeline creation function to tell the pipeline to regroup together the parts of the 
# sentence that correspond to the same entity: here the model correctly grouped “Hugging” and “Face” as a single organization, even though 
# the name consists of multiple words.
ner = pipeline("ner", grouped_entities=True)
result=ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(result)
