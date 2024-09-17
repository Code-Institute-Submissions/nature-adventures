# Nature Adventures

Luonto is a website designed to allow people to share information about their favourite hiking routes with others.

The website aims to encourage people encourage each other to go outdoors by sharing advice and informatio with each other. Registered users of the website vote the routes to indicate to other users which routes they have liked. 

Visit the deployed site [here](https://nature-adventures-b39f8380b4ce.herokuapp.com/)

## Table of Contents

## User Experience (UX)

### Project Goals

* The website creates a sense of adventure and encourages people to get outdoors.
* The website is responsive and can easily be used on different devices.
* The style and structure of the website is consistant to allow user to navigate the website easily
* Users are able to create a profile to encourage the users to get to know each other. 

### User Stories

Excel spreadsheet was used to collect epics and user stories before development was started. Four Epics were identified to help to organise the work: 1. User Profiles, 2. Routes, 3. Managing Routes and 4. Interacting with Routes. These Epics were broekn down into user stories with clearly definied Acceptance Criteria, Story Points and MoSCoW prioritisation. 

![All User Stories](assets/readme_files/user_stories/user-stories-all.png)

Before development was started the User Stories were transferred to GitHub projects that was used as a Kanban board to track user stories and the progress made.

| After Iteration 1 | After Iteration 2 | After Iteration 3 |
| ---               |  ---              |  ---              |
|![User Stories - Iteration 1](assets/readme_files/user_stories/User-stories-Iteration-1.png)|![User Stories - Iteration 2](assets/readme_files/user_stories/User-stories-iteration-2.png)|![User Stories - Iteration 3](assets/readme_files/user_stories/user-stories-iteration-3.png)|


### Database Model

### Wireframes

[Balsamiq](https://balsamiq.com/) User Interface wireframing tool was used to design the structure of the website.

| Feature       | Wireframe |
| ---           | ---       |
| List of hikes | ![Hikes List](assets/readme_files/wireframes/wireframes_hikes_list.png)|
| Detail view   | ![Hike detail](assets/readme_files/wireframes/wireframes_hike_detail.png)|
| Add a Hike    | ![Add a Hike](assets/readme_files/wireframes/wireframes_add_hike.png)|
| Edit a Hike   | ![Edit a Hike](assets/readme_files/wireframes/wireframes_edit_hike.png)|
| Delete a Hike | ![Delete a Hike](assets/readme_files/wireframes/wireframes_delete_hike.png)|
| View Profile  | ![View Profile](assets/readme_files/wireframes/wireframes_profile.png)|
| Edit Profile  | ![Edit Profile](assets/readme_files/wireframes/wireframes_edit_profile.png)|

### Colour Scheme

### Typography

The main font used is Raleway with sans serif as the backup font. The font used for heading and the logo is Playpen Sans with cursive as the backup font. 

[Back to top](#nature-adventures)

## Features

### General

* The website was designed following mobile first and responsive design principles.
* The navigation bar is consistent across all the pages allowing the user to navigate the site easily. The navigation bar contains Nature Adventure's logo and links to all the sections. 
* The footer also is the same on all the pages and allows users to easily access Nature Adventure's social media sites. 

### Hikes

* The Home page displays a paginated list of all the hikes that have been added to the site.
* The hikes are displayed in the order of total likes received. The hike that has received the most likes is displayed first. 
* All the users can see basic information about the hikes including the name, distance, region and the total number of likes the hike has received.
* Non-registred users are encouraged to login or sign up to be able to use other functionalities.
* Registered users are displayed a link to their own profile and the page to add more hikes.

### Hike detail

* If non-registered user attempts to access the hike details, they are advised to login or sign up. 
* Registered users are able to view all the hike details including name, distance, region, author, date created, number of likes and which users have liked the hike.
* The user who created the hike also has "Edit" and "Delete" buttons to allow them to manage their hikes.
* All registered users other than the author of the hike are able to like/unlike the hike. It is displayed above the hike button if the user has already liked the hike. 
* A list of all users who have liked the hike is displayed as a Bootstrap popover.

### Edit hike

* Edit hike page allows the author of the hike to make edits to the information that they has added.
* The current information about the hike has been prefilled for the ease of use. 

### Delete hike

* Delete hike button opens a delete hike modal that confirms that the user really wants to delete the hike. 

### Create a hike

* Create hike form allows registered users to share their knowledge by add new hiking routes.

### Profile page

* Registered users can view their own profiles as well as the profiles of other registered users.
* In addition to username, region and description, the hikes that the user has created and liked are also displayed.

### Edit profile

* Users can edit their own profile to ensure that their information is up-to-date. 

### Authentication pages

* The registeration page allows new users to sign up and create a profile for the site.
* The login page allows registered users to sign in using their login details.
* The logout page allows registered users to sign out. 

## Testing

### Testing user stories

### Code validation

* The [W3C Markup Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and [JSHint](https://jshint.com/) were used to validate the HTML, CSS and JS code to ensure that the project meets the current Web Standards and is free from any unintended syntax errors and mistakes that could cause issues with accessibility and usability.

* W3C Markup Validator:
    * highlighted that when creating a Bootstrap popover to display the people who had liked the hike, a link element had been used instead of a button element. The link element was replaced with a button element. 
    * highlighted that several closing div elements were missing. There were added to fix the errors.
    * highlighted that the form elements had empty "action" attributes. Links to the appropriate URLs were added to fix these errors.
    * highlighted that several trailing slashes. These were ignores as they have added by Cloudinary.

    | Page          | Feedback                                                                      |
    | ---           | ---                                                                           |
    | Hikes list    | ![hikes list](assets/readme_files/validation/hikes_list_validation.png)       |
    | Hike info     | ![hike detail](assets/readme_files/validation/hike_info_validation.png)       |
    | Create a hike | ![create a hike](assets/readme_files/validation/create_hike_validation.png)   |
    | Edit a hike   | ![edit a hike](assets/readme_files/validation/edit_hike_validation.png)       |
    | Profile       | ![profile](assets/readme_files/validation/profile_validation.png)             |
    | Edit profile  | ![edit profile](assets/readme_files/validation/update_profile_validation.png) |
    | 404           | ![404 page](assets/readme_files/validation/404_validation.png)                |

* W3C CSS Validator:
    * highlighted that "right" is not a value of the property "align-items". This was fixed by replacing "right" with the value "start".

    ![CSS validation](assets/readme_files/validation/css_validation.png)

* JSHint:
    * highlighted that some semicolons were missing. These were added.
    * highlighted that "popover" and "bootstrap" are not used. These were ignore as they are part of the Bootstrap popover code.

    ![JS validation](assets/readme_files/validation/js_validation.png)

* [autopep8](https://pypi.org/project/autopep8/), [Flake8](https://flake8.pycqa.org/en/latest/) and [CI Python Linter](https://pep8ci.herokuapp.com/#) were used to validate the Python code for PEP8 requirements.

### Performance and Accessibility

Chrome DevTool Lighthouse was used to assess the project's performance and accessibility. The reports confirmed that the page performs well and is accessible. The recommadations relating to Best Practice noted that because of Cloudinary the site is using third party cookies.

| Page tested   | Report                                                                        |
| ---           | ---                                                                           |
| Hikes list    | ![hikes list](assets/readme_files/lighthouse/hike_list_lighthouse.png)        |
| Hike info     | ![hike detail](assets/readme_files/lighthouse/hike_info_lighthouse.png)       |
| Create a hike | ![create a hike](assets/readme_files/lighthouse/create_hike_lighthouse.png)   |
| Edit a hike   | ![edit a hike](assets/readme_files/lighthouse/update_hike_lighthouse.png)     |
| Profile       | ![profile](assets/readme_files/lighthouse/profile_lighthouse.png)             |
| Edit profile  | ![edit profile](assets/readme_files/lighthouse/update_profile_lighthouse.png) |
| Register      | ![register](assets/readme_files/lighthouse/register_lighthouse.png)           |
| Login         | ![login](assets/readme_files/lighthouse/login_lighthouse.png)                 |
| Logout        | ![logout](assets/readme_files/lighthouse/logout_lighthouse.png)               |


### Responsiveness

In addition to manual checks, responsiveness was tested further using Chrome DevTools and Responsive Design Checker.

### Manual testing

#### Browser compatibility

| Browser          | Outcome                                                                                                                                                          | Pass/Fail |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Google Chrome    | No appearance, responsiveness nor functionality issues.                                                                                                          | Pass      |
| Mozilla Firefox  | The Game Mode label was displayed over two lines. <br>The label length was increased by 5px to resolve this issue.<br>No responsiveness nor functionality issues | Pass      |
| Microsoft Edge   | No appearance, responsiveness nor functionality issues.                                                                                                          | Pass      |
| Samsung Internet | No appearance, responsiveness nor functionality issues.                                                                                                          | Pass      |

#### Device compatibility

| Device                 | Outcome                                                 | Pass/Fail |
| ---------------------- | ------------------------------------------------------- | --------- |
| Sony Xperia 10 III     | No appearance, responsiveness nor functionality issues. | Pass      |
| Samsung Galaxy A55     | No appearance, responsiveness nor functionality issues. | Pass      |
| Lenovo Yoga s730       | No appearance, responsiveness nor functionality issues. | Pass      |
| Sony VAIO 15"          | No appearance, responsiveness nor functionality issues. | Pass      |
| Dell P2419H 24" screen | No appearance, responsiveness nor functionality issues. | Pass      |
| Samsung Galaxy Tab S4  | No appearance, responsiveness nor functionality issues. | Pass      |

#### Common Elements Testing


### Unit testing

## Technologies Used

### Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries and Frameworks used

* [Django](https://www.djangoproject.com/) web framework was used to develop the site.

* [Django Template](https://jinja.palletsprojects.com) was used as a templating language for Django.

* [Google Fonts](https://fonts.google.com) was used to import the fonts used.

* [Font Awesome](https://fontawesome.com) was used to add icons such as social media icons and the "like" icon.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used throughout the website to improve responsiveness and styling.

### Packages / Dependecies installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/) was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/) was used as the Python Web Server Gateway Interface (WSGI) HTTP server. 

* [Cloudinary](https://cloudinary.com/) was used as the image management solution.

* [Whitenoise](https://pypi.org/project/whitenoise/) was used to serve static files.

### Database Management

* [Postgres](https://www.postgresql.org/) object-relational database system was used in production.


https://learndjango.com/tutorials/django-slug-tutorial

## Credits: 

- default hiking image: Photo by Guduru Ajay bhargav: https://www.pexels.com/photo/people-walking-on-road-near-trees-at-daytime-photo-1076081/
- default hiking image 2: Photo by Eric Sanman: https://www.pexels.com/photo/group-of-person-walking-in-mountain-1365425/
- Seven Sisters: Photo by Andras Stefuca: https://www.pexels.com/photo/seven-sisters-sussex-england-17568779/
- background image: Photo by Markus Spiske: https://www.pexels.com/photo/light-landscape-nature-forest-117843/
- Snowdon: Photo by Julien Goettelmann: https://www.pexels.com/photo/scenic-panorama-of-a-mountain-lake-snowdon-wales-uk-12021273/
- Lake District (Helvellyn): Photo by T6 Adventures: https://www.pexels.com/photo/lake-wast-water-in-wasdale-valley-part-of-lake-district-national-park-18671162/
- surrey: Photo by Ollie Craig: https://www.pexels.com/photo/ancient-gothic-tower-located-on-hill-surrounded-by-green-trees-5344943/
- compass: Photo by Supushpitha Atapattu: https://www.pexels.com/photo/round-grey-and-black-compass-1736222/

- profile pic - hiker123 : Photo by mohamed abdelghaffar: https://www.pexels.com/photo/man-in-black-jacket-771742/
- profile pic - admin: Photo by George Dolgikh: https://www.pexels.com/photo/woman-taking-selfie-while-smiling-1310522/
- profile pic - vaeltaja: Photo by Italo Melo: https://www.pexels.com/photo/portrait-photo-of-smiling-man-with-his-arms-crossed-standing-in-front-of-a-wall-2379004/
- profile pic - user1 : Photo by Christina Morillo: https://www.pexels.com/photo/woman-standing-near-whiteboard-1181519/
- profile pic: Photo by Anna Nekrashevich: https://www.pexels.com/photo/photo-of-man-wearing-eyeglasses-6801642/

-Favicon: <a href="https://www.freepik.com/icon/compass_10507707#fromView=search&page=2&position=33&uuid=8f47f99c-0454-4226-bf39-8848ce14fd41">Icon by Smashicons</a>

<a href="https://www.freepik.com/free-photo/crop-hand-with-compass-nature_2415325.htm#fromView=search&page=1&position=47&uuid=66f2ab65-d34d-4178-990c-bc72d2c66713">Image by freepik</a>

<a href="https://www.freepik.com/free-vector/flat-design-sport-silhouette_65686980.htm#fromView=search&page=1&position=9&uuid=9fad7fc0-9ade-4f98-8fae-b41f0a5853fd">Image by freepik</a>

###Credits:

automatically create profile:
# How to create profile automatically using signals taken from:
# https://www.youtube.com/watch?v=H8MmNqDyra8&list=
# PLCC34OHNcOtoQCR6K4RgBWNi3-7yGgg7b&index=3

how to create a profile:
# Inspiration taken from:
# https://dev.to/earthcomfy/django-user-profile-3hik
# and https://www.youtube.com/watch?v=KNvSWubOaQY

