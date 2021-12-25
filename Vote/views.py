from django.shortcuts import render,redirect,Http404
from django.http import HttpResponse
from .models import Contact,Votes,Member,Notice
from .forms import createvoteform
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.

def signin(request):
    if request.method== 'GET':

        if 'action' in request.GET:
            action=request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return render(request,'signin.html')

        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())
            print(request.session.get_expiry_date())

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if Member.objects.filter(name=username, password=password):
            request.session['username'] = username
            print(username)
            print('Login succesfull')
            vote = Votes.objects.all()
            context = {'vote': vote,
                       'username': username}
        else:
            return HttpResponse('Invalid Username and Password')
        return render(request, 'index.html', context)
    return render(request, 'index.html')




def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password1', '')
        if (password != password2):
            return HttpResponse( " Passwords do not match please try again")
            return redirect('/register')
        member = Member(name=name, email=email, password=password)
        member.save()
        submit = True
        return redirect('/signin/?action=logout')
    return render(request,'register.html')




def index(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        vote = Votes.objects.all()
        context={'vote':vote,
                 'username':username}
    else:
        return redirect('/signin/?action=logout')
    return render(request,'index.html',context)





def voteresult(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        vote = Votes.objects.all()
        context={'vote':vote,
             'username':username}
    else:
        return redirect('/signin/?action=logout')
    return render(request,'voteresult.html',context)





def vote(request,vote_id):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        poll = Votes.objects.get(pk=vote_id)
        if request.method == 'POST':
            print(request.POST['poll'])
            selected_option=request.POST['poll']
            if selected_option == 'option1':
                poll.option_one_count +=1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1
            elif selected_option == 'option4':
                poll.option_four_count += 1
            poll.save()
            submit = True
            return render(request, 'vote.html', {'submit': submit})
        context={'poll':poll,
                 'username':username}
    else:
        return redirect('/signin/?action=logout')
    return render(request,'vote.html',context)




def notice(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        myposts = Notice.objects.all()
        context = {'username': username,
                   'myposts':myposts}

    return render(request,'notice.html',context)


def blogpost(request,id):
    post=Notice.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blogpost.html',{'post':post})





def create(request):
    if request.method == 'POST':
        form = createvoteform(request.POST, request.FILES)
        print('just')
        if form.is_valid():
            print('validated')
            form.save()
            print('done')
            return redirect('/')
    else:
        print('ERROR')
        form = createvoteform()
    context = {'form' : form}
    return render(request, 'create.html', context)





def result(request,vote_id):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        poll = Votes.objects.get(pk=vote_id)
        if poll.option_one_count > poll.option_two_count and poll.option_one_count > poll.option_three_count and poll.option_one_count > poll.option_four_count:
            option1= poll.option_one
        elif poll.option_two_count > poll.option_one_count and poll.option_two_count > poll.option_three_count and poll.option_two_count > poll.option_four_count:
            option1= poll.option_two
        elif poll.option_three_count > poll.option_one_count and poll.option_three_count > poll.option_two_count and poll.option_three_count > poll.option_four_count:
            option1= poll.option_three
        elif poll.option_four_count > poll.option_one_count and poll.option_four_count > poll.option_two_count and poll.option_four_count > poll.option_three_count:
            option1= poll.option_four
        else:
            option1 = 'ITS A TIE'
        context = {'poll': poll,
                   'msg':option1,
                   'username':username}
    else:
        return redirect('/signin/?action=logout')
    return render(request,'result.html',context)





def ongoingvote(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        vote=Votes.objects.all()
        context={'vote':vote,
                 'username':username}
    else:
        return redirect('/signin/?action=logout')
    return render(request, 'ongoingvote.html',context)





def contact(request):
    if 'username' in request.session:
        username = request.session['username']
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            desc = request.POST.get('message', '')
            print(name, email, phone, desc)
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            submit = True
            return render(request, 'contact.html', {'submit': submit,'username':username})
    return render(request,'contact.html',{'username':username})