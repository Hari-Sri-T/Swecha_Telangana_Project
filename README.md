---
sdk: docker
app\_file: src/app.py
---
--------------------------------

### Project running in Hugging Space Link: https://huggingface.co/spaces/Harisri/Viswamai-Project-HeritageVerse

#  HeritageVerse: Share Your Cultural Stories

Welcome to **HeritageVerse** — a place to share your cultural stories, proverbs, or memories in **any language**.
Our app detects the language, generates audio, and creates a beautiful story card — all saved **permanently** to MEGA cloud storage.


##  Features

* ** Multilingual** — Share stories in any language with **automatic language detection**.
* ** Audio Generation** — Converts your story to audio using **gTTS**.
* ** Stylish Story Cards** — Generates beautiful images with **Noto Sans Telugu** font.
* ** Persistent Storage** — All files (audio, cards, and metadata) are uploaded to **MEGA**.
* ** Download Everything** — Get your audio and cards instantly after creation.



## 🗂️ Project Structure

```
.
├── requirements.txt
├── Dockerfile
├── README.md
└── src/
    ├── streamlit_app.py
    └── NotoSansTelugu-VariableFont_wdth,wght.ttf
```

* All app code and the font reside in **`src/`**.
* Temporary files are handled in **`/tmp`** for deployment compatibility.

---

##  Deployment (Docker & Hugging Face Spaces)

This project uses **Docker** for universal deployment — locally and on **Hugging Face Spaces**.

### 1️ Prerequisites

* [Python 3.9+](https://www.python.org/)
* [Docker](https://www.docker.com/) for local builds
* A **free MEGA.nz** account (for persistent cloud storage)

---

### 2️ Environment Variables (Secrets)

Set these in your environment **or** in your Hugging Face Space Secrets:

| Variable        | Description                |
| --------------- | -------------------------- |
| `MEGA_EMAIL`    | Your MEGA account email    |
| `MEGA_PASSWORD` | Your MEGA account password |

> ⚠️ Never commit credentials to source control. Always use environment variables or CI/Space secrets.

---

### 3️ Local Docker Build & Run

**Build the container:**

```bash
docker build -t heritageverse .
```

**Run it** (replace with your MEGA credentials):

```bash
docker run -p 8501:8501 \
  -e MEGA_EMAIL=your@email.com \
  -e MEGA_PASSWORD=yourpassword \
  heritageverse
```

Then open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

### 4️ Deploy on Hugging Face Spaces

1. Create a new Space and **select `Docker`** as the SDK.
2. Push your repository to the Space (or link the repo from GitHub).
3. In the Space settings, add the secrets `MEGA_EMAIL` and `MEGA_PASSWORD`.
4. Verify that `app_file` is set to `src/streamlit_app.py` (the metadata block at the top of this README helps with that).

---

##  Font Configuration

* The file **`NotoSansTelugu-VariableFont_wdth,wght.ttf`** must be present in **`src/`**.
* The filename must match **exactly** (case-sensitive).
* Re-download if needed:
  [Noto Sans Telugu Variable Font — GitHub](https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTelugu/NotoSansTelugu-VariableFont_wdth,wght.ttf)

---

##  Requirements

Add the following to `requirements.txt` or your environment file:

```
streamlit
pillow
langdetect
langcodes
gtts
mega.py
```

> If you pin versions for reproducibility, list them here (e.g. `streamlit==1.21.0`).

---

##  Usage

1. Open the **HeritageVerse** app.
2. Enter your name *(optional)* and your cultural story, proverb, or memory.
3. Submit to **generate audio** (gTTS) and a **story card** (image with Noto Sans Telugu rendering).
4. Download your audio or card, or view previous submissions *(if implemented)*.

---

##  Troubleshooting

### **Font Not Loading**

* Ensure the font file exists at `src/NotoSansTelugu-VariableFont_wdth,wght.ttf` and is spelled exactly.

### **MEGA Errors**

* Confirm `MEGA_EMAIL` and `MEGA_PASSWORD` are set correctly as environment variables or Space secrets.
* Check that your MEGA account is active and not locked by login attempts.

### **Permissions or File Errors**

* The app writes temp files to `/tmp` — ensure the Docker container or Space allows writing to `/tmp` (usually allowed).

---

## Security Tips

* Do not log or print secrets in application logs.
* Use scoped/temporary credentials if possible.
* Consider rotating your MEGA password if it’s been committed anywhere.

---

##  License

MIT License

Font © Google (Noto Sans Telugu)

---

##  Contact / Issues

If you find bugs or want features, please open an issue or contact the maintainer (add your preferred contact method here).

> *Built for HeritageVerse, 2025 *
