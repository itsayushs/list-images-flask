from flask import Flask ,render_template
app=Flask(__name__)

@app.route('/')
def home():
    linklist=['https://farm5.staticflickr.com/4605/39366636264_4f0c5d3968_b.jpg', 'https://farm5.staticflickr.com/4742/28297288849_86de43aa6b_b.jpg', 'https://farm5.staticflickr.com/4765/40044460992_3a33b8e289_b.jpg', 'https://farm5.staticflickr.com/4718/28297354039_3b95730b61_b.jpg', 'https://farm5.staticflickr.com/4622/28297354319_dc5b94186b_b.jpg', 'https://farm5.staticflickr.com/4712/28297354959_67e584106b_b.jpg']
    return render_template('index.html',ayush=linklist)

app.run(debug=True)
