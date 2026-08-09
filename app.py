from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Demo</title>
        </head>

        <body style="text-align:center; margin-top:100px;">

            <h1>🚀 CI/CD Demo Application</h1>

            <h2>Flask + Docker + Jenkins</h2>

            <p>Application deployed successfully!</p>

        </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "cicd-demo"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
