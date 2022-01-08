# Buybook here



[View the live project here](https://buybookhere.herokuapp.com/) 

This website is made for users who are interested in shopping for new published books or shop second-hand books. The main aim of the project is to create a user-friendly website that can help users to interact with content and search the information easily, be able to purchase the product through a secure payment method.
It also gets secure confirmation after the order submits. The admin can do managing the products through the website.  Finally, The website is actively working as an e-commerce platform with all essential functions.


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
 Many websites deal with book e-commerce platforms. My main purpose of this website is becoming admin of the website, updating new product(book) through the website and managing inventories within the website. Also, the user who signs up can review him/her profile,order history and secure check out too. I tried to make a simple, easy but reliable e-commerce website. 


## Description
---
 It is a buybookhere website is aim to be a simple and easy e-commerce platform that trade new book as well as second-hand books which can be accessed on all devices. As store owner can do manage the store within the website, as site user also able to signup/login and check the profile. As shopper can search right book for themselves. All basic e-commerce satisfied the purpose of the website. 

![overoll site images](readme_img/site_img.png)
![overoll site images](readme_img/site_img2.png)



## UX

### User experience
---

### Strategy
---

 Main target user : book shopper, book searcher, book dealer, site visitors worldwide.

 The website is aimed to function simple book e-commerce platform. Therefore, main target users are able to signup/login and check their profiles and review their order history. In this way, users feel secure to checkout and revisit the site with better impressions. Visitors can search the book for what they are looking for easily and review the book with simple steps.




####  Business Goals

 1. To provide a professional, clear and easy navigate a website for any type of user, be it, first time user, as well.

 2. Simple book trade e-commerce platform, checkout platform is reliable and confirmed all the checkout record after. Users can sign up on the platform, as the admin can manage inventory and users too. 

 3.  Visitors can easily navigate all the sites and search the book too. 


#### User Stories

  * As first time user

    " I'm just looking for an easy way to search book what I look for, I don't want to register"

    " I want to see the total of my purchases during my shopping"
    
    " I'm not sure I will get free delivery after how much I purchased the book"
    
    "I want to change the mind and remove the books from the shopping bag"

    "I don't know I order book correctly? right address and money I paid"

    "Don't remember I sign up this site before"

        

  * As Regular User:
    "I want to see my profile on the site because I sign up for the website"

    " I want to check my order history"

    " I don't want to other people see my oder history"

    " I forgot my password"

    " I want to change my delivery address and save for next time"

### Scope
---

 - Useful - This website is useful to a visitor who searches new published book and cheap second-handbook. Also, admin user can manage the stock and sign up the user can manage profile and review the order history. 

 - Sellable -  There are many potential fundable possibilities such as a book market and furthermore, challenge the e-book market in future.  In covid situation, more customer want to use e-market, second-hand book items can be great potential customer behind too.

 - Buildable - Fits in with the level of my abilities, limited python usability and javascript function but it can improve in future. Many codes followed the Boutique Ado from code institute course, inspired by  Django prebuilt functions for all basic e-comers function. Use stripe for payment provider and AWS for database management tool. Having difficulty to connected all platforms but followed the course steps.  

 - Objective - user/visitor can use this site as reliable book e-comers platform. As admin, can manage the inventory within website. 

 - Functional - user can log in/log out and register an account. After register the website, the user can review the profile and order history. Admin can upload new book,edit and delate. Also admin can manage users and website function as basic e-comers platform (buy,checkout,get paid, confirmed etc) 

 - Non-Functional  -  Would be better with sorted function by price/review. Also, if user could add review or comment can be potential improve-able  functions. 


 - Business Rules -   Make sure don't share personal user name and password, specially as admin, don't share any information in relate the site ownership. Otherwise, it can be compromised. Make sure not exposed any secret key in relate stripe,AWS. User who did check out get confirmed order and get records to proven. 



 * Main target user : book shopper, book searcher, book dealer, site visitors worldwide.




### Structure
---
1. visitor/non-registered user
welcoming page and books pages(able to search and check the details of book, buy and checkout, confirmed the order and get a confirmation email)
2. login/sign up user
same structure as a non-registered user as well as own profile pages and able to update profile information and check the order history. 
3. Admin user
Able to manage the inventory. Have a book management page only for the admin user. Each book has an edit and delates button for the manage book only admin can access and view.




### Skeleton
---
The website shows three different ways. the non-registered user used the site and the registered user using the site. As well as Admin who is able to manage inventory and has ownership of site get more control of edit, delate and update access. Most of the pages are match with my framework, but I didn't much change of basic frame work and models from Code institute boutique Ado project. I gave bit of front-end change from the original project to give Morden and cheerful looks. 

 
 #### Wireframes



 - Landing Page: welcoming page
 
![welcome](readme_img/framework/frame_welcome.png)

 - Welcome

![home](readme_img/framework/frame_home.png)

 - Home

![fictions](readme_img/framework/frame_fictions.png)

 - Fictions
 
![nonfictions](readme_img/framework/frame_nonfictions.png)

 - Non-Fictions

![secondhand](readme_img/framework/frame_secondhand.png)

 - Second-hand books

![loginprofile](readme_img/framework/frame_login_profile_management.png)

 - Login and Profile and management page

![checkoutthankyou](readme_img/framework/frame_checkout_thankyou.png)

 - Checkout and Thank you page

![signup](readme_img/framework/frame_signup.png)

 - Sign up

 



### Surface
—--
I wanted to attracted more younger generation for the website visitor. So, tried to give more colourful and as same time Morden look too. Use red colour for the main attraction colour and grey ,white and black are primary colours for the website. Try not too use many colour which can create confusions. 
Check [colorspace]((https://mycolor.space/?hex=%23352E24&sub=1)) for colour match. Many parts of colours and framework used from bootsrap prebuilted for the card/basic e-commers functions. Can found the reference on the bottom of the readme file. 



 #### Design

   - Images : Each book image is selected from [pixabay](https://pixabay.com/) and  [unsplash]( https://unsplash.com/). All the book titles and authors written by manually. Try to match the image with book contents. 


  - Color Scheme : Use Red for the attraction and emphasising purpose. Gray and Black for the Morden look and try to leave many empty space to not make confusion of the user. Use pre-build color Scheme on toast and give green and red for edit/delate button to easily catch the eyes.  
 
   
  - Typography : I used Google Fonts to get some idea of my website fonts and decided to use “ Roboto” and “Sans-serif” as the backup font. I choose Roboto because it looks more followed trend as modern and minimalism at the same time it looks friendly and reliable.


  - Icons : Font Awesome was my choice to use all icons on my website. Try to use icons that easy to understand the purpose of usage. 





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
