# CivicFlow — AI-Powered Government Appointment Scheduling & Queue Platform

> **"Skip the Queue. Get Government Services Smarter."**  
> *Official GovTech Digital Public Infrastructure Initiative*

CivicFlow is an enterprise-grade, citizen-centric digital platform designed to eliminate long queues, overcrowding at service centers, unpredictable waiting times, missed appointments, and repeat visits due to missing documents.

---

## 🌟 Key Features

### 1. Python AI Agents Core
- **SlotAllocationAgent (`backend/agents/slot_agent.py`)**:
  - Analyzes historical booking density, active counter throughput, and service duration.
  - Dynamically tags time slots (`Low crowd`, `Moderate crowd`, `High demand`).
  - Recommends the optimal slot with transparent AI reasoning (e.g. *35% lower crowd than the 11:00 AM rush*).
- **DocVerificationAgent (`backend/agents/doc_agent.py`)**:
  - Automatically generates personalized document checklists for each service.
  - Simulates instant AI OCR validation, confidence scoring (e.g., 97.5%), name alignment, and validity checks to prevent repeat visits.
- **QueueOptimizationAgent (`backend/agents/queue_agent.py`)**:
  - Manages real-time queue tokens (`CF-42`), active counters, and dynamic Estimated Waiting Time (EWT).
  - Triggers *"Your turn is coming soon"* notifications and audio chimes when a citizen is next in line.
- **MultiChannelReminderAgent (`backend/agents/reminder_agent.py`)**:
  - Generates scheduled reminder timelines (7 days, 3 days, 24 hours, 2 hours before).
  - Powers templates across SMS, WhatsApp, Email, and an **interactive USSD (`*123#`) telecom gateway** for feature phones.
- **CivicFlowAssistantAgent (`backend/agents/assistant_agent.py`)**:
  - Floating conversational assistant ("Ask CivicFlow") capable of answering document rules, looking up appointments, recommending low-crowd slots, and assisting with rescheduling.

### 2. Citizen Experience
- **Modern GovTech Aesthetic**: Clean, trustworthy, blue/white visual identity, rounded cards, and smooth micro-interactions.
- **Citizen Dashboard**: Upcoming appointments with live QR pass, recent history, completed services, and 1-click actions.
- **Government Services Directory**: Searchable catalogue covering Revenue (Income, Caste, Domicile), Municipal (Birth, Death), Transport (Driving License), and Social Welfare (Pension).
- **Smart 4-Step Booking Wizard**: Fast scheduling with AI slot recommendation and document readiness confirmation.
- **Live Queue Tracking**: Displays queue position, people ahead, estimated wait minutes, serving token, and interactive simulation controls.
- **Multi-Channel Drawer**: Live previews of WhatsApp, SMS, and an **interactive USSD (`*123#`) phone simulator** with functional dial pad.
- **Accessibility & Inclusion**:
  - Font scaling (`A-`, `A`, `A+`)
  - Dark / Light mode toggle
  - Bilingual switcher: **English | हिन्दी**

### 3. Government Staff & Administrator Command Center
- **Live KPIs**: Today's Appointments, Active Check-ins, Current Queue, Average Wait Time, Center Utilization Rate.
- **Counter Operations**: Real-time counter status (Active/Paused), Call Next citizen token, and throughput tracking.
- **Export Reports**: Instant CSV download for municipal auditing.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ (Tested on Python 3.14)
- Web Browser (Chrome, Edge, Firefox, Safari)

### Run with Python
```powershell
cd d:\civicflow
python main.py
```
Or double-click `run.bat`.

The application will launch at: **`http://localhost:8000`**

---

## 🧪 Testing the User Flows

1. **Flow 1: Booking an Appointment**
   - Click **"Book an Appointment"** from the landing page.
   - Step 1: Select *Income Certificate*.
   - Step 2: Select *Central Civic Kendra*.
   - Step 3: View intelligent slots. Notice the **CivicFlow AI Insight** recommending `10:30 AM` with the `Low crowd` badge.
   - Step 4: Verify your document checklist (Aadhaar Card, Address Proof, Income Proof, Photo).
   - Step 5: Click **Confirm**. Your unique `CF-XXXXXX` appointment ID and scannable QR Pass are generated!

2. **Flow 2: Arriving at the Center & Live Queue**
   - On the Citizen Dashboard, click **"Arrive & Check In"**.
   - Your status updates to `Checked In`, token `#CF-42` is issued, and you are placed at Position `#7` with an 18-minute wait.
   - Go to **"Live Queue"** in the navigation. Click **"Call Next Token"** to simulate counter officers processing citizens.
   - When 1 person is ahead, the system triggers the green banner *"Your Turn is Coming Soon"* and plays an audio chime!

3. **Flow 3: AI Assistant ("Ask CivicFlow")**
   - Click the floating **"Ask CivicFlow"** button at the bottom-right.
   - Click any suggestion chip (e.g. *"Docs for Income Cert?"* or *"When is my appointment?"*).
   - The Python AI agent parses your intent and provides contextual guidance with clickable direct action links.

4. **Flow 4: USSD (*123#) Feature Phone Simulator**
   - Go to **"Multi-Channel (USSD)"** in the top navigation.
   - On the vintage LCD screen, enter `2` and click **"Send Reply"** to look up your active appointment via telecommunication protocol.
   - Enter `0` to return to the root menu, or test `1` to book and `5` for nearest centers.

5. **Flow 5: Administrator Portal**
   - Use the top role dropdown to switch to **"Counter Officer (Amit Roy)"** or **"Admin Director (Dr. Sunita Rao)"**.
   - Review live metrics, pause or activate counters, and call the next citizen in line.
   - Click **"Export Report (CSV)"** to download the municipal operations summary.
