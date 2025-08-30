import streamlit as st
from mega import Mega
import os
import uuid
from datetime import datetime
from PIL import ImageFont, Image, ImageDraw
import textwrap
import json
from langdetect import detect, DetectorFactory
from gtts import gTTS


# Find this script's folder and the font there 
this_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(this_dir, "NotoSansTelugu-VariableFont_wdth,wght.ttf")


# MEGA login
mega = Mega()
MEGA_EMAIL = os.getenv("MEGA_EMAIL")
MEGA_PASSWORD = os.getenv("MEGA_PASSWORD")
if not MEGA_EMAIL or not MEGA_PASSWORD:
    st.error("MEGA credentials missing. Set MEGA_EMAIL and MEGA_PASSWORD env vars.")
    st.stop()


m = mega.login(MEGA_EMAIL, MEGA_PASSWORD)


def upload_to_mega(filepath):
    file = m.upload(filepath)
    link = m.get_upload_link(file)
    return link

def get_font_for_language(lang_code, size=28):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception as e:
        st.warning(f"Could not load font: {e}")
        return ImageFont.load_default()

st.set_page_config(page_title="HeritageVerse", layout="centered")
st.title("HeritageVerse: Share Your Cultural Stories")
st.write("""
Welcome to HeritageVerse! Share your stories, proverbs, or memories in any language. We'll detect the language, generate audio, and create a beautiful story card for you.
""")

with st.form("story_form"):
    name = st.text_input("Your Name (optional)")
    story = st.text_area("Your Story or Proverb", height=150)
    submitted = st.form_submit_button("Submit")

if submitted and story.strip():
    st.info("Processing your submission...")
    DetectorFactory.seed = 0
    try:
        detected_lang = detect(story)
        from langcodes import Language
        try:
            full_lang = Language.get(detected_lang).display_name()
            st.success(f"Detected Language: {full_lang} ({detected_lang})")
        except:
            st.success(f"Detected Language: {detected_lang}")
    except Exception as e:
        st.error(f"Language detection failed: {e}")
        detected_lang = None

    tmp_dir = "/tmp" if os.path.exists("/tmp") else "."
    audio_filename = f"audio_{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join(tmp_dir, audio_filename)
    card_filename = f"card_{uuid.uuid4().hex}.png"
    card_path = os.path.join(tmp_dir, card_filename)

    # Text-to-speech
    try:
        tts = gTTS(text=story, lang=detected_lang if detected_lang else 'en')
        tts.save(audio_path)
        st.audio(audio_path, format="audio/mp3")
        with open(audio_path, "rb") as f:
            st.download_button("Download Audio", f, file_name=audio_filename)
        st.success("Audio generated!")
    except Exception as e:
        st.error(f"TTS generation failed: {e}")
        st.warning("This language might not be supported for audio yet.")

    # Story card image generation
    try:
        title_font = get_font_for_language(detected_lang if detected_lang else 'en', 36)
        body_font = get_font_for_language(detected_lang if detected_lang else 'en', 28)
        margin, offset = 40, 80
        max_width = 40
        lines = textwrap.wrap(story, width=max_width)
        line_heights = []
        for line in lines:
            bbox = body_font.getbbox(line)
            line_height = bbox[3] - bbox[1]
            line_heights.append(line_height + 8)
        total_text_height = sum(line_heights)
        base_height = 400
        extra_height = max(0, total_text_height - (base_height - offset - 60))
        img_height = base_height + extra_height
        img = Image.new('RGB', (800, img_height), color=(245, 235, 220))
        draw = ImageDraw.Draw(img)
        title_text = "Story Card"
        title_width = draw.textlength(title_text, font=title_font)
        draw.text(((800 - title_width) // 2, 20), title_text, font=title_font, fill=(90, 60, 30))
        y = offset
        for i, line in enumerate(lines):
            draw.text((margin, y), line, font=body_font, fill=(60, 40, 20))
            y += line_heights[i]
        if name.strip():
            draw.text((margin, y + 20), f"- {name.strip()}", font=body_font, fill=(100, 80, 60))
        draw.rectangle([(5, 5), (795, img_height - 5)], outline=(150, 120, 100), width=3)
        img.save(card_path)
        with open(card_path, "rb") as f:
            st.download_button("Download Story Card", f, file_name=card_filename)
        st.image(card_path, caption="Your Story Card", use_container_width=True)
        st.success("Story card generated!")
    except Exception as e:
        st.error(f"Story card generation failed: {e}")

    # Upload to MEGA
    try:
        audio_url = upload_to_mega(audio_path)
        card_url = upload_to_mega(card_path)
        st.success("Files uploaded to MEGA successfully!")
        st.audio(audio_url)
        st.markdown(f"[Download Audio]({audio_url})")
        st.image(card_url, caption="Your Story Card", use_container_width=True)
        st.markdown(f"[Download Card]({card_url})")
    except Exception as e:
        st.error(f"Failed to upload files to MEGA: {e}")
        audio_url = None
        card_url = None

    # Metadata
    metadata_file = "stories.json"
    local_metadata_path = os.path.join(tmp_dir, metadata_file)
    try:
        files = m.get_files()
        if metadata_file in files:
            m.download(metadata_file, dest_path=tmp_dir)
            with open(local_metadata_path, "r", encoding="utf-8") as f:
                stories = json.load(f)
        else:
            stories = []
    except Exception:
        stories = []
    try:
        data_entry = {
            "name": name.strip(),
            "story": story.strip(),
            "language": detected_lang if detected_lang else '',
            "timestamp": datetime.now().isoformat(),
            "audio_url": audio_url,
            "card_url": card_url
        }
        stories.append(data_entry)
        with open(local_metadata_path, "w", encoding="utf-8") as f:
            json.dump(stories, f, ensure_ascii=False, indent=2)
        m.upload(local_metadata_path)
        st.success("Metadata updated on MEGA!")
    except Exception as e:
        st.error(f"Failed to update metadata JSON on MEGA: {e}")

    # Cleanup
    try:
        if os.path.exists(audio_path): os.remove(audio_path)
        if os.path.exists(card_path): os.remove(card_path)
        if os.path.exists(local_metadata_path): os.remove(local_metadata_path)
    except: pass
