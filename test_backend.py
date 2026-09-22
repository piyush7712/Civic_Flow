import sys
import os

# Set utf-8 encoding for output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend.database import db
from backend.agents.slot_agent import SlotAllocationAgent
from backend.agents.doc_agent import DocVerificationAgent
from backend.agents.queue_agent import QueueOptimizationAgent
from backend.agents.reminder_agent import MultiChannelReminderAgent
from backend.agents.assistant_agent import CivicFlowAssistantAgent

def test_all():
    print("Testing CivicFlow Backend & AI Agents...")

    # 1. Database
    services = db.get_services()
    assert len(services) >= 7, f"Expected >= 7 services, got {len(services)}"
    print(f"[OK] Services catalog loaded: {len(services)} services")

    # 2. Slot Allocation Agent
    slot_agent = SlotAllocationAgent()
    slots = slot_agent.generate_slots_for_date("srv-income", "center-1", "Tomorrow", db.appointments, 5, 15)
    assert len(slots) > 0, "Slots generated"
    recommended = [s for s in slots if s.is_recommended]
    assert len(recommended) == 1, "Expected 1 recommended slot"
    print(f"[OK] SlotAllocationAgent: Recommended {recommended[0].time_str} with {recommended[0].crowd_level}")

    # 3. Document Verification Agent
    doc_agent = DocVerificationAgent()
    res = doc_agent.verify_document_upload("srv-income", "aadhaar", "Rahul Sharma", "aadhaar_card.pdf")
    assert res.status == "VERIFIED", "Document should be verified"
    assert res.confidence_score > 90.0, "Confidence should be high"
    print(f"[OK] DocVerificationAgent: {res.document_name} verified at {res.confidence_score}%")

    # 4. Queue Optimization Agent
    queue_agent = QueueOptimizationAgent()
    checkin = queue_agent.check_in_citizen("app-001", "Rahul Sharma", "Income Certificate", "center-1", 15)
    assert checkin["success"] is True, "Check-in should succeed"
    print(f"[OK] QueueOptimizationAgent: Token {checkin['token_number']} checked in at position #{checkin['queue_position']}")

    # 5. Multi-Channel Reminder Agent
    rem_agent = MultiChannelReminderAgent()
    ussd_res = rem_agent.process_ussd_session("citizen-1", "*123#")
    assert "CivicFlow" in ussd_res["display"], "USSD menu displayed"
    print("[OK] MultiChannelReminderAgent: USSD *123# gateway initialized")

    # 6. Conversational Assistant Agent
    asst_agent = CivicFlowAssistantAgent()
    ans = asst_agent.answer_query("Which documents do I need for an income certificate?", "citizen-1", "Rahul Sharma", db.appointments, services, db.get_centers())
    assert "Aadhaar Card" in ans["text"], "Expected Aadhaar Card in answer"
    print("[OK] CivicFlowAssistantAgent: Natural language query answered successfully")

    print("\nALL BACKEND & AI AGENT TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_all()
