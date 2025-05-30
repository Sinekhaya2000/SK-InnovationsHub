@app.route('/')
def home():
    print("Rendering index.html")
    return render_template('index.html')
