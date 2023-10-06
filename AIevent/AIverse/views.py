from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import AIverse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.core import serializers

import magic

def index(request):
    return render(request, 'event/index.html')

def explore(request):
    return render(request, 'event/explore.html')



def reg(request):
    return render(request, 'event/reg.html')

def admin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            data = serializers.serialize("python", AIverse.objects.all())
            # print(data)
            # print(type(data))
            for i in data:
                p = i['fields']['Team_member']
                p = p.replace(",", ",\n")
                i['fields']['Team_member'] = p 

            details = {
                'data': data
            }
            return render(request, 'event/master.html', details)

    return render(request, 'event/admin_login.html')

def handlelogout(request):
    logout(request)
    return redirect("index")

def prepare_payment(request):
    name = request.POST.get('name')
    number = request.POST.get('contact')
    email = request.POST.get('email')
    branch = request.POST.get('Branch')
    year = request.POST.get('Year')
    event = request.POST.get('event')
    team_size = request.POST.get('team')
    amount = request.POST.get('amount')
    member1 = request.POST.get('1')
    member2 = request.POST.get('2')
    member3 = request.POST.get('3')
    member4 = request.POST.get('4')
    if member1 is not None:
        team_members = member1
    if member2 is not None:
        team_members += f"\n{member2}"
    if member3 is not None:
        team_members += f"\n{member3}"
    if member4 is not None:
        team_members += f"\n{member4}"
    payment_data = {'name': name, 'number': number, 'email': email, 'branch': branch, 'year': year, 'event': event,'team_size': team_size, 'team_members':team_members, 'amount':amount}
    return render(request, 'event/payment.html', payment_data)

def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('contact')
        email = request.POST.get('email')
        branch = request.POST.get('Branch')
        year = request.POST.get('Year')
        event = request.POST.get('event')
        team_size = request.POST.get('team_size')
        team_members = request.POST.get('team_member')
        amount = request.POST.get('amount')
        screenshot = request.FILES["screenshot"]
        print(screenshot)
        transaction_ID = request.POST.get("transaction-id")
        AIverse_item = AIverse(Name=name, Event=event, Branch=branch, Year=year, Email=email, Contact=number,
                               Team_Size=team_size, Team_member=team_members, Screenshot=screenshot, Transaction_ID=transaction_ID, amount=amount)
        AIverse_item.save()
       
        from typing import List 
        p : List[str] = [
            f"Hi, {name}\nYou have succesfully registered for the \"{event}\" event.\nHere are the workshop details of cubic realm:\ntime:  9:00 pm\nvenue: home\n{screenshot}" , "second event", "third event", "fourth event", "fifth event"
        ]
        if (event == "Cubic Realm") : l : str = p[0]
        else: l: str = "not cubic realm"

        # send_mail(
        #     f"{event} Registration Succesfull",
        #     l,
        #     "svpcetaiverse@gmail.com",
        #     [email],
        #     fail_silently=False,
        # )
        msg = EmailMessage(
            f"{event} Registration Succesfull",
            l,
            "svpcetaiverse@gmail.com",
            [email],

        )

        with open(f"./media/Event/images/{screenshot}", 'rb') as file: file_content = file.read()
        mime_type = magic.from_buffer(file_content, mime=True)


        msg.attach(
            screenshot.name,
            file_content, 
            mime_type
        )
        msg.send()


        return redirect("index")
    
def about(request):
    return render(request,"event/about_dept.html")

def cr_reg(request):
    data = serializers.serialize("python", AIverse.objects.all().filter(Event="Cubic Realm"))
    dictionary_lol = {"data": data}
    return render(request, "event/cr_reg.html", dictionary_lol)
def cr_back(request):
    return render(request, 'event/master.html')

def gg_reg(request):
    data = serializers.serialize("python", AIverse.objects.all().filter(Event="GigaGen"))
    dictionary_lol = {"data": data}
    return render(request, "event/gg_reg.html", dictionary_lol)

def gg_back(request):
    return render(request, 'event/master.html')

def bb_reg(request):
    data = serializers.serialize("python", AIverse.objects.all().filter(Event="BeatBots"))
    dictionary_lol = {"data": data}
    return render(request, "event/bb_reg.html", dictionary_lol)

def bb_back(request):
    return render(request, 'event/master.html')

def optiml_reg(request):
    data = serializers.serialize("python", AIverse.objects.all().filter(Event="optiML"))
    dictionary_lol = {"data": data}
    return render(request, "event/optiml_reg.html", dictionary_lol)
def optiml_back(request):
    return render(request, 'event/master.html')

def vv_reg(request):
    data = serializers.serialize("python", AIverse.objects.all().filter(Event="VentureVista.AI"))
    dictionary_lol = {"data": data}
    return render(request, "event/vv_reg.html", dictionary_lol)
def vv_back(request):
    return render(request, 'event/master.html')

# def cubical_realm(request):
#     return render(request,"event/events/ccubical_realm.html")


#############################################################################################################
# ADDING ROUUTINGS FOR ALL EVENT PAGES (HREF)
#############################################################################################################

# configuring the basic path
import os  
from pathlib import Path 
from typing import List 

path: Path = Path("event/events")

EVENTS: List[str] = [  
    "cubical_realm.html", 
    "giga_gen.html", 
    "beat_bots.html", 
    "opti_ml.html", 
    "startup_mela.html"
    ]
# Added for cubical realm event page display
def cubical_realm(request) -> HttpResponse :
    i : str= EVENTS[0]
    cr: Path = os.path.join(path, i)
    print(type(render(request, cr)))
    return render(request, cr)

# Added for Gigi Gen  event page display
def giga_gen(request) -> HttpResponse:
    i : str= EVENTS[1]
    cr: Path = os.path.join(path, i)
    return render(request, cr)

# Added for Beat Bots event page display
def beat_bots(request) -> HttpResponse: 
    i : str = EVENTS[2]
    cr: Path = os.path.join(path, i)
    return render(request, cr)

# Added for Opti Ml event page display
def OptiML(request) -> HttpResponse :
    i: str = EVENTS[3]
    cr: Path = os.path.join(path, i)
    return render(request, cr)

# Added for Startup Mela event page display
def ss(request) :
    i : str = EVENTS[4]
    cr: Path = os.path.join(path, i)
    return render(request, cr)

# this comment is for demo purpose of git pull for kaushal 