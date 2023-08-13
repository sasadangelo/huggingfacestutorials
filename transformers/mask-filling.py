from transformers import pipeline

# With this pipeline you’ll try the fill-mask. The idea of this task is to fill in the blanks in a given text.
# The top_k argument controls how many possibilities you want to be displayed. Note that here the model fills in the special <mask> word, 
# which is often referred to as a mask token. Other mask-filling models might have different mask tokens, so it’s always good to verify the 
# proper mask word when exploring other models. One way to check it is by looking at the mask word used in the widget.
unmasker = pipeline("fill-mask")
result = unmasker("This course will teach you all about <mask> models.", top_k=2)
print(result)
