import sys
import ToyRobot
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
tr = ToyRobot.ToyRobot()

CMDReader = {
	"PLACE": tr.Place,
	"LEFT": tr.Left,
	"RIGHT": tr.Right,
	"MOVE": tr.Move,
	"REPORT": tr.Report
}


# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('Enter a command:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	message = ""
	text = form.name.data
	if text != None:
		text = text.replace(",", " ")
		toks = text.split()
		if toks[0] == "PLACE" and len(toks) == 4:
			tr.Place(int(toks[1]),int(toks[2]),toks[3])
		elif len(toks) == 1 and toks[0] != "PLACE":
			func = CMDReader.get(toks[0], None)
			if func == None:
				message = "Command Not Found"
			else:
				message = func()
		else:
			message = "Command Not Found"
	return render_template('index.html', form=form, message=message)