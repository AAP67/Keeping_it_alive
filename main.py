# main.py
from playwright.sync_api import sync_playwright
import time

URLS = [
    "https://equity-research-ai-francium77.streamlit.app",
    "https://arkanex-tao.streamlit.app",
    "https://deal-sourcing-francium77.streamlit.app",
    "https://arkanex-ai-interviewer.streamlit.app",
    "https://arkanexconsultant.streamlit.app",
    "https://arkanecos.streamlit.app",
    "https://mortgage-servicing-orchestrator-8rdfdosxdktbseaxunynfc.streamlit.app",
    "https://mortgage-orchestrator-langgraph-bdritappvbz63jgscch4pmj.streamlit.app",
    "https://arkanexjyotish.streamlit.app",
    
    # add more as needed
]

def ping_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for url in URLS:
            try:
                page = browser.new_page()
                page.goto(url, wait_until="networkidle")
                time.sleep(10)
                page.close()
                print(f"✓ {url}")
            except Exception as e:
                print(f"✗ {url} — {e}")
        browser.close()

while True:
    ping_all()
    print(f"--- Sleeping 30 minutes ---")
    time.sleep(1800)
