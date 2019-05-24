from .models import User


class FrontUserMiddleware(object):
    def __init__(self, get_response):
        # 执行初始化代码
        print('front_user_middleware初始化代码。。。')
        self.get_response = get_response

    def __call__(self, request):
        # 在这个代码执行之前的代码，是request到view之前到代码
        print('request到达view之前执行的代码。。。')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = self.get_response(request)
        print('response到达浏览器之前执行的代码。。。')
        # response对象到达浏览器之前执行的代码
        return response
