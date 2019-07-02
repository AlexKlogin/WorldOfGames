from flask import Flask

app = Flask(__name__)

error_html_template = '<html>' \
            '<head>' \
                '<title>Scores Game</title>' \
            '</head>' \
            '<body>' \
                '<h1>' \
                    '<div id="score" style="color:red">{ERROR}</div>' \
                '</h1>' \
            '</body>' \
      '</html>'

no_error_html_template = '<html>' \
            '<head>' \
                '<title>Scores Game</title>' \
            '</head>' \
            '<body>' \
                '<h1>' \
                    'The score is <div id="score">{SCORE}</div>' \
                '</h1>' \
            '</body>' \
      '</html>'

import Utils

@app.route("/")
def home():
    try:
        with open('Scores.txt', "r") as file:
            current_score = file.read()
            Utils.define_BAD_RETURN_CODE(0)
    except:
        print('Could not open Scores.txt.')
        Utils.define_BAD_RETURN_CODE(1)

    if Utils.BAD_RETURN_CODE == 0:
        html_text = no_error_html_template.format(SCORE = current_score)
    else:
        html_text = error_html_template.format(ERROR = "Read-Write Error")
    return html_text


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


if __name__ == "__main__":
    app.run(debug=True)