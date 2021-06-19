from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    nameC = "Doctor Strange"
    show_image = True
    gif = "https://br.pinterest.com/pin/667869819722720151/"
    return render_template(
        "index.html",
        nameC = nameC,
        show_image = show_image,
        gif = gif,
    )
@app.route('/badass')
def badass():
    nameC = "Doctor Strange"
    show_image = True
    gif = "https://br.pinterest.com/pin/718253840567968037/"
    return render_template(
        "index.html",
        nameC = nameC,
        show_image = show_image,
        gif = gif,
    )
if __name__ == "__main__":
   app.run(debug=True)
