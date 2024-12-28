from pyngrok import ngrok
import subprocess

# Set your ngrok auth token
ngrok.set_auth_token("2qpRWeIX1oVNuMoOacmRWFXqyXQ_2ZDQHJLZK5FyB8iXJpe23")

# Start ngrok tunnel on port 8501 (Streamlit's default port)
public_url = ngrok.connect("8501", "http")  # Correct configuration for ngrok

# Print the public URL only
print(public_url)

# Run Streamlit app
subprocess.run(["streamlit", "run", "dashboard.py"])
