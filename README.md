# Smash-IT, A Question Paper Analyzer

Analyze past question papers and cluster the most frequently asked questions to identify important topics. This helps students prioritize their study plan efficiently.

## Website
[SmashIT](https://www.smashit.onrender.com) | [QPaper.live (Coming Nov 2025)](https://www.qpaper.live)

## Demo
[![Demo Video](https://img.youtube.com/vi/DDds_Mai3zo/maxresdefault.jpg)](https://youtu.be/DDds_Mai3zo)

## Acknowledgements
- [Django](https://www.djangoproject.com/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [OCR space API](https://ocr.space/)  
- [scikit-learn](https://scikit-learn.org/)  
- [NumPy](https://numpy.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Auth0](https://auth0.com/)  

## Features
- Light/Dark mode toggle
- Question Categorization (MCQ, Short, Long, Numerical, etc.)
- Fullscreen mode
- Cross-platform support

## API Reference

### OCR.space API for Text Extraction  
#### Free OCR API Endpoint (POST)  
```bash
POST https://api.ocr.space/parse/image
```

#### GET OCR API Endpoint  
```bash
GET https://api.ocr.space/parse/imageurl?apikey=YOUR_API_KEY&url=IMAGE_URL
```

### API Parameters  
| Parameter               | Type      | Description |
|-------------------------|----------|-------------|
| `apikey`               | String   | **Required.** Your API key. |
| `url` / `file` / `base64Image` | String   | **Required.** URL, file upload, or Base64-encoded image. |
| `language`             | String   | **Optional.** Language for OCR. Default is **English (eng)**. |
| `isOverlayRequired`    | Boolean  | **Optional.** If `true`, returns text bounding box coordinates. |

### Example JSON Response  
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

## Authors
- [@Abhishek Kumar](https://github.com/coder-abhi07)

## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)  

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

## Deployment
To deploy this project, run:
```bash
npm run deploy
```

## Installation
### Prerequisites  
Ensure you have Python installed. You may also need `pip` and `virtualenv`.

### Steps  
```bash
git clone https://github.com/coder-abhi07/smashIT
cd smashIT
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Support
For support, email **ak0188644@gmail.com**.

## Screenshots
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
