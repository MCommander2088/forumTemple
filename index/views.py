import datetime

from django.shortcuts import render, redirect

from .models import Level


# Create your views here.

def index(request):
    '''posts = [
        {'title': 'hello world',
         'pub_date': '2024/11/26',
         'author': 'MCommander2077',
         'status': 'active',
         'level_author': 'cmd2077',},
        {'title': 'banned post',
         'pub_date': '2024/11/26',
         'author': 'MCommander2077',
         'status': 'banned',
         'level_author': 'cmd2077',},
        {'title': '123hea',
         'pub_date': '2024/11/26',
         'author': 'MCommander2077',
         'status': '123',
         'level_author': 'cmd2077',},
    ]'''
    objects = Level.objects.all()
    posts = []
    for post in objects:
        posts.append(
            {
                'id': post.id,
                'song_name': post.song_name,
                'song_author': post.song_author,
                'pub_date': post.pub_date.strftime('%m/%d/%Y  %H:%M:%S'),
                'status': post.status,
                'level_author': post.level_author,
                'dl_link': post.dl_link,
                'vd_link': post.vd_link,
            }
        )

    context = {
        'date': datetime.date.today(),
        'TOP1': {'title': 'Top1 Name', 'pub_date': '2024/11/25', 'author': 'MCommander2077', 'href': '.'},
        'TOP2': {'title': 'Top2 Name', 'pub_date': '1145/01/04', 'author': 'MCommander2088', 'href': '.'},
        'TOP3': {'title': 'Top3 Name', 'pub_date': '1919/08/10', 'author': 'MCommander1145', 'href': '.'},
        'posts': posts,
    }
    return render(request, "index.html", context)


def info(request, id):
    try:
        id = int(id)
    except ValueError:
        #print(id,type(id))
        return redirect('index')

    if id > 0:
        pass
    else:
        print(id,type(id))
        return redirect("index")

    obj = Level.objects.filter(id=id)
    obj = obj.first()
    post = {
        'id': obj.id,
        'song_name': obj.song_name,
        'song_author': obj.song_author,
        'pub_date': obj.pub_date.strftime('%m/%d/%Y  %H:%M:%S'),
        'status': obj.status,
        'level_author': obj.level_author,
        'dl_link': obj.dl_link,
        'vd_link': obj.vd_link,
    }
    return render(request, "info.html", {'post': post})


def info_0(request):
    return redirect("index")
