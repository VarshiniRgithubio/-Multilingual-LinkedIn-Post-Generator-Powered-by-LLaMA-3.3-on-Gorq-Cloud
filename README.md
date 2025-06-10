# 🌐 Multilingual LinkedIn Post Generator | Powered by LLaMA 3.3 on Gorq Cloud

As a student passionate about AI and real-world applications of large language models, I built a LinkedIn post generator that creates **professional, multilingual captions** using **LLaMA 3.3 hosted on Gorq Cloud**.

---

## 🌟 Features

- ✅ Scraped and collected sample LinkedIn post data
- ✅ Stored and processed data in `.json` format using Python
- ✅ Custom prompts to guide the model’s responses
- ✅ Integrated with **LLaMA 3.3** via **Gorq Cloud** – all generation happens in the cloud
- ✅ Supports **few-shot learning** to match previous post tone, structure, and length
- ✅ Built a user-friendly **Streamlit** interface for easy use
- ✅ Users can select post **length, tone, and language**

---

## 🌍 Supported Languages

- English
- Hindi
- Kannada
- Telugu
- Korean
- Japanese

---

## 🧠 Real-World Applications

- 📌 Personal branding for global professionals
- 📌 Multilingual marketing content
- 📌 Cross-border hiring and HR posts
- 📌 Educational post sharing in regional languages
- 📌 DEI-focused communication
- 📌 Global networking and community building

---

## 🚀 Key Benefits

- 🔹 Cloud-based generation using **LLaMA 3.3**
- 🔹 Multilingual support for broader audience reach
- 🔹 Learns from past posts for consistent tone and style
- 🔹 Saves time via automation
- 🔹 Ideal for creators, marketers, recruiters, and educators

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Gorq Cloud (LLaMA 3.3)
- JSON for data storage
- Web scraping tools (e.g., BeautifulSoup, Requests)

---

## 🛠️ How to Run the Project Locally

### 🔽 Clone the Repository

```bash
git clone https://github.com/your-username/multilingual-linkedin-post-generator.git
cd multilingual-linkedin-post-generator
```
 ## Project Structure
multilingual-linkedin-post-generator/
│
├── app.py               # Streamlit interface
├── prompts.py           # Prompt generation logic
├── data/
│   └── sample_posts.json  # Sample LinkedIn posts (optional)
├── .env.example         # Environment variables template
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
---

## Environment Variables
GORQ_API_KEY=your_api_key_here
GORQ_ENDPOINT=https://api.gorq.cloud/llama-3.3/generate
---
#Install Dependencies
pip install -r requirements.txt

---
# Run the Streamlit App
streamlit run app.py






