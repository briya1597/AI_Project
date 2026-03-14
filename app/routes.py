from flask import Blueprint, request, jsonify, render_template
from .services.ai import generate_ai_response

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@main_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Server is running."})

@main_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "⚠ Please enter a valid message."})

    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    if user_message.lower() in greetings:
        return jsonify({"reply": "Hi there! Ready to explore the latest in tech?"})

    reply_text = generate_ai_response(user_message)
    return jsonify({"reply": reply_text})
