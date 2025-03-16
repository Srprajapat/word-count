# Word Count Application

## Overview
This is a distributed word count application that implements the **MapReduce** algorithm using **Python's threading module**. The backend is developed using **Flask**, and the frontend is built with **HTML, CSS, and JavaScript**.

## Features
- Accepts text input from a user or file upload.
- Uses **multithreading** to process text efficiently.
- Implements **MapReduce** to count word occurrences.
- Displays results dynamically on the frontend.
- Provides a REST API for word count computation.

## Technologies Used
- **Python** (Flask, threading, re)
- **JavaScript** (Fetch API for API requests)
- **HTML & CSS** (User interface)

## Installation & Setup
### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Srprajapat/word-count-app.git
   cd word-count-app
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## API Usage
### Endpoint: `/wordcount`
**Method:** POST  
**Request Format (JSON):**
```json
{
    "text": "This is an example text with repeated words."
}
```
**Response Format (JSON):**
```json
{
    "this": 1,
    "is": 1,
    "an": 1,
    "example": 1,
    "text": 1,
    "with": 1,
    "repeated": 1,
    "words": 1
}
```

## Future Enhancements
- Support for **file uploads** (processing text from documents).
- Deploying the application online.
- Optimizing with multiprocessing for larger text processing.

## Contributing

Feel free to fork this repository and make improvements. Pull requests are welcome! 🚀

## Contact

For any questions or suggestions, reach out to me at [**seetaram.22jics083@jietjodhpur.ac.in**](mailto\:seetaram.22jics083@jietjodhpur.ac.in) or connect on [LinkedIn](https://www.linkedin.com/in/seetaram-prajapat).


