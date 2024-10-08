# Plagiarism Detector

## Overview
The **Plagiarism Detector** is a web application designed to identify instances of plagiarism in submitted texts. Utilizing machine learning techniques, this application analyzes input text and determines whether it is plagiarized or original. The project is built using Flask and leverages natural language processing (NLP) for effective detection.

## What is Plagiarism?
Plagiarism is the act of using someone else’s work, ideas, or intellectual property without proper attribution or permission and presenting it as one’s own. This can include copying text, imitating ideas, or using expressions created by others across various forms of creative work.

## Features
- **User-Friendly Interface**: Simple and intuitive design for easy interaction.
- **Real-Time Detection**: Instant feedback on the originality of the submitted text.
- **Machine Learning Model**: Utilizes a trained model for accurate plagiarism detection.
- **TF-IDF Vectorization**: Implements term frequency-inverse document frequency for effective text comparison.

## Tech Stack
- **Client**: HTML/CSS, Flask
- **Server**: Python
- **Libraries**:
  - Flask
  - Pickle (for model loading)
  - Scikit-learn (for vectorization)

## Installation
To run the Plagiarism Detector on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**:
   Make sure you have Python installed and then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Flask server with:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/home`.

## Usage
To detect plagiarism, follow these steps:

1. Navigate to the home page.
2. Input or paste the text you want to check into the provided text area.
3. Click on the "Detect" button.
4. The result will indicate whether the text is "Plagiarism" or "Not Plagiarism".

## Code Snippet
Here’s a brief overview of how the main functionality is implemented in `app.py`:

```python
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form['text']
    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)[0]
    return render_template('index.html', result="Plagiarism" if result == 1 else "Not Plagiarism")
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.

## License
This project is licensed under the MIT License.

---

This README provides a comprehensive guide to understanding and utilizing the Plagiarism Detector project effectively.

Citations:
[1] https://github.com/Karthik-02/plagiarism-detection
[2] https://github.com/karolcichosz/project-plagiarism-detection
[3] https://github.com/parshva45/Plagiarism-Detector
[4] https://github.com/wchowdhu/plagiarism-detection
[5] https://github.com/grantgasser/plagiarism-detection-nlp
[6] https://github.com/gauravansal/Plagiarism-Detection
[7] https://github.com/topics/plagiarism-detector?o=desc&s=stars
[8] https://github.com/fibinfa/Plagiarism-Detector