# Buybook here



[View the live project here](https://buybookhere.herokuapp.com/) 






---
---
## Table of contents
---

[Overview](#overview)

[Description](#description) 

[Ux](#ux) 

[Features](#features) 

[Technologies](#technologies) 

[Testing](#testing) 

[Deployment](#deployment) 

[Credits](#credits) 





## Overview
---
 


## Description
---

![overoll site images](static/images/site_img.png)



## UX

### User experience
---

### Strategy
---

 Main target user : 




####  Business Goals

 1. 

 2. 

 3.  

 4.  

#### User Stories

  * As first time user

    " "

    " "
    
    " "

        

  * As Regular User:

    ""

    " "

    " "

### Scope
---

 - Useful - 

 - Sellable - 

 - Buildable - 

 - Objective - 
 - Functional - 

 - Non-Functional  -  

 - Business Rules -  



 * Main target user : 




### Structure
---





### Skeleton
---


 
 #### Wireframes



 - Landing Page: welcoming page
 
![HOME](static/images/wireframe/home_wireframe.png)

 - login

![login](static/images/wireframe/login_wireframe.png)

 - Register

![register](static/images/wireframe/register_wireframe.png)

 - profile
 
![profile](static/images/wireframe/profile_wireframe.png)

 - newrecipe

![newrecipe](static/images/wireframe/newrecipe_wireframe.png)

 



### Surface
—--




 #### Design

   - Images :


  - Color Scheme :  
 

   ![Materialize](static/images/color_palette.png)
    



  - Typography : 


  - Icons : 




## Features
---

### Navbar

 -  

 - 

 - 

### Home

 - 

 - 

 - 

 -  

### Login

 - simple login function page with a user name and password input form.  Under the form, the link suggested to the register page to lead the user to register to the site. User name and password min 5 to max 15words. required and correctly labelled.

### Logout

 - when the user logout the page it is automatically link to login page

### New Recipes

 - 

### Profile

 - the profile page is automatically linked to login information. So, registered user login the site, profile page open with right user information and it also has a button with home page linked. 

### Register

 -  simple register function page with a user name and password input form.  Under the form, the link suggested to the login page to lead the user who already register to the site. User name and password min 5 to max 15words. required and correctly labelled.



## Features left to implement
---

 -  

 -  

 - 

 - 

 

## Technologies

### Technologies Used
---

### Languages Used

## HTML5, CSS3, JAVASCRIPT,

### Frameworks,Libraries & Service sites

1) 

2) 

3) [Google Fonts](https://fonts.google.com/specimen/Oswald?preview.text_type=custom) - Google fonts use for most headlines and paragraphs. 

4) [Font Awesome](https://fontawesome.com/) - It used on all pages throughout the website to add icons 

5) [Balsamiq](https://balsamiq.com/wireframes/) - used to create the wireframe during the design process.

6) [JQuery](https://jquery.com/) - used javascript fuctions.


7) [flask](https://flask.palletsprojects.com/en/2.0.x/) - The project uses Flask, which is a Python microframework.

8) [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - The project uses Jinja for templating with Flask in the HTML code. I used Jinja to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.

9) 

10) 

### Version control

  - [Github](https://github.com/) - Used to store the code and use of Github Pages to deploy the website.

  - [Gitpod](https://gitpod.io/workspaces) - Used as the primary version control IDE for developers to further push and commit code to Github.

### Hosting
  - [Heroku](https://www.heroku.com/) - I've used Heroku as the hosting platform to deploy my app.

### Other

 - [Code institute Course](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) - my primary source of leaning code.
 - [ChromeDevTools](https://developer.chrome.com/docs/devtools/)- Used eachtime when I check error/issue on my site.
 - [W3Schools](https://www.w3schools.com/js/default.asp) - often use for css and javascript code tips
 - [AmIResponsive](http://ami.responsivedesign.is/) - Used to check how the layout of the website looks across different devices.
 - [responsinator](http://www.responsinator.com/?url=https://oneday2010.github.io/milestone-project2/) - Used to test website layout on multiple devices
 - [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) - Used to test all pages on a mobile device
 - [Colorspace](https://mycolor.space/?hex=%23352E24&sub=1) - Used to find right color pattern for my website
 - [Youtube](https://www.youtube.com/) - Used to got javascript and css tip
 - [TinyJPG](https://tinyjpg.com/) - to compress image to better loading speed 
 


## Testing 
---

 - Forms testing

   ### There are five test users registered in this site. 
    
    - 
    - 
    - 
    - 
    - 

-> login with Amy21 or Admin, site shows edit/delete button. 

There are six forms tests images below. 

1.  login 

![form test - login](static/images/form_test/login.png)

 - a user who already registers an account on this website can log in with an input username and password. If the username is less than five letters or more than 15letters, it shows a red underline and warning message with "please match the format requested". Same warning with a password. If password or username does not match with data, flask message pop up right corner of the website with a warning message. Moreover, after login, user's profile page will be open and with messege with username on it. 
  

2. register

 ![form test - register](static/images/form_test/register.png)

 - when a user tries to register an account, the user needs to input a username and password which letters between five to fifteen. If the requirement doesn't match, it will show a warning message.  After register  success, the user will be lead to the profile page and get the flask message with 'Registration Successful!"


3. add 

 ![form test - add recipe](static/images/form_test/add.png)

 - After the user adds a new recipe on the new recipe page, the pop-up message shows with the user successfully add the recipe. and if the contents don't match with the requirement, it doesn't allow to add any data. 


4. edit 

 ![form test - edit recipe](static/images/form_test/edit.png)

 - There are clickable buttons under recipes if the contents are created by the user who login. Therefore creators can edit/delete the contents as they wish. if the user clicks the edit button, it will lead to original data filled in a form and the user can change. After changing the form, the user can click the edit recipes button or cancel. If click edit recipes it updates with new data and if click the cancel will lead to the home page.


5. delate 

 ![form test - delete recipe](static/images/form_test/delete.png)

 - if the user clicks the delete button, it will delete the food recipe, the user will see the pop-up message.
 

6. logout

![form test - logout](static/images/form_test/logout.png)

  - If the user clicks the logout on the navbar it will lead the user to the login page and the user will get a pop-up message.


# Links : 

 Testing across various devices ( I used [responsinator](http://www.responsinator.com/?url=https%3A%2F%2Fkorean-food-recipes.herokuapp.com%2F) as well as my one device and friends. the devices blow works without issue

  -  Mobiles/tablet/laptop()

   * iPhone eXpensive portrait · width: 375px                 
   *  Android (Pixel 2) portrait · width: 412px
   * Android (Pixel 2) landscape · width: 684px
   * iPhone 6-8 Plump portrait · width: 414px
   * iPhone 11
   * iPad portrait · width: 768px:
   * MacBook 13inch 2014
   * MacBOOK 13inch 2019



 - Ensured the website was also responsive on all the pages [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly?utm_source=gws&utm_medium=onebox&utm_campaign=suit) 

   - Home ![mobile friendly test - Home](static/images/mobile_friendly_test/home_mobilefriendly.png)

   - login ![mobile friendly test - Dublin2](static/images/mobile_friendly_test/login_mobilefriendly.png)

   - register ![mobile friendly test - Dublin6](static/images/mobile_friendly_test/register_mobilefriendly.png)

   - addrecipe  ![mobile friendly test - Dublin8](static/images/mobile_friendly_test/addrecipe_mobilefriendly.png)

   
  - I tested on Safari,Chrome, Firefox it was performed without issue. 



#### Validation

 - [W3C Markup Validator](https://validator.w3.org/) : The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.


 - [W3C CSS Vaildator](https://jigsaw.w3.org/css-validator/) 

    

    ![W3C CSS Validator](static/images/css_validator.png)

 - [Esprima Syntax Validator tool](https://esprima.org/demo/validate.html) 

    

    ![Esprima Syntax Validator tool](static/images/javascript_validate.png)

 - [Pep8 Online tool](http://pep8online.com/) 

    

   ![Pep8 Validator tool](static/images/python_validator.png)


  - [Documentation on using Developer Tools Lighthouse](https://developers.google.com/web/tools/lighthouse) 

  ![Documentation on using Developer Tools Lighthouse](static/images/lighthouse.png)
   


#### Project bug and solution

  - bug1

   ![bug1](static/images/bugimg/bug1.png)

   


  - bug2

  

  

 - bug3

  

 
  
### Testing User Stories from User Experience (UX) section

 #### Testing user story goal

 
  * ##### As as First Time User:


    " "

    ->  .  

    " "

    -> . 
    
    " "

    -> .   

  * ##### As as Regular  User:

     ""


     -> . 


    " "

     -> .

    " "

    -> . 



## Deployment
---

 ### Local Deployment

  1) In order to run this project locally on your own system, you will need the following installed:

  - Python3 to run the application.
  - PIP to install all app requirements.
       -> 

  - 
    
     
      
I

   2)  
   3) 

   4) there is some sensitive data which we need to be hide in file "env.py" and it is able to hide file ".gitignore". Therefor you can secure your confidential data. you need to setup a secret key, which is required whenever using the flash() and session() functions of Flask from MongoDB. 
        

   


### Remote Deployment  

  This site is currently deployed on Heroku using the main branch on GitHub. To implement this project on Heroku, the following steps were taken:

  1) Create a requirements.txt file so Heroku can install the required dependencies to run the app.
  "pip3 freeze --local > requirements.txt".

  2) Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
    echo web: python app.py > Procfile

  3) Sign up for a free Heroku account, create your project app, and click the Deploy tab, at which point you can Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.
  
  4) In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
  IP : 
  PORT : 
  
  SECRET_KEY : <your own secret key>

  Back to diploy section and try diploy your app.
  Your app should be successfully deployed to Heroku at this point.


## Credits
---
* ### Content

    1) Many python code got inspired from  [codeinstitute_miniproject_task manager app ](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/0d4e3419132440d9b2c0943f80dc54a8/)

    2) Primary front-end framework from [materialize](https://materializecss.com/)

    3) Korean food recipe and containes [BBCGOODFOOD](https://www.bbcgoodfood.com/) / [maangchi](https://www.maangchi.com/)
    
    4) Grammar and spelling checked from [Grammarly](www.grammarly.com/)
    


* ### Media

  most of images I used I referenced below (Pixabay) and else below

    1) logo created by myself I used this tool [canva](https://www.canva.com/)
    2) [Bibimbap](https://pixabay.com/photos/food-photography-korean-bibimbap-2610863/)
    3) [Korean fied chicken](https://pixabay.com/photos/chicken-korean-dish-food-fry-521097/)
    4) [Fried rice](https://pixabay.com/photos/kimchi-fried-rice-fried-rice-rice-241051/)
    5) [Kimchi](https://pixabay.com/photos/kimchi-korean-food-food-korea-4361465/)
    6) [sonpun](https://pixabay.com/photos/wind-pant-tteok-rice-cake-masu-4869955/)
    7) [Yakgwa](https://pixabay.com/photos/korean-traditional-sweets-drug-and-2150895/)
    8) [Teokbokki](https://pixabay.com/photos/tteokbokki-food-korean-food-1607479/)
    9) [bulgogi](https://pixabay.com/photos/ttukbaegi-bul-gogi-ttukbaegi-bulgogi-2517765/)
    10) [bbq wing](https://pixabay.com/photos/ttukbaegi-bul-gogi-ttukbaegi-bulgogi-2517765/)
    11) [spinach_side](https://pixabay.com/photos/spinach-side-dish-vegetable-552505/)
    12) [Jap Chae noodles](https://pixabay.com/photos/japchae-asian-food-vegetables-house-876506/ )
    13) [Porkmeat fired](https://pixabay.com/photos/pork-meat-fried-korean-food-dinner-1582916/)
    14) [Stir-fried oyster mushrooms](https://pixabay.com/photos/food-cooking-mushrooms-4564419/)
    15) [hotdog](https://pixabay.com/photos/food-snack-street-food-korean-food-4701098/)
    16) [Hotteok](https://pixabay.com/photos/street-food-food-dish-snack-meal-6226730/)
    17) [kimbop](https://pixabay.com/photos/food-photography-korean-kimbab-2610864/)

* ### Acknowledgements

    I received inspiration for this project from 

    1) [Code institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)

    2) I got great help from elerel's [readme reference](https://github.com/elerel/ms1-go2snow/blob/master/README.md#overview) and pramcistudent'[readme reference](https://github.com/pramcistudent/cookbook-project3/blob/master/README.md#local-deployment)

    3) My mentor Nishant Kumar's support gives me great help and Thanks to my tutors. 
