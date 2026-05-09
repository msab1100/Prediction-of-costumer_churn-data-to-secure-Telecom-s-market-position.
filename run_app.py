#!/usr/bin/env python
"""
Customer Churn Analysis Web App Launcher
Launches the Streamlit dashboard in your default browser
"""

import subprocess
import sys
import webbrowser
import time
import os

def main():
    print("=" * 50)
    print("Customer Churn Analysis Web Dashboard")
    print("=" * 50)
    print()
    
    # Check if streamlit is installed
    try:
        import streamlit
    except ImportError:
        print("[INFO] Installing Streamlit...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit", "-q"])
        print("[SUCCESS] Streamlit installed")
    
    print()
    print("[INFO] Starting Streamlit app...")
    print("[INFO] The app will open in your browser at: http://localhost:8501")
    print()
    print("Press Ctrl+C to stop the app")
    print()
    
    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        try:
            webbrowser.open('http://localhost:8501')
        except:
            pass
    
    import threading
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "app.py", "--logger.level=error"
        ])
    except KeyboardInterrupt:
        print("\n[INFO] App stopped")
        sys.exit(0)

if __name__ == "__main__":
    main()
