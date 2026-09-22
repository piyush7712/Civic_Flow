import sys
import urllib.request
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def test_url(url, desc):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        content = resp.read()
        print(f"[OK] {desc} status {resp.status}, length {len(content)} bytes")
        return content

print("Verifying Live CivicFlow Web Server on http://127.0.0.1:8000 ...")

test_url("http://127.0.0.1:8000/", "Web Portal HTML Index")
test_url("http://127.0.0.1:8000/api/services", "Services API")
test_url("http://127.0.0.1:8000/api/slots?service_id=srv-income&center_id=center-1&date=Tomorrow", "AI Slot Engine API")
test_url("http://127.0.0.1:8000/api/admin/metrics", "Admin Metrics API")

# Test AI Assistant query
payload = json.dumps({"query": "Which documents do I need for an income certificate?"}).encode("utf-8")
req = urllib.request.Request("http://127.0.0.1:8000/api/ai/chat", data=payload, headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    print(f"[OK] AI Assistant response received: {res.get('action_label')}")

# Test USSD query
ussd_req = urllib.request.Request("http://127.0.0.1:8000/api/channels/ussd?input_str=%2A123%23", data=b"", headers={"Content-Type": "application/json"})
with urllib.request.urlopen(ussd_req) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    assert "CivicFlow" in res.get("display")
    print(f"[OK] USSD *123# gateway response verified")

print("\nALL LIVE WEB SERVER AND REST/AI ENDPOINTS VERIFIED SUCCESSFULLY!")
