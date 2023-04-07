from flask import Flask, render_template


app = Flask( __name__ )


@app.route("/", methods = ["GET"] )
def index():
    return render_template( "index.html", row=8, col=8, color_one = "red", color_two = "black")


@app.route( "/<int:x>", methods = ["GET"] )
def row(x):
    return render_template( "index.html", row=x, col=8, color_one = "red", color_two = "black")


@app.route( "/<int:x>/<int:y>", methods = ["GET"] )
def row_col(x,y):
    return render_template( "index.html", row=x, col=y, color_one = "red", color_two = "black")


@app.route( "/<int:x>/<int:y>/<string:one>", methods = ["GET"] )
def row_col_one(x,y,one):
    return render_template( "index.html", row=x, col=y, color_one = one, color_two = "black")


@app.route( "/<int:x>/<int:y>/<string:one>/<string:two>", methods = ["GET"] )
def row_col_two(x,y,one,two):
    return render_template( "index.html", row=x, col=y, color_one = one, color_two = two)


if __name__ == "__main__":
    app.run( debug = True )