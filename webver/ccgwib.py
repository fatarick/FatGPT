from pywebio import start_server
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_html, put_scrollable, put_markdown, popup
from pywebio.session import set_env

import openai

# Initialize the natural language processing model
openai.api_key = "#OPENAI API CODE"
model_engine = "text-davinci-003"

def chat():
    popup("Big update of interface", put_text('Big update of UI. From flask to pywebio.'))
    set_env(title="FatDisGPT")
    put_markdown('## FatDisGPT')
    put_text('The Devoloper is recomending after 2 answers restart the page, because 3+ on one session will be call bugs.')
    conversation = []
    while True:
        # Get the user's request
        prompt = input(placeholder="Enter your message here", type=TEXT)
        
        # Get the answer
        answer = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )["choices"][0]["text"]

        # Add the user's request and chatbot's answer to the conversation
        conversation.append(f'You: {prompt}')
        conversation.append(f'Chatbot: {answer}')

        # Display the conversation
        conversation_html = '<br>'.join(conversation)
        put_scrollable(put_html(conversation_html), height=200, keep_bottom=True)

if __name__ == '__main__':
    start_server(chat, debug=True, port=8080, cdn=False, auto_open_webbrowser=False)
