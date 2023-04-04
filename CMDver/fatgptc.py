import time
import openai

# Initialize the natural language processing model
openai.api_key = "#OPENAI API CODE"
model_engine = "text-davinci-003"

while True:
    # Get the user's request
    prompt = input("Write a request (or type 'exit' to quit): ")

    # If the user types 'exit', break out of the loop and end the program
    if prompt.lower() == "exit":
        break

    # Get the answer
    answer = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )["choices"][0]["text"]

    # Print the generated code on the console
    print(answer)

    # Pause for 1 second before executing the loop again
    time.sleep(1)
