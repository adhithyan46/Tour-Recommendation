# Tour Recommendation.
https://adhithyan.pythonanywhere.com/.

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


## Index page
![index](https://github.com/user-attachments/assets/422d9a21-ce17-4a09-a6c5-bebe3469a964)
## About Us page
![aboutus](https://github.com/user-attachments/assets/00fb2d67-9d9f-4ebb-849c-38b2c578b29d)
## Login page
![login](https://github.com/user-attachments/assets/b73bceb1-f22b-47f6-a667-fdbd874e4495)
## Profile page
![profile](https://github.com/user-attachments/assets/9cffe4d0-e481-491f-85fb-1e5cb17295b1)
## Register page
![register](https://github.com/user-attachments/assets/c2fc786d-bc36-4c89-98d2-dd79516218db)
## Search page
![search](https://github.com/user-attachments/assets/269ef277-b676-45f1-86b5-030db4218e0c)
