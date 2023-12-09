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