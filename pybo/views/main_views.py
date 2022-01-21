from flask import Blueprint, url_for
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main',__name__, url_prefix='/')

@bp.route('/home')
def home():
    return "hello home"
@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question._list'))
    #return 'index'