# 🗣️ Voice_Activated_AI_Chatbot

## 📘 Introduction

The **Voice Activated AI Chatbot** is a Python-based desktop application that interacts with the user using natural voice commands. It can answer questions using Wikipedia, open websites, report the time, take voice notes, set reminders, and more all through voice interaction. It also includes a background scheduler to trigger time-based reminders.

---

## 🎯 Objectives

- 🎙️ Capture and process voice input using the microphone.  
- 🧠 Answer factual queries via **Wikipedia** integration.  
- 🌐 Open websites like **Google** and **YouTube**.  
- ⏰ Speak the current time.  
- 📝 Take and read voice notes.  
- 🔔 Set scheduled **reminders** using voice commands.  
- 💬 Respond with intelligent replies using **text-to-speech**.  
- 🔄 Support commands like **shutdown**, **restart**, and **exit**.

---

## 🧰 Technologies Used

- **Language**: Python  
- **Libraries**:  
  - `speechrecognition` – Converts spoken language into text  
  - `pyttsx3` – Text-to-speech conversion  
  - `wikipedia` – Retrieves search results  
  - `webbrowser` – Opens web pages  
  - `schedule` – Time-based task scheduling  
  - `datetime`, `os`, `threading`, `time` – Standard Python modules  

---

## 🧠 Features Breakdown

### 🗣️ Voice Command Input
- Uses the microphone to capture audio.
- Converts speech to text via Google's Speech Recognition API.

### 🧾 Text-to-Speech Responses
- Uses `pyttsx3` to speak back information in real-time.

### 🔍 Wikipedia Search
- Searches and summarizes queries from Wikipedia.

### 🌐 Web Browsing
- Opens **Google** or **YouTube**.
- Performs Google searches for custom queries.

### 🕒 Time Queries
- Reports the current system time.

### 📝 Notes & Reminders
- Takes spoken notes and saves them to a local text file.
- Reads back all saved notes.
- Sets daily time-based **reminders** (e.g., "Remind me to call John at 17:30").

### ⏰ Reminder Scheduler
- Uses the `schedule` library running in a **background thread**.
- Alerts the user with reminders at the scheduled time using voice output.

### 🛑 System Commands
- Can **shutdown** or **restart** the system.
- Handles polite greetings and exit commands.

---

## 🔧 Setup Instructions

### ⚙️ Prerequisites

- Python **3.8+**
- Working **microphone**
- Internet connection (for Google Speech Recognition API)

### 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/adnan-saif/Voice_Activated_AI_Chatbot.git
cd Voice_Activated_AI_Chatbot

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the assistant
python assistant.py
