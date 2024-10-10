# Latte Night Cafe
![latte-night-cafe-homepage](https://github.com/user-attachments/assets/27505868-c322-4143-a2f2-5e075b777417)


## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [UX/UI](#uxui)
- [Site Goals](#site-goals)
- [User Stories](#user-stories)
- [Initial Planning Stage - Wireframes](#initial-planning-stage---wireframes)
  - [Desktop](#desktop)
  - [Mobile](#mobile)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Testing and Debugging](#testing-and-debugging)
  - [Validator Testing](#validator-testing)
  - [Bugs Fixed](#bugs-fixed)
- [Setup and Running the Application](#setup-and-running-the-application)
- [Deployment](#deployment)
- [Credits](#credits)

## Introduction

This is a table booking system for Latte Night Cafe, a late night cafe. Usually only clubs or pubs are open after dark, but not everyone is a party animal. This is a venue for the night owls who want to relax with their friends, or even get some work done, in at a calm and cosy place during the twilight hours. Offering customers the chance to book a space allows them to secure a quiet nook for themselves in the early hours of the morning when traditional cafes are normally closed. It also gives them peace of mind that they're in a safe space away from loud music and alcohol-fuelled antics so they can unwind.


This web application was created and built by Christina Hughes - [GitHub](https://github.com/CHughes13), [LinkedIn](https://www.linkedin.com/in/christina-hughes-50233041/)

***

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Bootstrap 5.3.3
- Django
- [Balsamiq](https://balsamiq.com/) used to create wireframes
- ChatGPT and Blackbox AI used throughout for coding advice and inspiration
- [Miro Board](https://miro.com/app/board/uXjVKrc3AA4=/) (digital interactive whiteboard)
- [Github Project Board](https://github.com/users/CHughes13/projects/2)

![latte-night-cafe-creenshot 2024-08-14 162917](https://github.com/user-attachments/assets/a94a7ee3-7eec-4396-96ad-2aa1be35126b)

[Back to top](#)

***

## UX/UI
### Site Goals
The goal of Latte Night Cafe is to provide a warm, cosy retreat to those who prefer want to visit coffee shops at night. Minimalic and simple, the aim was to make users feel comfortable and at ease.
![latte-night-cafe-creenshot 2024-08-14 163053](https://github.com/user-attachments/assets/0ee3f107-2872-4d03-af8e-7ede1debbffe)
![latte-night-cafe-CAG Contrast checker](https://github.com/user-attachments/assets/d80c3c4f-1b8c-4450-9951-185d300928e7)

The colours are warm and comforting. The main issue with the contrast check was the subtitle here. A text background was added to help it stand out more. This is something that could be altered in the future.

[Back to top](#)

### User Stories
Please see [GitHub project board](https://github.com/users/CHughes13/projects/2/views/1).

## Initial Planning Stage - Wireframes

Here are the initial wireframes for the Latte Night Cafe application (created using Balsamiq), along with screen shots of the initial design. These provide a visual outline of the planned layout and functionality.

#### Desktop
![Screenshot 2024-08-14 164448](https://github.com/user-attachments/assets/7a6456da-7bf4-45a8-b47c-9c1e1f5e6f16)
![Screenshot 2024-08-14 164453](https://github.com/user-attachments/assets/20aaea42-e62c-4cc7-a02a-e8130fef3440)
![Screenshot 2024-08-14 164501](https://github.com/user-attachments/assets/924676c3-d431-41af-9f87-d94210321b46)
![Screenshot 2024-08-14 164507](https://github.com/user-attachments/assets/9c215e4e-e270-452a-bfe9-8fb3304cbbc7)


#### Mobile
![Screenshot 2024-08-14 164512](https://github.com/user-attachments/assets/f5d70693-9488-42a7-a77f-04917c5676c5)

[Back to top](#)

***

## Features
I used the MoSCoW prioritisation method to determine which features were most important and a "must-have" in order to meet the user's needs and achieve a MVP in this initial sprint. 

### Existing Features
- __Navbar changes depends on who is logged in/out__
  - Allows personal experince for user. Keeps unauthorized users away from items they shouldn't have access to.
![latte-night-cafe-creenshot 2024-08-14 140634](https://github.com/user-attachments/assets/ee34f3d0-f160-4552-b32f-def5622d853b)

  
- __Sign In/Out Pages__
  - Easy sign up. Options to include social media itergration in the future.
![latte-night-cafe-creenshot 2024-08-14 142000](https://github.com/user-attachments/assets/4497f444-8348-4b99-bcf9-d7586b414cff)
![latte-night-cafe-creenshot 2024-08-14 141927](https://github.com/user-attachments/assets/78ad74a0-054e-44c6-8fc7-abd0649f8b6f)


- __Text and logo in top corner = return to homepage on a click__ 
  - This button will allow the user to easily navigate back to the homescreen.


- __Responsive Design__ 
  - Responsive design for compatibility with various devices and screen sizes, from mobile to desktop.
![latte-night-cafe-creenshot 2024-08-14 143258](https://github.com/user-attachments/assets/6236ecad-6fff-43db-a27e-25566c634126)
![latte-night-cafe-creenshot 2024-08-14 143313](https://github.com/user-attachments/assets/42c1388a-a116-4761-8cce-579d30257f3c)


- __Footer (see above)__ 
  - Footer section includes links to the relevant social media sites for Latte Night Cafe To allow for easy navigation, the links open in a new tab.
  - Copyright line includes year of publication and the creator. This allows users to see how up to date the information on the web application is.
  - Features at the bottom of the page throughout (and has a matching colour theme with other elements on the site), this lets the user know they're still on the same webpage.
  - The footer is important as it encourages the user to interact and stay connected with Latte Night Cafe on other social media platforms.

- __User Dashboard__ 
  - Where the user can see all their own bookings in one place with full CRUD functionality (create, read, update, and delete) only for their bookings.
  - Includes the option to sort bookings by date.
![latte-night-cafe-user-dashboard](https://github.com/user-attachments/assets/cd16fee4-0fd4-4a5e-80c4-5f91429044a4)

![latte-night-cafe-booking-update-1](https://github.com/user-attachments/assets/d5c953bd-b5be-4734-b78c-7c6928703fdf)

![latte-night-cafe-booking-update-2](https://github.com/user-attachments/assets/7e46ec21-e154-4530-9fd4-ba585f837a31)


- __Admin Dashboard__ 
  - Where the admin can see all the bookings for the cafe in once place. Includes full CRUD functionality (create, read, update, and delete) of all bookings by anyone.
  - Includes the option to sort bookings by date, user, and special requests.
![latte-night-cafe-admin-dashboard](https://github.com/user-attachments/assets/0e0be682-0ad6-4be6-8a60-cc0bb558eba6)

[Back to top](#)


### Features Left to Implement
Using the MoSCoW method, it was determined that these features weren't essential to create a MVP but are more "should-have" and "could-have". Due to time constraintents these features were left out, but they would make great additions to the application in the future.

- __About Page__ - Should Have
  - A more in-depth intro about the cafe and its philosophy to build its brand identiy. Include images of the cafe, staff, food, and drink so future customers know what to expect. Could also include a "How to find us" map. This page would add significant value but at the moment the contact details in the footer cover this.

- __Menu Page__ - Could Have
  - A page listing the food and drink items available, as well as their cost. This allows potential customers to scope out the offerings of the Latte Night Cafe in advance and decide if it's the place for them. Could display this information as a table, list, or PDF/image.
 
- __Reviews__ - Could Have
  - Form for registered users to leave a review of the cafe. These could then be displayed on the homepage as a carousel.
 
- __Social Media Registration/Sign In Option__ - Won't Have (for now)
  - Offer the user the chance to register/sign into the website using one of their social media accounts rather than having to create and remember a new account and password. Would make for a better user experience. At the moment using django's built-in sign up and admin works just fine. More for convienience than a necesaaity.
 
- __Custom Error Screens__ - Won't Have (for now)
  - Currently Django custom error screens are being used for 404, 500, etc. so this feature was not a priority in the first iteration of the project. However, when there is more time, it is definitely more fun to have a personalise and branded error page and you can then direct the user back to the homepage (better UX/UI).  

[Back to top](#)

***

## Testing and Debugging

Created test.py files and constant manual testing throughout.

__Test:__ Create a booking when not logged in.  
__Expectation:__ User will be prompted to log in.  
__Result:__ Pass  
![latte-night-cafe-creenshot 2024-08-14 142000](https://github.com/user-attachments/assets/11b59ef1-eb87-41f5-ab92-edfc9c193ce9)

__Test:__ Create a booking for a date in the past.  
__Expectation:__ User will be prompted select another date.  
__Result:__ Pass  
![latte-night-cafe-creenshot 2024-08-14 141647](https://github.com/user-attachments/assets/06f6113a-67f0-4e7a-80e1-1f3b18b283c2)

__Test:__ Booking appears in user dashboard.  
__Expectation:__ Once booking is made and validated, the user will be redirected to their dashboard which shows all their bookings ever made.  
__Result:__ Pass  
![latte-night-cafe-creenshot 2024-08-14 142847](https://github.com/user-attachments/assets/437db65e-752b-4f73-bdbb-52c98897c5d9)


### Validator Testing

- HTML
  - Passed through the official W3C validator: some errors
![latte-night-cafe-creenshot 2024-08-14 162120](https://github.com/user-attachments/assets/fa72a9ab-204f-44ae-ba03-a07ec26cb3ec)

- CSS
  - Passed through the Jigsaw validator successfully:
![latte-night-cafe-creenshot 2024-08-14 162239](https://github.com/user-attachments/assets/0f7c62f8-7253-4d13-a372-39fe7b02c3e6)

- CI Linter
![latte-night-cafe-creenshot 2024-08-14 162627](https://github.com/user-attachments/assets/ae32c37d-80e7-42aa-802d-87bda868b8f7)
![latte-night-cafe-creenshot 2024-08-14 162744](https://github.com/user-attachments/assets/3ad64a17-a7e8-4e02-ad0e-9e740158ed2c)

![latte-night-cafe-creenshot 2024-08-14 162722](https://github.com/user-attachments/assets/4652a315-4a39-47c3-a331-e3ae4c79c300)
![latte-night-cafe-creenshot 2024-08-14 162657](https://github.com/user-attachments/assets/1c5863a8-eab5-4d07-92e8-ba3b23209447)
![latte-night-cafe-creenshot 2024-08-14 162640](https://github.com/user-attachments/assets/4ef864e6-ab80-4b45-86da-0dea44f920ac)

- Website Optimization
  - Still need to pass through [Google Lighthouse](TBA)

[Back to top](#)

### Bugs Fixed
- __Collapse Navbar when goes into mobile mode__ 
Need to have nav items drop down.

- __Some Font Awesome icons not appearing__ 
The social media icons were appearing, but the speech bubble icons either side of the "Contact us:" text were not. After some investigation, it turns out that the version of Font Awesome that was linked to in the stylesheet was not the same one listed on the icon (different versions of icons have slightly different names and versions).  
![latte-night-cafe-a-icon-not-showing-1](https://github.com/user-attachments/assets/8733f63c-f435-418e-a066-bd2ceec1ae3e)
![latte-night-cafe-a-icon-not-showing-2](https://github.com/user-attachments/assets/9f4c0bb8-2199-4ba1-8431-7f4f10f796a5)
![latte-night-cafe-a-icon-not-showing-3](https://github.com/user-attachments/assets/c401f7ca-0de9-4d92-b1dc-14219bc87a93)
![latte-night-cafe-a-icon-not-showing-4](https://github.com/user-attachments/assets/194a277b-64e4-4454-9998-ee40495ee620)


[Back to top](#)

***

## Setup and Running the Application

1. Clone the repository to your local machine or download the HTML, CSS, and JavaScript files.
2. Open the HTML file in a web browser to start the application.
3. Sign up and create a booking

## Deployment
- Repository created in Github and updated in Gitpod
- Deployed using Heroku
- Connected Secret Keys to config vars
- Connected to the Code Institute PostGres Database
- Connected to [Cloudinary](https://cloudinary.com/) (static file/assests host)

Link to deployed site: [https://late-night-cafe-353782271257.herokuapp.com/](https://late-night-cafe-353782271257.herokuapp.com/)

[Back to top](#)

***

## Credits
__Resources Used and Consulted__ 
- [ChatGPT](https://openai.com/chatgpt/) used throughout for coding advice and inspiration.
- [Blackbox AI](https://www.blackbox.ai/) used throughout for coding advice and inspiration.
- [Font Awesome](https://fontawesome.com/) for the social media icons in footer.
- [Favicon.io](https://favicon.io/) - online favicon generator used to draw favicon.
- Angela Yu's [The Complete 2024 Web Development Bootcamp course on Udemy](https://www.udemy.com/course/the-complete-web-development-bootcamp) - reviewed videos to brush up on Python.
- [Stack Overflow](https://stackoverflow.com/) for troubleshooting and understanding coding concepts.
- [MDN web docs](https://developer.mozilla.org/) for helpful guides on all things coding.
- [W3Schools](https://www.w3schools.com/) for helpful guides on all things coding.
- [Bootstrap](https://getbootstrap.com/) for docs about Bootstrap.

__Media__
<a href="https://www.freepik.com/free-photo/cup-coffee-table-front-street-with-city-lights-background_40970695.htm#fromView=search&page=1&position=39&uuid=64b1e9e8-e30f-4dc8-9008-dd118719555f">Image by vecstock on Freepik</a>
Photo by Clem Onojeghuo on Unsplash 
Photo by Alexander Gilbertson on Unsplash 

__Special Thanks__
- [Spencer Barriball](https://github.com/5pence/demodemo/blob/main/assets/js/script.js)
- Code Institute's Subject Matter Expert Kevin
- Code Institute's Coding Coach Martin
- Code Institute's Coding Bootcamp Tutor Lewis
- Code Institute's Cohort Facilitator David
- Everyone in the April 2024 WW Bootcamp
- Ian Stokes for all the cups of tea
- Christopher Hughes and Sebastian Hughes for technical support and advice

[Back to top](#)
