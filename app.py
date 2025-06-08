from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Set your Gemini API Key
genai.configure(api_key="AIzaSyCtJtUx0QCUoig0PTq6pP-n5v1BVfZN17M")  # Replace with your actual API key

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    prompt = f"Answer this question strictly based on Automata Theory: {user_message}"

    try:
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"Error: {e}"

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
