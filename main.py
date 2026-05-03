import requests
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
]

def ping_all():
    for url in URLS:
        try:
            r = requests.get(url, timeout=60, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            print(f"✓ {url} — {r.status_code}")
        except Exception as e:
            print(f"✗ {url} — {e}")

while True:
    ping_all()
    print("--- Sleeping 30 minutes ---")
    time.sleep(1800)
