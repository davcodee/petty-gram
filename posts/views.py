"""Posts Views"""
from django.shortcuts import render

#utilities
from datetime import datetime


posts = [
    {
        'title': 'My dog',
        'user': {
            'name': 'David Morales',
            'picture':'https://content-static.upwork.com/uploads/2014/10/01073427/profilephoto1.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/200/300'
    },
    {
        'title': 'Miztli',
        'user':{
            'name': 'Isaac Ulises',
            'picture': 'https://avatars3.githubusercontent.com/u/28477116?s=400&u=76e53b6a61862ac52245edce97ad33f47490cab1&v=4'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/200/300'
    },
    {
        'title': 'Percefone',
        'user': {
            'name': 'Anita michelle',
            'picture': 'https://avatars3.githubusercontent.com/u/28477116?s=400&u=76e53b6a61862ac52245edce97ad33f47490cab1&v=4'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/200/300'
    },

]

def list_posts(request):
    return render(request,'feed.html', {
        'posts': posts
    })

