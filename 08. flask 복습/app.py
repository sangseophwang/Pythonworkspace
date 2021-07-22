from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

names = ['John', 'Jane', "Elice"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user', methods=["GET", "POST", "PATCH", "DELETE"])
def user():
    if request.method == "POST":
        username = request.form["username"]
        if username not in names:
            names.append(username)

    elif request.method == "PATCH":
        username = request.form["username"]
        new_username = request.form["new_username"]
        if username in names:
            idx = names.index(username)
            names[idx] = new_username
            return jsonify(result="success")
        else:
            return jsonify(result="failed")
    elif request.method == "DELETE":
        username = request.form['username']
        if usename in names:
            names.remove(username)
            return jsonify(result="success")
        else:
            return jsonify(result="fail")

    return render_template("user.html", names=names)


if __name__ == '__main__':
    app.run(debug=True)
