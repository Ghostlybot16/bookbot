# 📚 BookBot - Text Analysis Tool

BookBot is a Python-based text analysis tool that reads a book (or any `.txt` file) and generates a clean report<br> 
with word couts, character counts, lexical diversity, and the most frequent words.

It currently supports **two analysis pipelines**:
- **Regex Tokenizer** (baseline approach).
- **NLP-powered pipeline with spaCy** (lemmatization + stopword removal + optional POS filtering)



---

## ✨ Features

- ✅ Word count (total, unique)
- ✅ Word diversity ratio
- ✅ Top 10 most common words (Regex vs NLP-enhanced)
- ✅ Lexical diversity comparison:
    - Regex-tokenized version
    - spaCy (lemmas, with and without stopwords)
- ✅ Handles punctuation, numbers, and different dash/quote characters robustly
- ✅
- 🚧 (Planned) FastAPI backend for serving analysis results
- 🚧 (Planned) Docker support for easy deployment
- 🚧 (Planned) Word cloud visualization


---


## 📂 Project Structure

<pre>
bookbot/
|--- main.py                     # Entry point: generates reports
|--- stats.py                    # Regex-based pipeline
|--- nlp_stats.py                # spaCy-based pipeline
|--- books/                      # Place your .txt books here
|      | --- frankenstein.txt
|
|--- .gitignore
|--- requirements.txt
|--- README.md
|--- venv/

</pre>

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/Ghostlybot16/bookbot.git
cd bookbot
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv               
source venv/bin/activate           # Linux / macOS
venv\Scripts\activate              # Windows Powershell
```

### 3. Install dependencies
```bash
pip install -r requirements.txt    # Install dependencies
```

### 4. Run BookBot
```bash
cd bookbot
python3 main.py books/frankenstein.txt
```

---


## 📦 Requirements
- Python 3.10+
- spaCy (```en_core_web_sm``` model)
- Standard libraries: ```collections```, ```re```, ```sys```


---

## 🛠 Future Enhancements
- Add **FastAPI REST API** to expose analysis endpoints
- Add **Dockerfile** for containerization & cloud deployment
- Add word cloud visualization
- Add **unit tests + GitHub Actions** for CI/CD