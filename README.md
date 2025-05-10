# Smash-IT: A Question Paper Analyzer


## Previous Version
[![Demo Video]]

**Website:** [SmashIT](https://www.smashit.onrender.com)  
**Upcoming Deployment:** [QPaper](https://www.qpaper.live) (November 2025)  

## 📌 Overview
Smash-IT is a **Question Paper Analyzer** that processes past question papers, identifies frequently asked questions, and clusters them into important topics to help students focus on key areas during their preparation.

## 🚀 Features
- **OCR-Based Text Extraction** (Powered by OCR.space API)
- **Question Categorization** (MCQs, Short Answer, Long Answer, Numerical, etc.)
- **Topic Clustering** using Machine Learning (Scikit-Learn, NumPy, Pandas)
- **User Authentication** via Auth0
- **Dark/Light Mode Toggle**
- **Cross-Platform Compatibility**
- **Admin Dashboard for Analysis**

## 🔗 Acknowledgements
- [Django](https://www.djangoproject.com/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [OCR.space API](https://ocr.space/)  
- [scikit-learn](https://scikit-learn.org/)  
- [NumPy](https://numpy.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Auth0](https://auth0.com/)  

## 📡 API Reference
### OCR.space API for Text Extraction

**OCR API Endpoint (POST)**  
```
POST https://api.ocr.space/parse/image
```

**OCR API via URL (GET)**  
```
GET https://api.ocr.space/parse/imageurl?apikey=YOUR_API_KEY&url=IMAGE_URL
```

#### API Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `apikey` | String | **Required.** Your API key. |
| `url` / `file` / `base64Image` | String | **Required.** URL, file upload, or Base64-encoded image. |
| `language` | String | **Optional.** Language for OCR (default: `eng`). Other options: `ara`, `chs`, `spa`, `fre`, etc. |
| `isOverlayRequired` | Boolean | **Optional.** If `true`, returns text bounding box coordinates. |
| `detectOrientation` | Boolean | **Optional.** Auto-rotate image if `true`. |

#### Example JSON Response
```json
{
  "ParsedResults": [
    {
      "ParsedText": "Hello World!",
      "ErrorMessage": "",
      "ErrorDetails": ""
    }
  ],
  "OCRExitCode": 1,
  "IsErroredOnProcessing": false
}
```

## 📷 Screenshots
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## 🛠️ Installation
### Prerequisites
- Python 3.x
- PostgreSQL
- Virtual Environment (recommended)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/coder-abhi07/smashIT
cd smashIT
```

### 2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Start the Server
```bash
python manage.py runserver
```

## 📦 Deployment
To deploy this project, run:
```bash
npm run deploy
```

## 🤝 Contributing
Contributions are always welcome! Please adhere to this project's `code of conduct`.

## 🏷️ License
[MIT License](https://choosealicense.com/licenses/mit/)

## 👨‍💻 Author
- [Abhishek Kumar](https://github.com/coder-abhi07)

## 📬 Feedback
For feedback or inquiries, reach out via email: **ak0188644@gmail.com**

## 📑 Appendix
- **Supported File Formats:** PDF, PNG, JPG, JPEG
- **Authentication:** API Key-based authentication
- **Limitations:** Free tier has request limits per day
- **Troubleshooting:** Ensure images are high-resolution and use `detectOrientation=true` if rotated

## 🌟 Other Info
- 👀 **Competitive Programmer**
- 💻 **Tech Enthusiast & Inquisitive Learner**
- 🚀 **Always Exploring New Technologies**

