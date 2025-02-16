
from django.shortcuts import redirect, render
  

from base.forms import EditProfile
from base.models import *

from base.forms import *

from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register_page(request):
     
     register_form=CustomUserCreationForm()
     if request.method=='POST':
         register_form=CustomUserCreationForm(request.POST)
         if register_form.is_valid():
            username=register_form.cleaned_data.get('username').lower()
            
            if User.objects.filter(username=username).exists():
                 messages.error(request,"username already exist")
            
            else:
             user=register_form.save(commit=False)
             user.username=user.username.lower()
             user.save()
             messages.success(request,"You have been registered successfully. Login now..")
             return redirect("login")
         
         else:
            messages.error(request, "There was an error with your registration. Please try again.")

     context={'register_form':register_form}
     return render(request,"auth/register.html",context)





def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        print(username,password)


        try:
            
            user=User.objects.get(username=username)

        except:

            messages.error(request,"user doesnot exist")
        
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Login success")
            return redirect('home')
        

        
        else:
            messages.error(request,"username or password doesnot matched.")



    context={}
    return render(request,"auth/login.html",context)


def logout_page(request):
        messages.success(request,"You are successfully logout")
        logout(request)
        


        context={}
        return redirect('home')

@login_required
def profile(request,pk):
    
    profile=User.objects.get(id=pk)
    rooms=profile.room_set.all()
    recent_messages=profile.message_set.all()
    topics=Topic.objects.all()

    context={'profile':profile,'rooms':rooms,'recent_messages':recent_messages,'topics':topics}






    return render(request,"user/profile.html",context)


def editprofile(request,pk):
    user=User.objects.get(id=pk)
    
   
    form=EditProfile(instance=user)


    if request.method=='POST':
        print("Request files : ",request.FILES)
        print("Request post : ",request.POST)

        if request.user.id==user.id:

            form=EditProfile(request.POST,request.FILES,instance=user)

            if form.is_valid():
                username=form.cleaned_data['username'].lower()
            
                if User.objects.filter(username=username).exclude(id=user.id).exists():
                        print("username already exist")
                        messages.error(request,"username already exist")
                    

                else:    
                            
                        user=form.save(commit=False)
                        if not request.FILES.get('pic') and not user.pic:
                            user.pic = None
                        user.save()
                        messages.success(request, "Profile updated successfully.")
                        return redirect('profile',pk=user.id)
            
            else:
                messages.error(request, "Invalid form data. Please correct the errors and try again.")  
                    

        else:
            messages.error(request,"You are not authorized to edit this profile.")
            return redirect('profile',pk=user.id)
        
        



    context={'form':form}
    return render(request,"user/edit-profile.html",context)

