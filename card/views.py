from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  CreateUserForm
# Create your views here.
def home(request):
 
    context = {}   
    return render(request, 'flashcards/index.html', context)



def registerPage(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
          
            messages.success(request, 'account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'flashcards/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('flashcard')
        else:
                messages.info(request,'Username or password is incrorrect')
    context = {}
    return render(request, 'flashcards/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('home')
def flashcards(request):
    '''
    Renders the flashcard app's flashcards.html template
    '''
    # Card_Set.objects.all() returns all cards in the database
    # topic_query_set = Card_Set.objects.all().order_by('topic').filter(is_active = True)
    context = {}   # Dictionary{} rendered for flashcards/flashcards.html
    return render(request, 'flashcards/flashcard.html', context)
