# Tour Recommendation
A Django-based web application that provides personalized tour recommendations based on user interests, ratings, and location types. This system uses machine learning algorithms and a custom dataset to suggest tourist destinations.
## Features
* User Registration and Login: Users can create an account, log in, and update their profiles.
* User Profile Management: Each user has a profile that includes their name, email, and preferred location type.
* Search Functionality: Users can search for tourist destinations based on their interests.
* Personalized Recommendations: The system recommends destinations based on user interests using machine learning techniques such as TF-IDF and cosine similarity.
* Responsive Design: The application features a responsive design that works well on various devices.
* Admin Management: Admins can upload destination images and manage tour data through the Django admin panel.
## Dataset
1. city: Name of the city.
2. place: Tourist attraction.
3. rating: User rating for the place.
4. type: Category of the place (e.g., Temple, Lake, Garden, Park).
## Usage
1. Register: Create a new account and provide your details, including your preferred location type.
2. Search: Use the search page to find destinations based on location, and get recommendations tailored to your interests.
3. Profile Management: Update your profile with your preferred location type, and the system will provide personalized recommendations.
## Customization
* Adding New Data: You can add new tourist destinations by updating the tour_data.csv file or by using the Django admin panel.
* Modifying Interests: You can adjust the interests and recommendation logic in the tour_recommend() function inside views.py.

├── myapp/
│   ├── dataset/
│   │   └── tour_data.csv  # Dataset used for recommendations
│   ├── migrations/
│   ├── models.py          # Database models (Tour, UserProfile, Interest)
│   ├── views.py           # Core views (Search, Profile, Registration, Login)
│   ├── templates/
│   │   ├── base.html      # Base template for the project
│   │   ├── profile_page.html  # User profile template
│   │   ├── search_page.html   # Search and recommendation page
│   │   └── login_page.html    # Login page template
│   └── forms.py           # Django forms (SignupForm, LoginForm)
├── static/
│   └── css/
│       └── style.css      # Custom CSS for the application
├── manage.py              # Django management commands
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

