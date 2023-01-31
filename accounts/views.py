from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from contacts.models import Contact
from .models import Profile


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .forms import ProfileForm, form_validation_error

# Create your views here.
def dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)
    # user_contacts = Contact.objects.filter(user_id = request.user.id).order_by('-contact_date')

    context = {
        # 'contacts': user_contacts,
        'profile': profile,
    }
    return render(request,'accounts/dashboard.html',context)

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username,password = password)

       if user:
          auth.login(request,user)
          messages.success(request,"You are now logged in.")
          return redirect('home_index')
       else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')       
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect("home_index")

def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,"That username is taken.")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"That email is taken.")
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name)
                    user.save()
                    # Login after register
                    auth.login(request,user)
                    messages.success(request,"You are now logged in.")
                    return redirect('edit-profile')

        else:
            messages.error(request,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')




# PROFILE

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'accounts/edit-profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Changes saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('dashboard')



