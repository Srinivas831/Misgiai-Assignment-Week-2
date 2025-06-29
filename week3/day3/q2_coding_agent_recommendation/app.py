# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import recommend_agents
from agents_data import agents

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    task = data.get("task", "")

    if not task:
        return jsonify({"error": "Task description is required."}), 400

    results = recommend_agents(task)
    return jsonify({
        "task": task,
        "recommendations": results,
        "total_agents": len(agents)
    })

@app.route("/agents", methods=["GET"])
def get_agents():
    """Get all available agents information"""
    return jsonify({"agents": agents})

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "AI Coding Agent Recommendation System API",
        "endpoints": ["/recommend", "/agents"]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
