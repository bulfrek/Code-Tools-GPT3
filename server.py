from flask import Flask, render_template, request
import openai
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def comment():
  if request.form.get('improve'):
    question = (f"Improve this code without comments: {request.form['input-box']}")

  elif request.form.get('comment'):
    question = (f"Display every lines of this code and add comments: {request.form['input-box']}")

  elif request.form.get('text2code'):
    question = (f"Translate this text to a {request.form['language']} code without comments: {request.form['input-box']}")
    
    
  openai.api_key = "ENTER YOUR API KEY HERE"
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=question,
      max_tokens=1024,
      temperature=0.5,
    )
  var=(response["choices"][0]["text"])
 
  if request.form.get('improve'):
      return render_template('improve.html', var=var)

  elif request.form.get('comment'):
      return render_template('comment.html', var=var)
      
  elif request.form.get('text2code'):
      return render_template('text2code.html', var=var)
    

if __name__ == '__main__':
  app.run(host='0.0.0.0')

   