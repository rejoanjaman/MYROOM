
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import UserProfile, Location



User = get_user_model()

def home(request):
    return render(request,"home.html")




def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        mobil_no = request.POST.get("mobil_no")
        password = request.POST.get("password")

       
        user = User.objects.login(email=email, mobil_no=mobil_no, password=password)

        return {"message": "User successfully created", "user_id": user.userid}

    return render(request, "login.html")

@login_required  
def create_user_profile(request):
    if request.method == 'POST':
        
        profile_name = request.POST.get('profile_name')
        profile_img = request.FILES.get('profile_img')
        mobile_no = request.POST.get('mobile_no')
        business_type = request.POST.get('business_type')
        owner_name = request.POST.get('owner_name')
        total_room = request.POST.get('total_room')
        room_rent = request.POST.get('room_rent')
        description = request.POST.get('description')

        
        try:
            UserProfile.objects.create(
                userid=request.user,
                profile_name=profile_name,
                profile_img=profile_img,
                mobile_no=mobile_no,
                business_type=business_type,
                owner_name=owner_name,
                total_room=total_room,
                room_rent=room_rent,
                description=description
            )
            messages.success(request, "Profile created successfully!")
            return redirect('home') 
        except Exception as e:
            messages.error(request, f"Error creating profile: {e}")

    return render(request, 'from.html')  

