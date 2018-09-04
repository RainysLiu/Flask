from flask import Blueprint
from flask_cache import Cache


cache = Cache(config={'CACHE_TYPE':'simple'})
blue = Blueprint('blue',__name__)


@blue.route('/getinfo')
@cache.cached(timeout=30,key_prefix='infocache')   #试图函数的结果在cache中保存30秒
def getinfo():
    print('进入getinfo方法了')
    return '<h3>Are You Ok?</h3>'
