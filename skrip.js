// Dapatkan elemen-elemen yang diperlukan
const inputText = document.getElementById('inputText');
const speakButton = document.getElementById('speakButton');

// Tambahkan event listener saat tombol diklik
speakButton.addEventListener('click', () => {
  // Dapatkan teks yang dimasukkan oleh pengguna
  const text = inputText.value;
  
  // Buat objek SpeechSynthesisUtterance untuk menghasilkan suara
  const utterance = new SpeechSynthesisUtterance(text);
  
  // Mulai pembacaan suara
  speechSynthesis.speak(utterance);
});
