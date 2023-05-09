from flask import Flask, render_template, render_template, request, redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def form_data():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


@app.route('/process', methods=["POST"])
def process_data():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")


@app.route('/result')
def display_data():
    return render_template("display.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
