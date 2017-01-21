# https://github.com/jsvine/markovify
import markovify

# Get raw text as string.
with open("Facebook Data/messages.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence().capitalize())