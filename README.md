[![Build Status](https://travis-ci.com/johnj974/store.svg?branch=master)](https://travis-ci.com/johnj974/store)


<div id="readme" class="Box-body readme blob js-code-block-container">
    <article class="markdown-body entry-content p-3 p-md-6" itemprop="text"><h1><a id="user-content-your-projects-name" class="anchor" aria-hidden="true" href="#your-projects-name"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
    </a>Mystery Shack</h1>

<p>The Mystery Shack is an e-commerce site which allows customers to purchase wacky online goods, the owners decided to concentrate on the weird and wonderful,
  Unfortunately there are not many products for sale at the moment but hopefully enough to give customers the idea of what the
  future site can become. Customers can browse the products on the site, the site has all the functions of an e-commerce site with the customer once they are registered be able to add products to their cart and proceed to
 a checkout area where they can amend their order or they can proceed to a payment area where they can enter delivery and payment options using
  the stripe api</p>

<p>
This project has been deployed to heroku and can be viewed <a href="https://agri-e-store.herokuapp.com/" target="_blank">here.</a>
The projects repository can be viewed <a href="https://github.com/johnj974/store" target="_blank">here.</a>
</p>

<h2>Resubmission</h2>
<p>This is a resubmission of my project MysteryShack, The major issue addressed with this submission is the password reset functionallity
which seems to have been resolved with the creation of a new google account with certain security features disabled being used as the base/gateway e-mail
for the site, Debug mode is now also set to false,</p>
<h2><a id="user-content-ux" class="anchor" aria-hidden="true" href="#ux"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>UX</h2>
<p>The idea for the user experience is to have a site that is easy to navigate around, I did not achieve that goal with this design, the lack of a 
wireframe and an idea of what the site was going to cater for at the start of the project hindered things later.
My goals as a user were to have a site that is easy on the eye and easy to navigate around where all the  important information is prominent
on the site and that there would be options to get more information if desired, I wanted users to be able to view the products and to be able 
to purchase them with little fuss. As a user of the site my plan was to have an option for the customer to updaate all their details but at the 
moment they can only change their password.</p>
<p>As an e-commerce customer I believe that the site delivers on the core requirements of such a site where the user can:</p>
<ul>
<li>Register an account</li>
<li>Log in or log out of their registered account</li>
<li>Search for products</li>
<li>Reset their password</li>
<li>Add products to a cart</li>
<li>Adjust their orders</li>
<li>Pay for their items securely</li>
</ul>
<h2><a id="user-content-features" class="anchor" aria-hidden="true" href="#features"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Features</h2>

<p>The home page has a landing image and a basic navigation bar and footer, there is a message for any new user to the site,
the navigation bar has all the links required to navigate around the site, any user that does not log in can only view the products,
they have the option of registering from the navigation bar</p>
<p>Once a customer logs in they have the option of puchasing any of the products from the products page, there is a search function
located in the navbar to help customers look for items, when a customer adds items to the basket
there is a counter on the cart which gives them a visual clue as to the amount of products that they have added, the customer
clicks on the cart to access the cart page where they can amend each item in their shopping cart before moving onto the checkout page, 
there is a list at the top of the page again confirming the products for purchase before the customer enters delivery and payment details,
Customers can also request a new password through the login page, an e mail is sent to their address which they use to reset their password</p>
<p>As an admin user you have the option of adding, deleting and updating products. Unfortunately this is not fully functional as I
 have yet to figure out how to add an image to the new created product from the dashboard</p>
 <p>To access the site as a superuser use; username:admin, password:o1234567</p>
  




<h2><a id="user-content-features-left-to-implement" class="anchor" aria-hidden="true" href="#features-left-to-implement"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Features Left to Implement</h2>
<p>This site is far from finished, there are a lot of features on the site that could be done a lot better given more time and more experience.</p>
<p>I started a rare items page that would only appear if you were a registered or logged in customer, my idea was that it would be a reward
for registering to the website, however when I tried to put the rare item into the cart it kept getting over ridden by the producks id key, I would 
like to fix this when I have more time. I removed the connection to the app until I can figure out how to implement it correctly </p>
<p>More detailed information about the products such as the number in stock and a way of recording items sold in total and maybe over a certain
period of time. I would also include an individual counter on each product to show the amount of each item a person has in their cart.</p>
<p>I did not get a chance to finish the profile page of the logged in user, I would like it to show customers address and purchasing history.
Also some kind of a loyalty system that would reduce the cost of products based on the amount already purchased by a customer 
As a superuser you are able to adjust products from the dashboard but I could not get it to render an image to the new product
from the dashboard, this is a future feature that I would want to add, I would also 
like the superuser to be able to do more from the dashboard such as updating users from the dashboard. I must also add a search message when 
a search item does not match the search parameters, also adding some sort of filtered search options when the list of products gets larger</p>
<p> I would like to add the ability where the customer could adjust their own personal information, an option to leave a comment or rating on
purchased products could also be added, also the ability for customers to create a wishlist where they could save items for a later purchase</p>

<h2><a id="user-content-technologies-used" class="anchor" aria-hidden="true" href="#technologies-used"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Technologies Used</h2>
<ul>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
<li>Python</li>
<li>Django</li>
<li>Javascript</li>
<li>Heroku</li>
<li>AWS</li>
</ul>

<h2><a id="user-content-testing" class="anchor" aria-hidden="true" href="#testing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Testing</h2>
<p>The site was tested on mobile devices manufactured by huawei,apple and samsung.it was tested on laptop devices and desktops
 of varying sizes and operating systems such as chrome,firefox, and edge, only slight styling changes were observed, during a password reset
 using the phone the page where you reset the password did not render correctly, there appeared to be a break in te side panel to the left<br>
 The following tests were conducted on the site to check functionality. <br>
 <ul>
 <li>All navbar links on all the differant pages were checked and all of them are linked correctly.</li>
 <li> The footer links were checked and all of them work and open in a seperate window.</li>
 <li> All functional buttons are working on site</li>
 <li> All input fields were checked and all inputs are being recorded</li>
 <li> All pages when resized are responsive and are easy to navigate.</li>
 <li>All the forms were checked for required input fields</li>
 </ul>
</p>
<p>I used html validators and css validators to check for errors in the code, I corrected as many errors as i could, A pep8
validator was used to check the python code and most issues were resolved, I left the lines that were too long as I did
not want to take the chance of breaking working code</p>
<p>The forms for login and registering were tested to confirm it displays a message to the user asking to enter
the required information and preventing the form submission in case a field was left empty.
The social media links were tested individually to make sure it does redirect the user to the relevant content and that they
opened in seperate tags</p>
<p>Manual testing was done on all the functionality of the site.
The products were successfully loaded and stored in the database, same with the profile of the user.
Products were added to the cart and moved to the checkout successfully and the Stripe payment function
has been verified with a test card and all transactions show up on the Stripe dashboard.</p>
<p>The password reset functionality cracked me up for days, I tried three differant ways of implementing it and each one
generated all the same problems, I traced the main problem back to my user registration form not recording the users email
in the database for some reason, I reverted back to a django class for the creation of a new user and that seemed to fix
that issue, I then had a problem with the SMTPA authentication even though I adjusted my google settings it would still given
me that failure.
<p>This is a resubmission of my project MysteryShack, The major issue addressed with this submission is the password reset functionallity
which seems to have been resolved with the creation of a new google account with security features disabled being used as the base/gateway e-mail
for the site, Debug mode is now also set to false,</p>
<p>Automated testing was done by Travis-CL, there were a lot of errors during the build but they all seemed to get 
ironed out as I went over the code</p>
<p></p>

 
 

<h2><a id="user-content-deployment" class="anchor" aria-hidden="true" href="#deployment"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Deployment</h2>
<p>This site was deployed to Heroku using the command line interface<br>
   The steps taken to deploy the app were:<br>
   <ul>
   <li>1. I created a Heroku account</li>
   <li>2. Click on the new button to create the app name I used to run my project.</li>
   <li>3. Choose the region that the server will be based from.</li>
   <li>4. Log into Heroku from the CLI, I needed to provide confirmation using a url.</li>
   <li>5. I insured that the requirements.txt file was installed along with a procfile and that</li>
      all environmental variables were safely hidden in a git ignore file.
   <li>6. I added my files and then commited them to the github repository.</li>
   <li>7. From the Heroku home page that has my app that was created earlier I copied a
      line of code under the Create a new directory that has my application name
      and inserted it into the CLI to create a link between my code and Heroku.</li>
   <li>8. Once that snippet of code runs I typed: git push heroku master to push my</li>
      project to the Heroku server to be run.
   <li>9. Type heroku ps:scale web=1 to start the app, confirmation is when it is scaling dynos</li>
  <li>10. I went back to Heroku, go to settings, go to reveal config vars, input my IP and PORT</li>
      addresses and also add in any variables that are kept in the gitignore file.
  <li>11. When all configs are input I clicked on open app and my project was being hosted by Heroku.</li>
  <li>12. My initial deployment was implemented using the ClI, further deployments were initialised from the heroku dashboard.</li>
  <li>13. To deploy from heroku I added,commited and pushed any changes of code to github.</li>
  <li>14. I went to the deploy section in heroku which is already referanced to the app name.</li>
  <li>15. I chose connect to github in the deployment method of the deploy page.</li>
  <li>16. I input my github login details and the app i wished to connect with</li>
  <li>17. When i received notification of the connection i chose manual deploy of the app.</li>
  <li>18. The most up to date version of the app is then hosted on Heroku</li>
    </ul>
    </p>
    <p>To view the app after initial setup in Heroku</p>
    <ul>
    <li>Login to heroku</li>
    <li>Choose app name.</li>
    <li>Choose Deploy header in dashboard.</li>
    <li>Go to bottom of page and click on deploy branch</li>
    </ul>
    <h2>Local Deployment</h2>
    <p>In order to clone the github repository:</p>
    <ol>
    <li>On GitHub, navigate to the main page of the repository.</li>
    <li>Under the repository name, click Clone or download.</li>
    <li>To clone the repository using HTTPS, under "Clone with HTTPS", click . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click .</li>
    <li>Open Git Bash.</li>
    <li>Change the current working directory to the location where you want the cloned directory to be made.</li>
    <li>Type git clone https://github.com/johnj974/Store</li>
    <li>Press Enter. Your local clone will be created.</li>
    <li>Run pip install -r requirements.txt to add the project requirements</li>
    <li>Start the server with ./manage.py runserver</li>
    </ol>
    

<h2><a id="user-content-credits" class="anchor" aria-hidden="true" href="#credits"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Credits</h2>
<h3><a id="user-content-content" class="anchor" aria-hidden="true" href="#content"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Content</h3>
<p>All of the content is written by me</p>

<h3><a id="user-content-media" class="anchor" aria-hidden="true" href="#media"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Media</h3>
<p>All pictures were taken from Pexels.com</p>

<h3><a id="user-content-acknowledgements" class="anchor" aria-hidden="true" href="#acknowledgements"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>
</a>Acknowledgements</h3>
<p>The project was built using the code institute django module as the main go to referance when I got stuck,the majority of the 
functionality comes from the django  module tutorial. I also used various youtube channels
such as Traversy media, Dennis Ivy, Corey Schafer and Freecodecamp for ideas along with all the various stack overflow threads which helped to me to
identify and fix a lot of the errors that I encountered.</p>


