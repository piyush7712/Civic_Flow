import sys
import os
import webbrowser
import threading
import time

# Ensure proper encoding on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

import uvicorn

def open_browser():
    time.sleep(1.2)
    url = "http://localhost:8000"
    print(f"\n[CivicFlow] Opening web portal in default browser: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[CivicFlow] Please open {url} manually in your browser.")

def main():
    print("=" * 65)
    print("      CivicFlow - AI Government Appointment & Queue Platform     ")
    print("   'Skip the Queue. Get Government Services Smarter.'            ")
    print("=" * 65)
    print(" * AI Slot Allocation Agent: READY")
    print(" * AI Document Verification Agent: READY")
    print(" * AI Queue Optimization & Dynamic ETA Agent: READY")
    print(" * AI Multi-Channel Reminder Agent: READY")
    print(" * CivicFlow Conversational Assistant Agent: READY")
    print(" * Web Portal: http://localhost:8000")
    print("=" * 65)

    # Launch browser in a background thread
    threading.Thread(target=open_browser, daemon=True).start()

    # Start FastAPI server via Uvicorn
    uvicorn.run(
        "backend.app:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
