from flask import Flask, request, jsonify, render_template
from llama_cpp import Llama
import os

# 1. Initialize Flask App
app = Flask(__name__)

# 2. Define the path to your GGUF model file
model_filename = "./indian-legal-model/outpt_file.gguf"
model_path = os.path.abspath(model_filename)

print(f"Loading GGUF model from: {model_path}")

# 3. Load the Model using llama-cpp-python
try:
    llm = Llama(
        model_path=model_path,
        n_gpu_layers=30,
        n_ctx=4096,  # The total memory for the prompt + response
        verbose=True,
    )
    print("GGUF Model loaded successfully!")

except Exception as e:
    print(f"ERROR: Failed to load GGUF model.")
    print(f"Python Error: {e}")
    exit()


# 4. Define the main route for the chat interface
@app.route("/")
def index():
    return render_template("index.html")


# 5. Define the API endpoint for the chatbot
@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        conversation_history = request.json["history"]

        # -- THIS IS THE FINAL MEMORY FIX --
        # We start with the base instruction
        prompt = """### Instruction:
You are Nyay AI, an esteemed legal scholar and expert assistant on Indian Law. You can remember previous parts of the conversation. Your purpose is to provide answers that are well-structured, coherent, and authoritative. Your name is Nyay AI. Maintain a formal and professional tone. Address the user by name if they have provided it in the conversation history.

"""
        # Build the conversation history into the prompt
        for message in conversation_history:
            if message['role'] == 'user':
                prompt += f"### User:\n{message['content']}\n\n"
            elif message['role'] == 'assistant':
                prompt += f"### Assistant:\n{message['content']}\n\n"

        # Add the final turn for the AI to respond to
        prompt += "### Assistant:\n"

        # ------------------------------------

        output = llm(
            prompt,
            max_tokens=2048,
            echo=False,
            temperature=0.7,
            top_p=0.9,
            repeat_penalty=1.1,
            stop=["### User:", "### Instruction:"],
        )

        assistant_response = output['choices'][0]['text'].strip()

        return jsonify({"response": assistant_response})

    except Exception as e:
        print(f"Error during model inference: {e}")
        return jsonify({"response": "Sorry, I encountered an error while generating a response."}), 500


# 6. Run the Flask App
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)