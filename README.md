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

### Navbar ![navbar](readme_img/site_view/navbar.png)

 -  There is a navbar fixed on the top of all the web pages to give the user better access and navigate the website easily. 

 - search bar on the top inside navbar can assite user to search book in any pages

 - shopping bag help to visual of total amount of checkout. 
 - Account button has login/signup ( For the admin account has book manager too). So user can easily login/singup/my profile/book manager. 

 - show four main pages( BOOKS/FICTIONS/NON-FINCTIONS/SECOND_HAND BOOKS)
easily navigate the each pages. 

### Welcome (Home)![home](readme_img/site_view/home_page.png)

 - Welcoming page with shop book button which lead to main books page.



### Books ![books](readme_img/site_view/books_page.png)


 - Shows all inventory on the website ( all the books registered)

 - each books have a button to go book detail( click the image or click the buy now button)
 - small up arrow button help to viewer can go topup with one click

### Fictions ![fictions](readme_img/site_view/fictions_page.png)

 -  show all fictions categorised book.

 - small up arrow button help to viewer can go topup with one click

### Non-Fictions ![nonfictions](readme_img/site_view/nonfictions.png)

 - show all Non-fictions categorised book. 

 - small up arrow button help to viewer can go topup with one click

### Second-hand books ![secondhandbooks](readme_img/site_view/secondhand_page.png)

 - show all second-hand book categorised book. 

 - small up arrow button help to viewer can go topup with one click

### Book_detail ![bookdetail](readme_img/site_view/book_detail_page.png)

 - Show user selected book detail

 - Details of the book and come with order function. 

 - ordering quantity can be change with mouse click or keyboard type

 -  keep shopping link to the books page. 

### Login ![login](readme_img/site_view/login_page.png)

 - user who already have account here can login in this page

 - save function with remember me click box

 - go back to home (lead to welcome page)

 -  Forget password button lead to password reset page/user type the registered email and it will send the password reset e-mail to reset password link in it. 


### Sign out ![signout](readme_img/site_view/signout_page.png)

- after user logout from the main page, this page will load to confirm that user really want to logout. 

- have a two option that cancel the logout or logout. 

- when the user logout the page it is automatically load to welcoming page


### Sign up ![signup](readme_img/site_view/signup_page.png)

- simple register function page with a user name and password input form.  Under the form, the link suggested to the login page to lead the user who already register to the site. User name and password min 5 to max 15words. required and correctly labelled.

### Check out ![checkout](readme_img/site_view/checkout_page.png)

 -  the page for input detail of user information for the shipping and order information. 

 -  Delivery information can be save for the next order on my profile

 - Payment info ( only card at the moment). and if the it isn't valid information, shows the error

### Book management ![bookmanagement](readme_img/site_view/bookmanagement_page.png)

 -  As admin, able to update book ( details and image)

### Shopping bag ![shippingbag](readme_img/site_view/shopping_bag_page.png)

 -  When shopper add the book on the bag it will lead to this page

 -  shows the detail of order information and shopper can update the order quantity or remove the choose the book from the bag. 

 - Page lead to final checkout page to conclude the ordering process. 

 -  shows total amount of payment and Delivery fee too, inform the free delivery if it is the case

### My profile ![myprofile](readme_img/site_view/myprofile_page.png)

 - If user login, there is my profile page can be shown. 

 - User can change profile and check the order history. 

 - Check the order number, can see the all the detail of oder. 

### Profile/Order history ![orderhistory](readme_img/site_view/profile_orderhistory.png)

 -  If the user has order history it will shows right side of my profile page.

### Order confirmed ![confirmed](readme_img/site_view/orderconfirmed_page.png)

- when shopper finished all the checkout, this page will render and shows all the details of order 
   details. Also toast message will inform to shopper that it sent to order confirmation email. 



## Features left to implement
---
 -  If a shopper can change the rate or admin can collect the rate of the book can be great for collecting a good recommendation database. 

 -  Social media links can be added in future such as facebook page or instagram. It will also be a nice tool to collect information and engagement between users. 

 - If the viewer can sort the book by price/rate could be nice.

 - Having a footer explain about the business and contact information would be nice. 

 - If account on the navbar change the icon when user login/admin login, could be nice
 

## Technologies

### Technologies Used
---

### Languages Used

## HTML5, CSS3, JAVASCRIPT,Python+Django

