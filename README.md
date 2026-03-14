# TrackTech AI - Global Innovation Tracker

TrackTech is a cutting-edge AI assistant specialized in tracking and reporting the latest innovations in science and technology. It provides expert-level updates on breakthroughs in AI, space exploration, robotics, quantum computing, biotech, and more.

## 🚀 Features

- **Dual AI Providers**: Uses Google's **Gemini 1.5 Flash** as the primary provider with a seamless fallback to **Groq (Llama 3.1)** to ensure 100% uptime.
- **Real-time Insights**: Delivers concise and accurate updates on research papers, patents, and product launches.
- **Secure Configuration**: Fully integrated `.env` system to protect sensitive API credentials.
- **Deployment Ready**: Configured for industry-standard deployment on **Vercel** and **Render**.

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **AI Integration**: Google Generative AI SDK, Groq SDK
- **Environment Management**: `python-dotenv`
- **Deployment**: Vercel Serverless Functions

## 💻 Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AI_Project.git
   cd AI_Project
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`.
   - Add your API keys:
     ```env
     GEMINI_API_KEY=your_key_here
     GROQ_API_KEY=your_key_here
     ```

5. **Run the Application**:
   ```bash
   python index.py
   ```

## 🌐 Deployment

### Deploy to Vercel (Recommended)

1. Push your code to GitHub.
2. Link your repository to Vercel.
3. **Crucial**: Add `GEMINI_API_KEY` and `GROQ_API_KEY` in the Vercel **Environment Variables** settings.
4. Vercel will automatically build and deploy the app using the included `vercel.json` and `requirements.txt`.

## 🔒 Security

- Sensitive keys are never committed to the repository thanks to a robust `.gitignore` configuration.
- Always use the `.env.example` template when sharing or documenting the project.
