from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/play')
# def playground():
#     return render_template("index.html")

# @app.route('/play/<int:times>')
# def playground1(times):
#     return render_template("index.html", times=times)

@app.route('/play/<int:times>/<bg_color>')
def playground2(times, bg_color):
    return render_template("index.html", times=times, bg_color=bg_color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

