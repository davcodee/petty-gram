"""Posts Views"""
from django.http import HttpResponse

#utilities
from datetime import datetime
posts = [
    {
        'name': 'My dog',
        'user': 'David Morales',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name': 'My dog',
        'user': 'David Morales',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name': 'My dog',
        'user': 'David Morales',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },

]

def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i> {timestamp}</small></p>
            <p><strong>{name}</strong></p>
            <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))


