from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learn_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learn_logs/topics.html',context)


def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request,'learn_logs/topic.html', context)

def new_topic(requset):
    """添加新主题"""
    if requset.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据库进行处理
        form = TopicForm(requset.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learn_logs:topics'))
    context = {'form':form}
    return render(requset,'learn_logs/new_topic.html',context)
