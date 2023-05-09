from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def counter():
    if "views" in session:
        session["views"] += 1
    else:
        session["views"] = 1
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.