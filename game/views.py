from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from .models import User, Quarterback, Runningback, Widereceiver, Tightend, Kicker, Team
from .forms import Quarterbackform, Runningbackform, Widereceiverform, Tightendform, Kickerform, Teamform
from django.views.generic.base import TemplateView
import requests




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("show"))
        else:
            return render(request, "game/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "game/login.html")

#@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("show"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "game/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "game/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        
        return redirect('createteamname')
    else:
        return render(request, "game/register.html")



def show(request): 

    user = request.user

    if user.is_authenticated:

        if request.method == 'POST':
            Team.objects.filter(user=request.user.id).update(team_name = request.POST.get('teamname'))
        
        team_name = Team.objects.filter(user=request.user.id)
        myteamname = ''

        for t in team_name:
            print(t.team_name)
            myteamname = t.team_name

        QB = Quarterback.objects.filter(author_id=request.user.id)
        RB = Runningback.objects.filter(author_id=request.user.id)
        WR = Widereceiver.objects.filter(author_id=request.user.id)
        TE = Tightend.objects.filter(author_id=request.user.id)
        K = Kicker.objects.filter(author_id=request.user.id)


        QBname = ''
        RBname = ''
        WRname = ''
        TEname = ''
        Kname = ''

        Kscore = 0
        QBscore = 0
        RBscore = 0
        WRscore = 0
        TEscore = 0

        # Set the Playername variables

        for q in QB:
            QBname = q.name
               
        
        for r in RB:
            RBname = r.name

        for w in WR:
            WRname = w.name

        for t in TE:
            TEname = t.name

        for k in K:
            Kname = k.name



        url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerGameStatsByWeek/2019/6?key=c3df3464e99245a6a7970f51c008cbee'

        r = requests.get(url.format()).json()

        scores = []

        
        for i in r:
            player_info = {
                'player_id' : i['PlayerID'],
                'player_name' : i['Name'],
                'points': i['FantasyPoints']
            }

            scores.append(player_info)
        
        totalpoints = []



        for score in scores:
            if score['player_name'] in QBname:
                QBscore = float(score['points'])
                totalpoints.append(QBscore)
                Quarterback.objects.filter(author_id=request.user.id).update(score = QBscore)

            elif score['player_name'] not in QBname:
                totalpoints.append(0) 

        for score in scores:
            if score['player_name'] in RBname:
                RBscore = float(score['points'])
                totalpoints.append(RBscore)
                Runningback.objects.filter(author_id=request.user.id).update(score = RBscore)

            elif score['player_name'] not in RBname:
                totalpoints.append(0) 

        for score in scores:
            if score['player_name'] in WRname:
                WRscore = float(score['points'])
                totalpoints.append(WRscore)
                Widereceiver.objects.filter(author_id=request.user.id).update(score = WRscore)

            elif score['player_name'] not in WRname:
                totalpoints.append(0) 

        for score in scores:
            if score['player_name'] in TEname:
                TEscore = float(score['points'])
                totalpoints.append(TEscore)
                Tightend.objects.filter(author_id=request.user.id).update(score = TEscore)

            elif score['player_name'] not in TEname:
                totalpoints.append(0) 

        for score in scores:
            if score['player_name'] in Kname:
                Kscore = float(score['points'])
                totalpoints.append(Kscore)
                Kicker.objects.filter(author_id=request.user.id).update(score = Kscore)

            elif score['player_name'] not in Kname:
                totalpoints.append(0) 

        totalscore = sum(totalpoints)

        Team.objects.filter(user=request.user.id).update(teamscore = totalscore)

        
        context = {
            'QB': QB,
            'QBscore': QBscore,
            'RB': RB,
            'RBscore': RBscore,
            'WR': WR,
            'WRscore': WRscore,
            'TE': TE,
            'TEscore': TEscore,
            'K': K,
            'Kscore': Kscore,
            'totalscore': totalscore,
            'myteamname': myteamname
        }

        return render(request,"game/show.html", context) 

    else:
        return redirect('login') 



def playerchoose(request):

    user = request.user
    team_form = Teamform(request.POST)
    teamname = ''

    QBpage = []
    RBpage = []
    WRpage = []
    TEpage = []
    Kpage = []

    if user.is_authenticated:

        if 'teamname' in request.POST:
            
            if team_form.is_valid():
                instance = team_form.save(commit=False)
                instance.user = request.user
                instance.save()  
      
    
    url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerGameStatsByWeek/2019/6?key=c3df3464e99245a6a7970f51c008cbee'
 
    r = requests.get(url.format()).json()
    
    player_data = []
    
    for i in r:
        player_info = {
            'player_id' : i['PlayerID'],
            'player_name' : i['Name'],
            'team' : i['Team'],
            'position': i['Position'],
            'points': i['FantasyPoints']
        }

        player_data.append(player_info)

    for p in player_data:
        if 'QB' in p['position']:
            QBpage.append(p)
        
        elif 'RB' in p['position']:
            RBpage.append(p)

        elif 'WR' in p['position']:
            WRpage.append(p)

        elif 'TE' in p['position']:
            TEpage.append(p)

        elif 'K' in p['position']:
            Kpage.append(p)

    Kform = Kickerform(request.POST, prefix="kick")
    TEform = Tightendform(request.POST, prefix="tight")
    WRform = Widereceiverform(request.POST, prefix='wide')
    QBform = Quarterbackform(request.POST, prefix='quarter')

    if 'quarterback' in request.POST:
        if QBform.is_valid():
            instance = QBform.save(commit=False)
            instance.author = request.user
            instance.save()  
            messages.add_message(request, messages.SUCCESS, "Quarterback added")
        RBform = Runningbackform(prefix='running')
        
    elif 'runningback' in request.POST:
        RBform = Runningbackform(request.POST, prefix='running')
        if RBform.is_valid():
            instance = RBform.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Running Back added")
            
        QBform = Quarterbackform(prefix='quarter')

    elif 'widereceiver' in request.POST:
        WRform = Widereceiverform(request.POST, prefix="wide")
        if WRform.is_valid():
            instance = WRform.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Wide Receiver added")
            
        QBform = Quarterbackform(prefix='quarter')
        RBform = Quarterbackform(prefix='running')

    elif 'tightend' in request.POST:
        TEform = Tightendform(request.POST, prefix="tight")
        if TEform.is_valid():
            instance = TEform.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Tightend added")
            
        QBform = Quarterbackform(prefix='quarter')
        RBform = Quarterbackform(prefix='running')
        TEform = Tightendform(prefix='tight')

    elif 'kicker' in request.POST:
        Kform = Kickerform(request.POST, prefix="kick")
        if Kform.is_valid():
            instance = Kform.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Kicker added")
            
        QBform = Quarterbackform(prefix='quarter')
        RBform = Quarterbackform(prefix='running')
        TEform = Tightendform(prefix='tight')
        Kform = Kickerform(prefix='kick')
        

    else: 
        WRform = Widereceiverform(prefix='wide') 
        QBform = Quarterbackform(prefix='quarter')
        RBform = Runningbackform(prefix='running')
        TEform = Tightendform(prefix='tight') 
        Kform = Kickerform(prefix='kick') 


    context = {'player_data': player_data,
               'QBform': QBform,
               'RBform': RBform,
               'WRform': WRform,
               'TEform': TEform,
               'Kform': Kform,
               'team_form': team_form,
               'QBpage': QBpage,
               'RBpage': RBpage,
               'WRpage': WRpage,
               'TEpage': TEpage,
               'Kpage': Kpage          
    }
    
    return render(request,'game/form.html', context)



def delete_QB(request, id):
    QB = Quarterback.objects.get(id=id)
    QB.delete()
    return redirect('show')


def delete_RB(request, id,):
    RB = Runningback.objects.get(id=id)
    RB.delete()
    return redirect('show')


def delete_WR(request, id):
    WR = Widereceiver.objects.get(id=id)
    WR.delete()
    return redirect('show')

def delete_TE(request, id):
    TE = Tightend.objects.get(id=id)
    TE.delete()
    return redirect('show')

def delete_K(request, id):
    K = Kicker.objects.get(id=id)
    K.delete()
    return redirect('show')



def teamscores(request, id):

    team = Team.objects.get(id=id)

    totalscore = 40

    url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerGameStatsByWeek/2019/6?key=c3df3464e99245a6a7970f51c008cbee'

    r = requests.get(url.format()).json()

    scores = []

    for i in r:
        player_info = {
            'player_id' : i['PlayerID'],
            'player_name' : i['Name'],
            'points': i['FantasyPoints']
        }

        scores.append(player_info)

    context = {
        'totalscore': totalscore
    }
    
    return render(request, 'game/scoreboard.html', context)



def scoreboard(request):

    allteams = Team.objects.all()
    
    for i in allteams:
    
        context = {'allteams': allteams}

        return render(request, 'game/scoreboard.html', context)


def editname(request):

    user = request.user
    

    if user.is_authenticated:

        if request.method == 'POST':
            Team.objects.filter(user=request.user.id).update(team_name = request.POST.get('teamname'))

        team_name = Team.objects.filter(user=request.user.id)

        return render(request, 'game/editname.html')


def createteamname(request):

    user = request.user

    team_form = Teamform(request.POST)
    teamname = ''

    if user.is_authenticated:
        if 'teamname' in request.POST:
            if team_form.is_valid():
                instance = team_form.save(commit=False)
                instance.user = request.user
                team_name = Team.objects.filter(user=request.user.id)
                
                instance.save()

            if request.method == 'POST':
                Team.objects.filter(user=request.user.id).update(team_name = request.POST.get('teamname'))
                team_name = Team.objects.filter(user=request.user.id)

                return redirect('show')

    #if request.method == 'POST':
            #Team.objects.filter(user=request.user.id).update(team_name = request.POST.get('teamname'))

            #team_name = Team.objects.filter(user=request.user.id)

            #return render(request, 'game/editname.html')

    context = {
        'team_form': team_form
    }

    return render(request, 'game/createname.html', context)