from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"id": 1, "title": "İlk Yazı", "content": "Bu, blogun ilk gönderisidir."},
    {"id": 2, "title": "İkinci Yazı", "content": "Bu da ikinci yazımız."}
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
