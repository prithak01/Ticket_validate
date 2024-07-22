# Ticket Validation System

This repository contains the backend component for the ticket validation system, including OCR processing and validation logic.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Unix or MacOS: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the application

1. Ensure you're in the project root directory
2. Run `python src/main.py`

## Testing

(More instructions for running tests will be added once we've set them up)

## API Endpoints

- `/validate` (POST): Submit a ticket image for validation
  - Request: Multipart form data with 'image' field
  - Response: JSON with validation results

(More endpoints will be added as they're developed)
