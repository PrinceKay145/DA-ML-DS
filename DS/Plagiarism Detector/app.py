from flask import Flask, render_template, request
import pickle
import os
print(os.getcwd()   )

app = Flask(__name__, template_folder='/Users/princekay/programming/projects/templates')

model = pickle.load(open('/Users/princekay/programming/projects/penv/model.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('/Users/princekay/programming/projects/penv/tfidf_vectorizer.pkl', 'rb'))

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form['text']

    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)[0]
    result = "Plagiarism" if result == 1 else "Not Plagiarism"
    return render_template('index.html', result=result)
if __name__ == "__main__":
    app.run(debug=True)