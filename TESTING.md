# Manual Testing

### User Registration and Authentications

| Description | Steps | Expected Outcome | Outcome |
|-------------|-------|------------------|---------|
| User can register. |1. Click the "Get Started" or "Sign Up" button.<br>2. Fill out the form accordingly with choice to create either a student or trainer account| Upon confirming that the username is unique and the password meets validation criteria, the registration is deemed successful, leading to redirection to the Dashboard page of the account type. | Worked as expected |
| User can log in.| 1. Click the "Log In" button in the nav bar.<br>2. Enter and submit your log in detail in the form. | Upon successful validation of the username and password, the user is logged in and then redirected to the designated dashboard.| Worked as expected |
| User can log out.| 1. Click the "Log Out" button in the navigation bar | After pressing the "Log Out" button you will be logged out from your account and redirected to the homepage. | Worked as expected |

### Dashboard

#### __Trainer__ :
| Description | Steps | Expected Outcome | Outcome |
|-------------|-------|------------------|---------|
| Logged out user cant access the dashboard | Enter the url of the of the dashboard.| The user should be redirected to the "Log In" page. | Worked as expected |
| Student Account can't access trainers dashboard | 1. Log into a student account. <br> 2. Enter the url of the of the trainer dashboard. | The student account should be redirected to the student dashboard. | Worked as expected |
| If there are more than 3 lessons created, only the 3 earliest are shown. | Open the trainer dashboard page. | Only the first 3 of the earliest lessons should be displayed in cronological order. | Worked as expected |
| The navigation bar has the scheduling option included. | 1. Log into a trainer account. <br>2. Click the hamburger icon on the top right. | The menu should slide in from the right and contain the "scheduling" button to link you to the | Worked as expected |
| The Earnings section displays the total price before and after fees. | 1. Create a number of lessons in the scheduling page.<br>2. Open the trainer dashboard. | Application should add up all the lesson prices and display them in the earing section. | Worked as expected |

#### __Student__ :
| Description | Steps | Expected Outcome | Outcome |
|-------------|-------|------------------|---------|
| Logged out user can't access the dashboard | Enter the url of the of the dashboard.| The user should be redirected to the "Log In" page. | Worked as expected |
| If there are more than 3 lessons created, only the 3 earliest are shown. | Open the student dashboard page. | Only the first 3 of the earliest lessons should be displayed in cronological order. | Worked as expected |
| Accept incoming lessons from the trainer | 1. Open the dashboard.<br>2. Click the accept button. | After clicking the "Accept" button the lesson should appear in the calendar section. | Worked as expected |
| Cancel incoming lessons from the trainer | 1. Open the dashboard.<br>2. Click the cancel button. | After clicking the "Cancel" button the incoming lesson should disappear and the status of the lesson to "cancelled". | Worked as expected |

### Scheduling

| Description | Steps | Expected Outcome | Outcome |
|-------------|-------|------------------|---------|
| Logged out user can't access the scheduling page. | Enter the url of the of the scheduling page url. | The user should be redirected to the "Log In" page. | Worked as expected |
| Students user can't access the scheduling page. | 1. Log into a student account.<br>2. Enter the url of the of the scheduling page url. | The user should be redirected back to the student dashboard. | Worked as expected |
| View the created lessons | Open the schedule page. | All the created lessons by the trainer should be displayed. | Worked as expected |
| Trainer can edit each lesson. | 1. Open the scheduling page.<br>2. Click the "more" button on a lesson of choice.<br>3. Press "Edit" from the dropdown option. | The lesson should open on a new page displaying a form that enables the trainer to edit the lesson of choice. | Worked as expected |
| Trainer can delete each lesson | 1. Create a lesson.<br>2. Find the created lesson and click the "more" button.<br>3. Press the delete option. | The created lesson should be deleted from the database. | Worked as expected |

### Lesson Edit Page

| Description | Steps | Expected Outcome | Outcome |
|-------------|-------|------------------|---------|
| Trainer can edit each part of the lesson. | 1. Open the scheduling page.<br>2. Click the "more" button on a lesson of choice.<br>3. Press "Edit" from the dropdown option.<br>4. Edit the form accordingly.<br>5. Click the save button. | If all the edited data is correctly formatted, the data will be saved and you will be redirected back to the scheduling page. | Worked as expected |

## Browser and Mobile compatibility

Each page has been designed with the mobile first approach, so therefore the website is responsive to smaller devices. With some differences depending on the content, pages should switch into mobile view if the size drops below 768 pixels.

I tested this by using the built in Chrome mobile viewer but have also used my Iphone 12 to further test my website.

The website was tested on multiple browsers to check for any compatibility bugs both in the mobile view and the desktop size view. The browsers on which I tested my website on:

-   Google Chrome
-   Internet Explorer
-   Safari
-   FireFox

Minor bugs were found where on the features page the videos would not auto-play due to safety reasons on the mobile phone.

## Unit Testing

## Validator Testing

### HTML W3C Validator

Each source code was processed by the validator by passing the url into the "validate by Url" to check for any markup errors. I run the validator and the results were as followed:

#### Home Pages

-   index.html
    - no Errors
-   features_page.html
    - no Errors
-   goals_page.html
    - no Errors
-   about_us_page.html
    - no Errors

#### Authentication Pages

Account Pages
-   login.html
    - no Errors
-   signup.html
    - no Errors

#### Dashboard Pages

-   dashboard.html
    - no Errors
-   student_dashboard.html
    - no Errors
-   schedule.html
    - no Errors
-   update_lesson.html
    - no Errors

#### Errors

-   404.html
    - no Errors
-   500.html
    - no Errors

### CI Python Linter 

I tested all the python files using the Code Institute python Linter, this is not including the files that were originally created by the django REST Framework.

#### fit_sync_app
-   admin.py
-   apps.py
-   models.py
-   views.py

The only errors that was displayed by the CI python linter were the line length errors due to the lines being over 80 characters long.

#### accounts
-   admin.py
-   apps.py
-   forms.py
-   models.py
-   urls.py
-   views.py

The only errors that was displayed by the CI python linter were the line length errors due to the lines being over 80 characters long.