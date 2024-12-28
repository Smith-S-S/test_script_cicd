from pyngrok import ngrok
import subprocess
import os

# Set your ngrok auth token
ngrok.set_auth_token("2qpRWeIX1oVNuMoOacmRWFXqyXQ_2ZDQHJLZK5FyB8iXJpe23")

# Start ngrok tunnel
public_url = ngrok.connect(port=8501)
print(f"Public URL: {public_url}")

# Run Streamlit
subprocess.run(["streamlit", "run", "dashboard.py"])
