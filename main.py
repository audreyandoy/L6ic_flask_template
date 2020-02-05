import flask
app = flask.Flask(__name__)

dictionary = {
  "t-shirt": "blue long sleeve",
  "pants": "keeps these on!",
  "shoes": "no shoes no service"
}

@app.route('/')
def home():
  return flask.render_template('index.html', items = dictionary)

@app.route('/store/<item>')
def lookup(item):
  if item in dictionary:
    return flask.render_template(
      'index.html',
      item = item,
      definition = dictionary[item])
  else:
    return flask.render_template('index.html',
      item = "not found",
      definition = "item doesn't exist"
    )
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

