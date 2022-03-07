from flask import request, jsonify
from flask.views import MethodView
from app import app
from app.validator import validate
from app.models import Ad, User
from app.schema import USER_CREATE, AD_CREATE


# Должны быть реализованы методы создания/удаления/редактирования объявления
# POST метод должен создавать объявление, GET - получать объявление, DELETE - удалять объявление.

@app.route("/hello")
def api_hello_world():
    return jsonify({"Hello": "world"})


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


class AdView(MethodView):

    def get(self, ad_id):
        ad = Ad.by_id(ad_id)
        return jsonify(ad.to_dict())

    @validate('json', AD_CREATE)
    def post(self):
        ad = Ad(**request.json)
        ad.add()
        return jsonify(ad.to_dict())

    def delete(self, ad_id):
        ad = Ad.by_id(ad_id)
        ad.delete()
        return jsonify({'message': f'Ad was deleted'})


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'))
app.add_url_rule('/users', view_func=UserView.as_view('users_create'))

app.add_url_rule('/ads', view_func=AdView.as_view('ads_create'))
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('get_ad'))
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_delete'))
