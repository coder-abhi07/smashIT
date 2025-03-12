# smashIT
www.smashit.onrender.com
nov 2025 www.qpaper.live

https://youtu.be/DDds_Mai3zo


# Smash-IT, A Question Paper Analyzer 

Analyze the past question papers and clusters the most frequently asked question and gives an idea about the important topic so students can prepare those topic firstly




## Acknowledgements
- [Django](https://www.djangoproject.com/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [OCR space API](https://ocr.space/)  
- [scikit-learn](https://scikit-learn.org/)  
- [NumPy](https://numpy.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Auth0](https://auth0.com/)  
## API Reference

### OCR space API for Text Extraction  

The **OCR.space API** allows you to extract text from images and PDFs using OCR (Optical Character Recognition).  

#### Free OCR API Endpoint (POST)  

POST https://api.ocr.space/parse/image  

This API supports both **HTTPS (SSL)** and **HTTP** connections.

#### GET OCR API Endpoint  

For simple OCR via URL, use:  

GET https://api.ocr.space/parse/imageurl?apikey=YOUR_API_KEY&url=IMAGE_URL  

Example:  

GET https://api.ocr.space/parse/imageurl?apikey=helloworld&url=https://dl.a9t9.com/ocr/solarcell.jpg  

To specify a language and request word coordinates:  

GET https://api.ocr.space/parse/imageurl?apikey=helloworld&url=https://dl.a9t9.com/ocr/solarcell.jpg&language=chs&isOverlayRequired=true  

**Note**: The **GET API** only supports image and PDF submissions via URL. File uploads (`file` parameter) or base64 strings (`base64image`) require **POST requests**.

---

### API Parameters  

| Parameter               | Type      | Description |
|-------------------------|----------|-------------|
| `apikey`               | String   | **Required.** Your API key. |
| `url` / `file` / `base64Image` | String   | **Required.** URL, file upload, or Base64-encoded image. |
| `language`             | String   | **Optional.** Language for OCR. Default is **English (eng)**. Other options: `ara`, `chs`, `spa`, `fre`, etc. |
| `isOverlayRequired`    | Boolean  | **Optional.** If `true`, returns text bounding box coordinates. Default is `false`. |
| `filetype`             | String   | **Optional.** Specify file type (`PDF`, `PNG`, `JPG`, etc.). |
| `detectOrientation`    | Boolean  | **Optional.** Auto-rotate image if `true`. Default is `false`. |
| `isCreateSearchablePdf` | Boolean  | **Optional.** Generate a searchable PDF. Default is `false`. |
| `isTable`             | Boolean  | **Optional.** Preserve table structure if `true`. Default is `false`. |
| `OCREngine`           | Integer  | **Optional.** Choose OCR engine: `1` (default) or `2`. |

---

### Select OCR Engine  

#### OCR Engine 1  
- Supports many languages  
- Fastest OCR  
- Best for large images  
- Multi-page TIFF support  

Use: `OCREngine=1`  

#### OCR Engine 2  
- Automatic language detection  
- Better recognition for special characters (e.g., `§$@€`)  
- Handles text on images, road signs, and CAPTCHAs  

Use: `OCREngine=2`  

Both engines return results in the same JSON format, so switching between them requires **no code changes**.

---

### Example JSON Response  

```json
{
  "ParsedResults": [
    {
      "TextOverlay": {
        "Lines": [],
        "HasOverlay": false
      },
      "TextOrientation": "0",
      "FileParseExitCode": 1,
      "ParsedText": "Hello World!",
      "ErrorMessage": "",
      "ErrorDetails": ""
    }
  ],
  "OCRExitCode": 1,
  "IsErroredOnProcessing": false,
  "ProcessingTimeInMilliseconds": "123",
  "SearchablePDFURL": ""
}

## Features

- Light/dark mode toggle
- Question Categorization (MCQ, Short, Long, Numerical, etc.)
- Fullscreen mode
- Cross platform





## Authors

- [@Abhishek Kumar](https://github.com/coder-abhi07)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## 🚀 About Me
nothing special 


## Feedback

If you have any feedback, please reach out to us at ak0188644@gmail.com


## Demo

[![Demo Video](https://img.youtube.com/vi/DDds_Mai3zo/maxresdefault.jpg)](https://youtu.be/DDds_Mai3zo)

## Appendix

Supported File Formats
PDF (.pdf)
Image Files: PNG, JPG, JPEG, PDF
Authentication
Uses API Key-based authentication for secure access.
Limitations
Free tier has a limited number of requests per day.
Maximum file size limit depends on subscription plan.
Troubleshooting
Ensure correct content-type when using URL-based OCR.
For improved accuracy, use high-resolution images.
If an image is rotated, enable detectOrientation=true in API parameters.
This appendix provides essential technical details to enhance the usability of the Question Paper Analyzer.
## Other Common Github Profile Sections
- 👋 Hi, I’m Abhishek Kumar
- 👀 Competitive Programmer
-  💻 Tech Inquisitive
- 👋 Good Learner

## Installation


### Prerequisites  
Ensure you have Python installed on your system. You may also need `pip` and `virtualenv` (optional but recommended).  

## Steps  

### 1. Clone the Repository  
```bash
git clone https://github.com/coder-abhi07/smashIT
cd smashIT
```
### 2. Create a Virtual Environment (optional)
```bash
python -m venv venv
### 1. Clone the Repository  
git clone https://github.com/coder-abhi07/smashIT
cd smashIT
```
### 2. Create a Virtual Environment (optional)
```bash
python -m venv venv
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


## Support

For support, email fake@fake.com or join our Slack channel.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

