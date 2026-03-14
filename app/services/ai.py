import os
import traceback
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv is only required for local development
    pass

# Provider API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = (
    "You are TrackTech, a cutting-edge AI assistant specialized in tracking and reporting the latest innovations in science and technology from around the world. "
    "You provide expert-level, up-to-date information on breakthroughs in artificial intelligence, space exploration, robotics, quantum computing, biotech, clean energy, and emerging technologies.\n\n"
    "Your goal is to help users stay ahead of the curve by delivering concise, insightful, and accurate updates on technological advancements, research papers, patents, and product launches.\n\n"
    "If someone asks 'Who are you?' or 'Who built you?', always respond with: 'I am TrackTech, your AI guide to the forefront of global technological innovation.'\n\n"
    "If the user greets you (e.g., 'hi', 'hello', 'hey'), respond in an engaging manner such as: 'Hi there! Ready to explore the latest in tech?'\n\n"
    "Guidelines for Your Response:\n"
    "1. Be enthusiastic and informative.\n"
    "2. Highlight real-world applications and impacts of the technology.\n"
    "3. Reference reliable sources, scientific journals, or reputable tech news outlets.\n"
    "4. Avoid speculation—stick to verified developments.\n"
    "5. Categorize innovations when possible (e.g., AI, space, health tech).\n"
    "6. Use accessible language for general users but include technical depth when appropriate.\n"
)

def generate_ai_response(user_message: str) -> str:
    """Try Gemini first, fallback to Groq if Gemini fails."""
    
    # --- Try Gemini (Primary) ---
    try:
        import google.generativeai as genai
        print("💡 Attempting Gemini response...")
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        gemini_prompt = f"{SYSTEM_PROMPT}\nUser's Message: {user_message}\n\nTrackTech's Response:"
        response = model.generate_content(gemini_prompt)
        if hasattr(response, "text"):
            print("✅ Gemini handled the request.")
            return response.text
    except Exception as e:
        error_msg = f"⚠️ Gemini provider failed: {str(e)}"
        print(f"{error_msg}\n{traceback.format_exc()}")
        # Note: Avoid writing to local files on Vercel (read-only filesystem)

    # --- Try Groq (Fallback) ---
    try:
        from groq import Groq
        print("💡 Attempting Groq fallback...")
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set.")
            
        client = Groq(api_key=GROQ_API_KEY)
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            model="llama-3.1-8b-instant",
        )
        print("✅ Groq handled the request.")
        return chat_completion.choices[0].message.content
    except Exception as e:
        error_msg = f"❌ Groq also failed: {str(e)}"
        print(f"{error_msg}\n{traceback.format_exc()}")
        return f"⚠ AI Service Error: {str(e)}"
