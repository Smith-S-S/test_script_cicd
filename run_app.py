from pyngrok import ngrok
import subprocess
import os

# Set your ngrok auth token
ngrok.set_auth_token("2qpRWeIX1oVNuMoOacmRWFXqyXQ_2ZDQHJLZK5FyB8iXJpe23")

# Start ngrok tunnel on port 8501 (Streamlit's default port)
public_url = ngrok.connect(port=8501)

# Print the public URL so it can be captured by the GitHub Actions workflow
print(f"Public URL: {public_url}")

# Run Streamlit app
subprocess.run(["streamlit", "run", "dashboard.py"])
