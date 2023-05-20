from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

# Fungsi untuk mengganti suara
def change_voice(voice_id):
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.id == voice_id:
            engine.setProperty('voice', voice.id)
            return True
    return False

# Fungsi untuk mengatur logat bahasa Indonesia
def set_indonesian_language():
    engine.setProperty('language', 'id')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    engine.say(text)
    engine.runAndWait()
    return 'Suara berhasil diputar'

@app.route('/change-voice', methods=['POST'])
def set_voice():
    voice_id = request.form['voice']
    if change_voice(voice_id):
        return 'Suara berhasil diubah'
    else:
        return 'Suara tidak ditemukan'

if __name__ == '__main__':
    set_indonesian_language()  # Mengatur logat bahasa Indonesia
    app.run(port=5001)  # Ganti port sesuai kebutuhan Anda
