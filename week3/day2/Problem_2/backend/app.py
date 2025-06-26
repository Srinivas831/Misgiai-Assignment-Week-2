# ✅ Import libraries
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ✅ Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ✅ Route for main page
@app.route("/", methods=["GET", "POST"])
def index():
    answer = None

    if request.method == "POST":
        # Get question from form
        question = request.form["question"]

        # Get uploaded image file
        image = request.files["image"]

        if image:
            # Read image content into bytes
            image_bytes = image.read()

            # Call OpenAI Vision model (GPT-4o)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": [
                        {"type": "text", "text": question},
                        {"type": "image_url", "image_url": {
                            "url": "data:image/jpeg;base64," + base64.b64encode(image_bytes).decode('utf-8')}
                         }
                    ]}
                ],
                # max_tokens=500
            )

            # Extract answer
            answer = response.choices[0].message.content

    # Render the HTML page with answer (if any)
    return render_template("index.html", answer=answer)


# ✅ API Route for React frontend
@app.route("/api/analyze", methods=["POST"])
def analyze_image():
    try:
        # Get question from request parameters or form data
        question = request.args.get('question') or request.form.get('question', 'What do you see in this image?')
        
        # Get image from form data
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
            
        image = request.files['image']
        
        if image.filename == '':
            return jsonify({"error": "No image selected"}), 400

        # Read image content into bytes
        image_bytes = image.read()
        
        # Encode image to base64
        base64_image = base64.b64encode(image_bytes).decode('utf-8')

        # Call OpenAI Vision model (GPT-4o)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"}
                     }
                ]}
            ],
            max_tokens=500
        )

        # Extract answer
        answer = response.choices[0].message.content
        
        return jsonify({
            "success": True,
            "answer": answer,
            "question": question
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)