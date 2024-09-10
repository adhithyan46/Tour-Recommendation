from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from . forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
import pandas as pd
from .models import Tour,UserProfile
from django.contrib.auth.decorators import login_required



# from django.template import loader
def index(request):
    return render(request,'index.html')
def login_page(request):
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the search page
        return redirect('search_page')
    
    # Add an entry message when the user visits the login page
    messages.info(request, 'Please login to access your account.')

    if request.method == 'POST':       
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('search_page')
            else:
                # Display an error message if authentication fails
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Invalid form submission. Please check your input.')        
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})

def register_page(request):
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the search page
        return redirect('search_page')
    messages.info(request, 'Please login to access your account.')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['type']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            
            UserProfile.objects.create(user=user , type=user_type)
            
            
            

           
            return redirect('login_page')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()
    return render(request, 'register_page.html', {'form': form})

def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login_page')  # Redirect to the login page after logout

def tour_recommend(user_profile, filtered_tours):
    # Filter based on interests
    recommended_tours = filtered_tours.copy()

    # Initialize Score column
    recommended_tours['Score'] = 0
    
    for interest in user_profile['type']:
        recommended_tours['Score'] += recommended_tours['Description'].str.contains(interest, case=False).astype(int)
    
    # Sort the tours by the score
    recommended_tours = recommended_tours.sort_values(by='Score', ascending=False)
    
    return recommended_tours

@login_required(login_url='login_page') 
def search_page(request):
    
    # Read the CSV file with the tour data
    csv_file_path = 'myapp/dataset/tour_data.csv'
    tour_data = pd.read_csv(csv_file_path)
    
    tour_data['Description'] = tour_data['type'].astype(str) + ' ' + tour_data['place'].astype(str)
    
    # Convert the DataFrame into a list of dictionaries
    tour_data = tour_data.to_dict(orient='records')

    # Fetch all the Tour objects that include images uploaded via the admin
    tours = Tour.objects.all()
    
    # Create a dictionary for quick lookup of images by place name
    tour_images = {}
    for tour in tours:
        # Only add images if they exist
        if tour.image:
            tour_images[tour.place] = tour.image.url

    # Add image URLs to the tour_data records if a match is found
    for t in tour_data:
        if t['place'] in tour_images:
            t['image_url'] = tour_images[t['place']]
    
    search_query = request.GET.get('search', '')
    if search_query:
        filtered_tours = [tour for tour in tour_data if search_query.lower() in tour['place'].lower()]
    else:
        filtered_tours = tour_data
    
    try:
        # Fetch user profile to get actual interests
        user_profile = UserProfile.objects.get(user=request.user)
        type = user_profile.type.split(',') if user_profile.type else []
    except UserProfile.DoesNotExist:
        # Handle case where UserProfile does not exist
        type = []
        messages.warning(request, "Your profile is incomplete. Please update your profile.")

    user_profile = {
        'type': type,
    }
    

    # Get recommendations
    recommendations = tour_recommend(user_profile, pd.DataFrame(filtered_tours))
    
    # Convert to list of dictionaries
    recommendation_list = recommendations.to_dict('records')
    
    
    # Render the search_page.html template, passing the combined data
    return render(request, 'search_page.html', {'tour_data': recommendation_list})

@login_required(login_url='login_page')
def profile_page(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'profile_page.html', {'user': request.user, 'user_profile': user_profile})

def about_page(request):
    return render(request, 'about_page.html')