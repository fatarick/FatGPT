import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize the natural language processing model
openai.api_key = "#YOUR OPEN AI API CODE"
model_engine = "text-davinci-002"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's request
        prompt = request.form['request']

        # Get the answer
        answer = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )["choices"][0]["text"]

        # Display the answer in the chatbox
        return render_template('chat.html', prompt=prompt, answer=answer)
    else:
        # Display the chatbox input form
        return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
