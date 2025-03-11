from flask import Flask, render_template, request
from caesar_cipher import CaesarCipher  # Đảm bảo bạn có file hoặc module này

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form.get("inputPlainText")
    key = int(request.form.get("inputKeyPlain", 0))
    
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form.get("inputCipherText")
    key = int(request.form.get("inputKeyCipher", 0))
    
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
