from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Global list of students
listStd = ["yugesh", "kishor", "gajen", "Gopi"]

@app.route("/")
def home():
    return render_template("index.html", students=listStd)

@app.route("/add", methods=["POST"])
def add_student():
    newStd = request.form["name"]
    if newStd in listStd:
        return f"Student {newStd} already exists!", 400
    listStd.append(newStd)
    return redirect(url_for("home"))

@app.route("/search", methods=["POST"])
def search_student():
    srcStd = request.form["name"]
    if srcStd in listStd:
        return f"Record found: {srcStd}", 200
    return f"No record found for: {srcStd}", 404

@app.route("/remove", methods=["POST"])
def remove_student():
    rmStd = request.form["name"]
    if rmStd in listStd:
        listStd.remove(rmStd)
        return redirect(url_for("home"))
    return f"No record found for: {rmStd}", 404

# Run the app
if __name__ == "__main__":
    # Use the PORT environment variable provided by Render, or default to 5000 if not set
    port = int(os.environ.get("PORT", 15000))
    app.run(host="0.0.0.0", port=port)
