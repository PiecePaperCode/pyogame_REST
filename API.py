from flask import *
from ogame import OGame
from ogame.constants import *
import inspect

API = Flask(__name__, static_url_path='/', static_folder='/')
empire = None


def clean_dict(dict):
    for key_to_remove in ['__module__', '__dict__', '__weakref__', '__doc__']:
        if key_to_remove in dict:
            del dict[key_to_remove]
    return dict


def ogame_to_json(fun, arg=None):
    result = None
    if isinstance(fun, str):
        result = fun
        msg = {'result': result}
        return msg
    else:
        if arg is not None: fun = fun(**arg)
        else: fun = fun()

        if inspect.isclass(fun):
            result = clean_dict(dict(vars(fun)))
            for key, value in result.items():
                if inspect.isclass(value):
                    result[key] = clean_dict(dict(vars(value)))
        elif isinstance(fun, list):
            result = []
            for element in fun:
                if inspect.isclass(element):
                    element = clean_dict(dict(vars(element)))
                    for key, value in element.items():
                        if inspect.isclass(value):
                            element[key] = clean_dict(dict(vars(value)))
                    result.append(element)
                else:
                    result = fun
                    break
        elif isinstance(fun, bool):
            result = fun
        msg = {'result': result}
        print(result)
        return msg


@API.route('/POST', methods=['GET'])
def post():
    return send_file('post.html')


@API.route('/', methods=['GET'])
def index():
    if empire is None:
        return {'error': 'Not Logged in'}, 403
    else:
        msg = {'functions': dir(empire)[27:]}
    return jsonify(dict(msg))


@API.route('/login', methods=['POST'])
def login():
    try:
        arg = request.get_json()
        global empire
        empire = OGame(**arg)
        return {'login': 'successful'}
    except:
        return {'login': 'Bad Login'}, 400


@API.route('/<function>', methods=['GET'])
def function(function):
    try:
        fun = getattr(empire, function)
        return ogame_to_json(fun)
    except Exception as E:
        return {'error': str(E)}, 403


@API.route('/<function>', methods=['POST'])
def function_post(function):
    try:
        arg = request.get_json()
        if arg == {} or arg is None:
            raise Exception('Empty or invalid json POST Request')
        fun = getattr(empire, function)
        return ogame_to_json(fun, arg)
    except Exception as E:
        return {'error': str(E)}, 403


API.run()
