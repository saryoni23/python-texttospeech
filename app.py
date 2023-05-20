from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    tts = gTTS(text=text, lang='id', tld='com')
    tts.save("output.mp3")
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True ,port=5001,use_reloader=False)
