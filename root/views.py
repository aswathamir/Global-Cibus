from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import User, models
import string, random, json, requests
from datetime import date


# Create your views here.
def login(request):
    mail = request.POST['email']
    passw = request.POST['pass']
    try:
        x = User.objects.get(email=mail)
        if x.password == passw:
            x.key = generateKey()
            x.save()
            response = HttpResponse('<html><script>window.location.replace("/");</script></html>')
            response.set_cookie('x-key', x.key, max_age=864000)
            return response
        else:
            html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
            return html
    except Exception as e:
        print(e)
        html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
        return html
    
    
def register(request):
    try:
        email = request.POST['email']
        if not User.objects.filter(email=email).exists():
            userid = generateUserId(User)
            password = request.POST['pass']
            reg = User(id=userid, key='UgbBYNCjNrpdSSPvBJ', email=email, joined_at=date.today(), password = password)
            reg.save()
            html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
            return html
        else:
            html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
            return html
    except Exception as e:
        print(e)
        html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
        return html
    
def registeruser(request):
    key = request.COOKIES.get('x-key')
    if validateUser(key):
        return render(request, 'main.html')
    else: 
        return render(request, 'register.html')

def logout(request):
    xkey = request.COOKIES.get('x-key')
    if validateUser(xkey):
        id = getUserId(xkey)
        user = User.objects.get(id=id)
        user.key = generateKey()
        user.save()
        html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
        return html
    else:
        html = HttpResponse('<html><script>window.location.replace("/");</script></html>')
        return html

def root(request):
    key = request.COOKIES.get('x-key')
    if validateUser(key):
        return render(request, 'main.html')
    else: 
        return render(request, 'login.html')
    
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def contactform(request):
    try:
        if request.method == 'POST':
            post_data = request.POST
            discord_webhook_url = 'https://discord.com/api/webhooks/1225090099864146023/TTN_tB_5tbf3qaC1lpwwyapR-R0Uk8eb-H3wVV_mPM5jr7lbWnF4Q9vTJCv3WfWyN1I4'
            message = f'**Email: **{post_data["email"]}\n**Message: **{post_data["message"]}'
            payload = {
                'username': post_data['name'],
                'content': message,
                }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(discord_webhook_url, json=payload, headers=headers)
        return HttpResponse("{}")
    except:
        return HttpResponse("")




def generateUserId(model):
    max_serial = model.objects.aggregate(models.Max('id'))['id__max']
    print(max_serial)
    if max_serial is None:
        return 999999999999 + 1
    return max_serial + 1
    
def generateKey():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.sample(chars, k=18))

def validateUser(token):
    try:
        x = User.objects.get(key=token)
        return True 
    except Exception as e:
        return False
    
def getUserId(token):
    try:
        x = User.objects.get(key=token)
        return x.id
    except:
        return None