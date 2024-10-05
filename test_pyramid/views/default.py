from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home', renderer='test_pyramid:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'test-pyramid'}


@view_config(route_name='hello')
def hello_world(request):
    body = '<h1>Hello everyone!</h1>'
    return Response(body)