# 🌍 Text Translator App

A simple full-stack web application that allows users to input text, select a target language (English or Swahili), and receive a translated result.

---

## 🚀 Overview

This project was built as part of a take-home assignment with a focus on:

- Simplicity and clarity
- Clean architecture
- Separation of concerns
- Practical technology choices

The application uses a server-rendered approach with a lightweight backend API to keep the system easy to understand, run, and extend.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + Vanilla JavaScript
- **Data Storage:** None (in-memory dictionary)

---

## ✨ Features

- Enter text to translate
- Select target language (English ⇄ Swahili)
- View translated output instantly
- Handles unknown words gracefully
- Clean and minimal UI

---

## 📂 Project Structure

```text
translator_app/
├── views.py                 # Handles HTTP requests/responses
├── urls.py                  # Route definitions
├── services/
│   ├── translator.py        # Translation logic
├── templates/
│   └── index.html           # Frontend UI
├── static/                  # (Optional) JS/CSS files
```

---

## 📡 API Endpoint

### `POST http://localhost:8000/api/v1/translate-text`

#### Request
```json
{
  "text": "father",
  "source_lang": "en",
  "target_lang": "sw"
}
```

#### Response
```json
{
  "translated": "baba"
}
```

The app currently uses a predeined dictionary:
```json
EN_TO_SW = {
        "hello" : "jambo",
        "tea" : "chai",
        "car" : "gari", 
        "fish" : "samaki",
        "thanks" : "asante",
        "please" : "tafadhali",
        "father" : "baba",
        "mother" : "mama",
        "shark" : "papa",
        "tree" : "mti"
    }
```

Swahili conversion uses the same dictionary with values reversed(swahili becomes the key)

---

## 🧠 Design Decisions

### 1. Django Templates over React

Although I have experience with React and Tailwind, I chose Django templates because:

- The application has low interactivity requirements
- It avoids the overhead of managing a separate frontend and API
- It keeps the system simple and easy to run

This aligns with the goal of prioritizing clarity over complexity.

---

### 2. Separation of Concerns

- `views.py` → Handles HTTP logic only  
- `services/translator.py` → Contains translation logic and dictionary 

This structure improves maintainability and makes the logic reusable and testable.

---

### 3. Translation Strategy

- Uses a predefined in-memory dictionary  
- Supports English ⇄ Swahili translations  
- Unknown words are returned unchanged to ensure consistent behavior  

---

### 4. No Database

A database was intentionally avoided as per the requirements.  
An in-memory dictionary is sufficient for the scope of this task.

---

## ⚖️ Trade-offs & Alternatives

### Alternative: React Frontend

For a more interactive or production-scale application, I would:

- Use React for the frontend  
- Consume the backend via REST APIs  
- Introduce state management for UI interactions  

However, this was intentionally avoided to maintain simplicity.

---

## 🧪 Running the Project

### 1. Clone the repository
```bash
git clone https://github.com/Silas-Labs/chichwa-translate.git
cd translate
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🎯 Future Improvements

- Expand dictionary coverage.
- Add exact translation including punctuations.
- Add automatic language detection  
- Improve UI feedback (loading states, validation)  

---

## 📌 Final Note

This project prioritizes **clarity, simplicity, and maintainability** over unnecessary complexity.

The goal was not just to meet the requirements, but to demonstrate thoughtful engineering decisions.