### Frameworks,Libraries & Service sites

1) [Bootstrap](https://getbootstrap.com/) - prime front-end framework

2) [stripe](https://dashboard.stripe.com/) - payment provider

3) [Google Fonts](https://fonts.google.com/specimen/Oswald?preview.text_type=custom) - Google fonts use for most headlines and paragraphs. 

4) [Font Awesome](https://fontawesome.com/) - It used on all pages throughout the website to add icons 

5) [Balsamiq](https://balsamiq.com/wireframes/) - used to create the wireframe during the design process.

6) [JQuery](https://jquery.com/) - used javascript fuctions.


7) [AWS](https://aws.amazon.com/) - public cloud storage resource, used for the store my static and media files.

8) [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - The project uses Jinja for templating with Flask in the HTML code. I used Jinja to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.


### Version control

  - [Github](https://github.com/) - Used to store the code and use of Github Pages to deploy the website.

  - [Gitpod](https://gitpod.io/workspaces) - Used as the primary version control IDE for developers to further push and commit code to Github.

### Hosting
  - [Heroku](https://www.heroku.com/) - I've used Heroku as the hosting platform to deploy my app.
  - [AWS](https://aws.amazon.com/) - public cloud storage resource, used for the store my static and media files.

### Other

 - [Code institute Course](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) - my primary source of leaning code. ![Project - Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218)
 - [ChromeDevTools](https://developer.chrome.com/docs/devtools/)- Used eachtime when I check error/issue on my site.
 - [W3Schools](https://www.w3schools.com/js/default.asp) - often use for css and javascript code tips
 - [AmIResponsive](http://ami.responsivedesign.is/) - Used to check how the layout of the website looks across different devices.
 - [responsinator](http://www.responsinator.com/?url=https://oneday2010.github.io/milestone-project2/) - Used to test website layout on multiple devices
 - [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) - Used to test all pages on a mobile device
 - [Colorspace](https://mycolor.space/?hex=%23352E24&sub=1) - Used to find right color pattern for my website
 - [Youtube](https://www.youtube.com/) - Used to got javascript and css tip
 - [stackoverflow](https://stackoverflow.com/) - get help for code error or advice
 - [TinyJPG](https://tinyjpg.com/) - to compress image to better loading speed 
 


## Testing 
---

 - Forms testing

   ### There are five test users registered in this site. 
    
    - bookseller (Primary admin user) -> password : admintest
    - volec -> password : test2022
    

-> login with bookseller(Primary admin), site shows edit/delete button on books and book manager page.

There are six forms tests images below. 


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

   
   
  - I tested on Safari,Chrome, Firefox it was performed without issue. 



#### Validation

 - [W3C Markup Validator](https://validator.w3.org/) : The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.


 - [W3C CSS Vaildator](https://jigsaw.w3.org/css-validator/) no issue found

    

    ![W3C CSS Validator]

 - [Esprima Syntax Validator tool](https://esprima.org/demo/validate.html) no issues found

    

    ![Esprima Syntax Validator tool]

 - [Pep8 Online tool](http://pep8online.com/)  

    

   ![Pep8 Validator tool]


  - [Documentation on using Developer Tools Lighthouse](https://developers.google.com/web/tools/lighthouse) 

  ![Documentation on using Developer Tools Lighthouse]
   


#### Project bug and solution

  - bug1

   ![bug1]

   


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

  

   


### Remote Deployment  

  

## Credits
---
* ### Content

    1) my primary source of leaning code. ![Project - Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218)

    2) Primary front-end framework from [bootstrap](https://materializecss.com/)

    3) Amazon.co.uk [Amazon.co.uk](https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=&ref=nb_sb_noss&crid=1T8BB5M2AUKBK&sprefix=%2Cstripbooks%2C67) 
    
    4) Grammar and spelling checked from [Grammarly](www.grammarly.com/)
    


* ### Media

  most of images I used I referenced below (Pixabay)/(Unsplash) and else below

   1) 


* ### Acknowledgements

    I received inspiration for this project from 

    1) [Code institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)

    2) I got great help from elerel's [readme reference](https://github.com/elerel/ms1-go2snow/blob/master/README.md#overview) and pramcistudent'[readme reference](https://github.com/pramcistudent/cookbook-project3/blob/master/README.md#local-deployment)

    3) My mentor Nishant Kumar's support gives me great help and Thanks to my tutors. 
