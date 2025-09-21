from flask import Flask, render_template, request
from youtube_comment_downloader import YoutubeCommentDownloader as ytd

app = Flask(__name__)
downloader = ytd()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_comments", methods=["POST"])
def get_comments():
    url = request.form["url"]
    comments = []

    try:
        for c in downloader.get_comments_from_url(url, sort_by=0):
            comments.append(c["text"])
            if len(comments) >= 10:  # ambil 10 komentar saja
                break
    except Exception as e:
        comments = [f"Error: {e}"]

    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)