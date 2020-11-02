# Final project  of the course  [CS50's Web Programming with Python and JavaScript at Harvard University](https://cs50.harvard.edu/web/2020/) Capstone

## PATAGONIA HIKING CLUB
On this web application the users can register to the club and book their place for a guided hiking in diferent places of PATAGONIA.

The hiking's can only be handled by the administrator, 
each hiking created in the **Hiking** model contains: title (name of the hiking), location, levels, a short and long description, an URL img, and URL map location who is rendered in the template of each hiking, and status; the admin is who receives the information if the trail is available or not. 
The user navigate through all the hiking's, is able to filter by location and level. Then open and read the information about it, open the map of the location, read other reviews and make their own comment about it (comments reviews are stored in the **Comment** model). In this section also have a button for add remove to a favorite list for each user stored in the **Favourite** model. If the user decide to do a booking just need to press the button "BOOK NOW" and it will be rendered a form using **django forms** to fill with name, lastname, a data to go, and provide a phone number. This information will be stored in the **Booking** model. Then serialized to a **JSON address API**, make a request to be rendered in "my bookings" section and also this information can be used by third parties, such as guides,providing all the information about the booking.

The web application is fully mobile-responsive, highlights and challenging for me in this project was; find a way to do a double search filter, create favorites, render a map using a django models variable, and a greater effort in terms of styling with CSS to make it more human-friendly, some details on the handling of the DOM with javascript and the manipulation of data after being serialized.

## Requirements to run the code

* Install python and pip.
* After pip was installed, run
    
    ````
    python -m pip install Django
    ````
    ````
    pip3 install markdown2
    ````
* In the root folder, execute 
    ````
    python manage.py runserver"
    ````

## Watch this project in action 
(https://youtu.be/Kb9K_qhOgC8)
