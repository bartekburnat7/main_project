# FitSync

FitSync is a Full-Stack online application created for personal trainers to keep track of their students and schedule lessons with ease so that the students can check when their next lesson will take place. The website allows to create lessons for the user of choice that include the date, time and price. Each created lesson then can be edited or cancelled by the trainer and viewed by the following student.

I created this full-stack website using Django framework, Python, HTML/CSS Bootstrap and JavaScript. I used ElephantSQl as the database of choice to store the usernames and the Scheduled Lessons.

## Table of Contents

-   User Interface / User Experience
-   Features and Design
-   

## User Interface / User Experience

While creating the website I decided to utilize Bootstrap 5 to create a responsive website for mobile and desktop users that has a very clean and professional layout. The website should have content the User can read before signing up to the service so they know if this application suits them. Users of all ages should be able to navigate through the website because each trainer might have different type of students this is very important.

####    Target client for the Website:

-   Based in the UK
-   Personal Trainer
-   Has Existing Clients
-   Individual

## User Stories

###    Web Navigation and Introduction
-   #1 As a user it should be obvious that the website is made for people that are interested in the gym.
-   #2 As a user I can see cards where I can read about what the website goals are and the features that are offered.
-   #3 As a user I can easily navigate to the sign up and login page.
-   ####    Trainer
    -   #4 As a Personal trainer I can easily create a "Trainer Account" by selecting the "Create a Trainer Account:" when signing up, so I am able to book lessons for my students.

###    User Registration and Authentication
-   #5 As a user I can easily register by creating a username, password and selecting what type of account I would like to create.
-   #6 As a user I can easily log out by clicking the "Log Out" button which is placed in the navbar.

###     Dashboard
-   ####    Student
    -   #7 As a user I can easily view the calendar to see what lessons have been created under my username.
    -   #8 I can easily accept or cancel any incoming lessons created by my trainer which will then change its status to cancelled.
-   ####    Trainer
    -   #9 As a trainer I can easily see the lessons I created with the username and date displayed, or there is a message shown when I have none saying "No Lessons Found".
    -   #10 As a trainer I can easily navigate to the scheduling page if there is a need to create a new lesson for a student.

###     Scheduling
-   ####    Trainer
    - #11 As a trainer I can create a lesson by entering the Students username, type of lesson, timestamp and price.
    - #12 As a trainer I can view the lessons with all the details displayed in chronological order.
    - #13 As a trainer I can seamlessly edit and delete each lesson by clicking the "more" button and then pressing the desired option.

## Idea and Plan

The idea for this project came to when I was looking for a business idea to create within a online application that could be used commercially and all over the world without any constraints. As I am familiar with the gym I looked for a personal trainer in my area but it was very difficult to do so and ended up not finding anything at all due to no information on the matter.

My plan was to create an application with tools that Personal Trainers can use to schedule lessons, create workout plans and much more. I would first create great tools that would attract new trainers to sign up for a trainers account, then add a feature that would make finding these trainers easy by people that are seeking personal training in their area.

I asked a few personal trainers online what type of features they would like to see in the application and these are the results from most important to least:

-   Scheduling System
-   Online Workout Programming
-   Virtual Training(P2P)
-   Payments
-   Late Fees

### Agile

For this project I decided to use GitHub's issues tab and list all the challenges a trainer or user faces and give solutions under each one. Using the Agile methodology I planned out how I would tackle each issue and after developing the feature, I would assess if this feature is functional and addresses the issue correctly. If I was unhappy with the feature I would see that something is missing develop an additional solution to the feature.

##  Features and Design

### Wireframes

I decided to sketch my rough ideas of how the layout of the pages would look using moqups.com so that I have a design that I can develop off of. Some changes might have been implemented due to finding a better way of displaying the information or due to adding an extra feature.

<details><summary>Home Page</summary>
<img src="images/home_page.JPG">
</details>
<details><summary>Dashboard for Trainers</summary>
<img src="images/dashboard_trainer_wireframe.JPG">
</details>
<details><summary>Dashboard for Students</summary>
<img src="images/dashboard_Student_wireframe.JPG">
</details>
<details><summary>Scheduling for Trainers</summary>
<img src="images/dashboard_scheduling_wireframe.JPG">
</details>

Every feature that has been added, targets one or potentially more user stories in order to solve the problem of the user. While planning the layout I made sure each feature has a similar design that looks familiar, which improves the ease of navigating through out the website.

### Navigation
-   #### Navigation Bar
    There are a few type of navigation bars implemented for visiting users and logged in users, furthermore, there is a different navigation bar for the dashboard features that differs for students and trainers.

    <details><summary>Navigation bar for home pages ( Logged Out )</summary><img src=""></details>
    <details><summary>Navigation bar for home pages ( Logged In )</summary><img src=""></details>
    <details><summary>Navigation bar for Dashboard ( Trainer Account )</summary><img src=""></details>
    <details><summary>Navigation bar for Dashboard ( Student Account )</summary><img src=""></details>

##  Credits


Codemy.com
https://animated-gradient-background-generator.netlify.app/