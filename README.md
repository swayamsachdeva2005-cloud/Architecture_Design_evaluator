# Blueprint Cop — AI-Powered Building Plan Review System

Blueprint Cop is an AI-powered web application designed to support the **preliminary review of architectural blueprint PDFs**. It uses Google Gemini Vision to analyze blueprint images and generate a structured inspection report containing building information, potential issues, inspection checks, and recommendations.

Developed as part of an AI hackathon at **IIT Jammu**, where the team received a **Special Recognition Award**.

> **Responsible use:** Blueprint Cop is a prototype for preliminary analysis and educational demonstration. AI-generated findings are not a substitute for review by a qualified architect or verification against applicable building regulations.

## Application Screenshots

### 1. Homepage

The landing page introduces Blueprint Cop and provides access to the blueprint review experience.

![Blueprint Cop homepage](screenshots/01-homepage.png)

### 2. Compliance Dashboard

A visual preview of the blueprint analysis experience and inspection summary.

![Blueprint Cop compliance dashboard](screenshots/02-compliance-dashboard.png)

### 3. Inspection Results

The results interface presents potential issues and inspection checks, including severity and recommendations where available.

![Blueprint Cop inspection results](screenshots/03-inspection-results.png)

## Key Features

- Upload building blueprint PDFs for preliminary analysis.
- Analyze blueprint images using Google Gemini Vision.
- Extract building information available in the document.
- Highlight potential design or documentation concerns.
- Present an AI-generated compliance score when returned by the analysis.
- Display inspection status, checks, and recommendations.
- Validate structured responses using Pydantic models.
- Review results through a web-based frontend.
- Connect the frontend to a FastAPI backend.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| AI model | Google Gemini 2.5 Flash |
| PDF processing | PyMuPDF |
| Image processing | Pillow |
| Data validation | Pydantic |
| API server | Uvicorn |

## How It Works

```text
User
  |
  v
Upload Blueprint PDF
  |
  v
Frontend sends file to FastAPI
  |
  v
PDF page converted to image
  |
  v
Google Gemini Vision analyzes image
  |
  v
Structured response validated with Pydantic
  |
  v
Inspection report displayed in the frontend
```

1. The user uploads a blueprint PDF through the web interface.
2. The frontend sends the file to the backend upload endpoint.
3. The backend processes the document and converts the relevant page into an image.
4. Gemini Vision analyzes the image using the configured prompt.
5. The model returns building information, potential findings, checks, and recommendations.
6. Pydantic validates the response structure.
7. The frontend displays the inspection report.

Results depend on document quality, the model's response, and the information visible in the uploaded blueprint. AI findings should be independently verified.

## Project Structure

```text
Architecture_Design_evaluator/
├── backend/
│   ├── app/
│   │   ├── automation/
│   │   │   ├── analyze.py
│   │   │   └── __init__.py
│   │   ├── routes/
│   │   │   ├── upload.py
│   │   │   └── __init__.py
│   │   ├── uploads/
│   │   ├── ai_engine.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── prompts.py
│   │   └── __init__.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── result.html
│   ├── result_script.js
│   ├── result.css
│   ├── script.js
│   └── style.css
├── screenshots/
│   ├── 01-homepage.png
│   ├── 02-compliance-dashboard.png
│   └── 03-inspection-results.png
├── .gitignore
└── README.md
```

*Update the tree if your actual filenames differ. Do not commit your `.env` file or API key.*

## Getting Started

### Prerequisites

- Python installed
- pip
- A Google Gemini API key
- A modern web browser

### 1. Clone the repository

After creating your GitHub repository, replace the URL below with its actual clone URL:

```bash
git clone https://github.com/YOUR-USERNAME/Architecture_Design_evaluator.git
cd Architecture_Design_evaluator
```

### 2. Install backend dependencies

```bash
cd backend
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file inside `backend/` and add the variable name expected by your backend code. If your code reads `GEMINI_API_KEY`, use:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never publish your real API key.

### 4. Start the backend

From the `backend` directory, run:

```bash
python -m uvicorn app.main:app --reload
```

If startup succeeds, the API should be available at `http://127.0.0.1:8000`, and interactive API documentation should be available at `http://127.0.0.1:8000/docs`.

### 5. Start the frontend

Open a second terminal:

```bash
cd frontend
python -m http.server 5500
```

Open `http://127.0.0.1:5500` in your browser. Ensure the frontend is configured to call the running backend and that the backend CORS settings allow the frontend origin.

## API Reference

### Upload a blueprint

- **Method:** `POST`
- **Endpoint:** `/upload`
- **Content type:** `multipart/form-data`
- **Form field:** `file` — the blueprint PDF

The example below illustrates the general response shape; refer to the backend models and `/docs` for the actual schema.

```json
{
  "building_details": {},
  "inspection_result": {},
  "summary": "",
  "inspection_checks": [],
  "violations": [],
  "recommendations": []
}
```

## Security and Responsible Use

- Keep API keys in environment variables and never commit `.env`.
- Add virtual environments, cache files, and temporary uploads to `.gitignore`.
- Only upload architectural documents you are authorized to share.
- Treat AI findings as preliminary and verify them with qualified professionals.
- Do not treat an AI-generated score or report as proof of legal or building-code compliance.

## Future Enhancements

- Multi-page blueprint analysis
- Integration with verified building-code databases
- Blueprint annotation and visual highlighting
- Downloadable PDF inspection reports
- User authentication and project history
- Support for additional architectural drawing formats
- Cloud deployment and improved document management

## Recognition

Developed as part of an AI hackathon at **IIT Jammu**.

**Achievement:** Special Recognition Award.

## Contributors

- Swayam Sachdeva
- Anshuman Sachdeva

## License

This project is intended for educational and hackathon purposes. Add a license file if you decide to distribute the project under a specific open-source license.
