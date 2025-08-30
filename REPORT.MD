# 📑 Project Report – HeritageVerse  

## 1.1 Team Information  
- **Project Name:** HeritageVerse  
- **Team Members:**  
  - Rama Krishna Bootla
  - Tanniru Hari Sri Shanmukha Sai
  - Sai Pranay Reddy Damarapalli
  - Phaneendra Gullapelli 
  - Hridya Sharma
- **Repository:** [Swecha_Telangana_Project](https://github.com/Hari-Sri-T/Swecha_Telangana_Project)  

---

## 1.2 Application Overview  
**HeritageVerse** is a community-driven platform that allows users to share **stories, proverbs, and cultural memories** in any language.  

The **MVP (Minimum Viable Product)** focused on:  
- Accepting text input from users (stories/proverbs).  
- Detecting the language automatically.  
- Generating **audio output** using gTTS.  
- Creating a **visually appealing story card** with the submitted text.  
- Storing and sharing both audio and cards securely via **MEGA cloud integration**.  

This MVP ensures inclusivity by working for **multiple languages** and offering an **offline-first design** suitable for low-bandwidth users.  

---

## 1.3 AI Integration Details  
- **Language Detection:** Implemented using `langdetect` to automatically identify the input language.  
- **Text-to-Speech (TTS):** Integrated via **Google Text-to-Speech (gTTS)** for generating high-quality audio in the detected language.  
- **Smart Font Rendering:** Uses a universal font (`NotoSansTelugu`) with PIL to correctly render regional scripts.  
- **Insights:** Although simple, these AI-powered components make HeritageVerse **language-agnostic**, giving it the ability to support cultural diversity at scale.  

---

## 1.4 Technical Architecture & Development  
- **Frontend:** Built with **Streamlit** for an interactive and simple UI.  
- **Backend:**  
  - Handles language detection (`langdetect`).  
  - Generates audio (`gTTS`).  
  - Produces story cards (`PIL`).  
- **Storage & Sharing:** Files (audio, cards, metadata JSON) uploaded to **MEGA cloud storage** for accessibility.  
- **Metadata Tracking:** Stories stored in `stories.json`, maintaining name, text, language, timestamp, and file URLs.  
- **Deployment:** Dockerized for consistent execution and hosted on **Hugging Face Spaces**.  

**Simplified Architecture Diagram:**  
```
User → Streamlit UI → Language Detection → [TTS + Story Card Generation]  
        ↓                                               ↓  
       Metadata JSON ← Upload to MEGA Cloud → Audio + Story Cards  
```

---

## 1.5 User Testing & Feedback (Week 2)  
### Methodology  
- **Recruitment:** Initial testers recruited from peers, student volunteers, and Swecha community members.  
- **Tasks Given:**  
  - Submit short stories or proverbs in native languages.  
  - Test app on **low-bandwidth internet**.  
  - Download and share story cards/audio.  
- **Feedback Collection:** Gathered via informal interviews, Google Forms, and GitHub Issues.  

### Insights  
- UI was intuitive, but testers requested **faster processing**.  
- Some languages produced poor-quality audio (gTTS limitations).  
- Users liked the **aesthetic story cards** and ability to share them.  
- Requests came for **voice input** and **mobile-first design**.  

### Iterations Implemented  
- Optimized card generation for faster rendering.  
- Improved error handling for unsupported languages in gTTS.  
- Simplified download process for audio/cards.  

---

## 1.6 Project Lifecycle & Roadmap  

### A. Week 1: Rapid Development Sprint  
- Set up GitHub repo & Streamlit app.  
- Built MVP with language detection, TTS, and story card generation.  
- Integrated MEGA cloud storage for persistence.  
- Deployed initial app to Hugging Face Spaces.  

**Key Deliverable:**  
A working MVP deployed publicly with core features and offline-first design.  

---

### B. Week 2: Beta Testing & Iteration Cycle  
**Methodology:**  
- Peer testers from college + Swecha volunteers.  
- Tasks: enter multilingual inputs, download story cards/audio, test on mobile + low-bandwidth.  
- Feedback logged via Google Forms and GitHub Issues.  

**Insights & Iterations:**  
- **Issue:** gTTS audio failed for certain regional languages.  
  - **Fix:** Added fallback handling.  
- **Issue:** Large text wrapping in story cards.  
  - **Fix:** Dynamic resizing + wrapping with PIL.  
- **Issue:** MEGA upload delays.  
  - **Fix:** Improved temporary storage and error retries.  

---

### C. Weeks 3–4: User Acquisition & Corpus Growth Campaign  
**Target Audience & Channels:**  
- Students in Telangana (especially rural areas).  
- Local cultural clubs and WhatsApp groups.  
- Swecha community networks.  
*Justification:* Targeting early adopters who value preserving cultural heritage.  

**Growth Strategy & Messaging:**  
- **Message:** *“Preserve your culture. Share your story. Leave a legacy with HeritageVerse.”*  
- **Promotion:**  
  - WhatsApp/Telegram campaigns.  
  - Social media posts with sample story cards.  
  - Small demo sessions in student groups.  
- **Examples:** Posters + digital flyers (to be included in repo).  

**Execution & Results:**  
- Conducted outreach in 2–3 local student communities.  
- Encouraged direct sharing of links + demo usage.  
- Promoted on WhatsApp study groups and Telegram channels.  

**Metrics:**  
- Unique users acquired: ~50–70 (est.)  
- Stories contributed (corpus units): ~100+ entries  
- Feedback: Positive response to cultural preservation theme, with suggestions for **mobile app + voice input**.  

---

### D. Post-Internship Vision & Sustainability Plan  
**Major Future Features:**  
- Voice input support.  
- Mobile-first Progressive Web App (PWA).  
- Expanding fonts and TTS support for underrepresented languages.  

**Community Building:**  
- Engage Swecha volunteers and student clubs as ambassadors.  
- Create a **Telegram/WhatsApp group** for contributors.  

**Scaling Data Collection:**  
- Crowdsourcing stories via campaigns.  
- Gamification (badges/leaderboards for top contributors).  
- Partnerships with local cultural organizations.  

**Sustainability:**  
- Maintain open-source repo on GitHub.  
- Continue hosting via Hugging Face/Render.  
- Long-term: integrate into Swecha’s digital culture initiatives.  
