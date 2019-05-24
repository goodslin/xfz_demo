from django.shortcuts import render, redirect, reverse
from django.http import StreamingHttpResponse, HttpResponse
from django.views.generic import View, ListView
from app03 import models
from django.core.paginator import Paginator, Page
from django.utils.decorators import method_decorator
from app03 import forms
from django.views.decorators.http import require_http_methods


def large_csv_view(request):
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=abc"
    rows = ("Row {}, {}\n".format(row, row) for row in range(0, 100000))
    response.streaming_content = rows
    return response


class AddBook(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持除GET以外的任何请求。")


def add_article(request):
    articles = []
    for x in range(0, 101):
        article = models.Article(title="%s" % x, content="%s" % x)
        articles.append(article)
    models.Article.objects.bulk_create(articles)
    return HttpResponse("add success")


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'

    # page_kwarg = 'p'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)

        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        # left_pages
        if current_page <= around_count * 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        # right_pages
        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'current_page': current_page,
            'num_pages': num_pages,
        }


def login_required(func):
    def wrapper(request, *args, **kwargs):
        username = request.GET.get('username')
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    return wrapper


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse('个人中心')


def login(request):
    return HttpResponse('登陆')


def error_view(request):
    return render(request, '404.html')


class IndexView(View):
    def get(self, request):
        form = forms.MessageBoardFrom()
        return render(request, 'app03/index.html', context={"form": form})

    def post(self, request):
        form = forms.MessageBoardFrom(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print(title, content, email, reply)
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('fail')


class RegisterView(View):
    def get(self, request):
        form = forms.RegisterForm()
        return render(request, 'app03/register.html', context={'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            models.User.objects.create(username=username, telephone=telephone)
            print(username, telephone)
            return HttpResponse('注册成功！')
        else:
            print(form.get_errors())
            return HttpResponse('注册失败！')


def add_book(request):
    form = forms.AddBookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        page = form.cleaned_data.get('page')
        price = form.cleaned_data.get('price')
        print(title, page, price)
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('Fail')


class IndexViews(View):
    def get(self, request):
        return render(request, 'index1.html')

    def post(self, request):
        myfile = request.FILES.get('myfile')
        with open('somefile.txt', 'wb') as fp:
            for chunk in myfile.chunks():
                fp.write(chunk)
        return HttpResponse('上传成功！')
