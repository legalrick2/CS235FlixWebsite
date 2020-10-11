# """App entry point."""
# from skeleton import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(host='localhost', port=5000, threaded=False)

#from flask import Flask, redirect, url_for, render_template, request
from skeleton import create_app

app = create_app()

# @app.route("/<name>")
# def director(name):
#     return f"Hello director {name}"

# @app.route("/redir")
# def redir():
#     return redirect(url_for("user", name="Tester1!"))

if __name__ == "__main__":
    app.run()