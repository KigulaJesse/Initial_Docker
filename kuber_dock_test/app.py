from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <title>SSML Transformer</title>
</head>
<body>
    <h2>SSML Transformer</h2>
    <input type="text" id="userInput" placeholder="Enter text...">
    <button onclick="processText()">Transform</button>
    
    <h3>SSML Output:</h3>
    <p id="output"></p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

