*Log in notice! If you don't want to create an account to test out the app, you can simply log in as "leigh" and use the password "123"

# Final Project - "Fantasy Football"
Final Project for CS50w. A very basic fantasy football web application built using django and JavaScript.

**Introduction**

This is a very basic fantasy-football web application built in Django as a back-end framework with JavaScript for the front-end. The app that users to create an account, select or delete members from their team and compare their scores to other users. Right now, for simplicity, you can only select 5 player positions, but I intend to add more as I develop the app further.

All team and player information is sourced via the ... api. At the moment, the scores and stats available are from week 3 of the 2019 NFL season and are just for demonstration purposes. In the future, I will link the "live" stats. During a regular, live NFL season, scores and statistics are updated at the end of that week's round. A user's overall team score will subsequently update at the end of that round.

**Installation**

*Install project dependencies by running pip install -r requirements.txt. 
*Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
*Create superuser using python manage.py createsuperuser (optional).

**Addons/Necessary extras**

Bootstrap 4 is used for styling and is available from this link
https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css

Extra styling is also provided via "MDB" (Material Design for Bootstrap) which also makes use of Google fonts and Font Awesome. Relevant JavaScript and JQuery for these stylesheets and packages are also listed below.

Font Awesome
            https://use.fontawesome.com/releases/v5.8.2/css/all.css
Google Fonts
            https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap
Bootstrap core CSS
            https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css
Material Design Bootstrap
            https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css

JS/Jquery
            https://code.jquery.com/jquery-3.5.1.min.js
            https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js
            https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js



**Project Structure** 

Start by visiting the url ....game/login. From here, you will be able to click the "Register" link where you will be able to create an account.

Once you've created an account, you will be directed to createteamname.html where you can choose your team's name. Once you've chosen a name, you will be directed to show.html. On this page you can see your team's name and current roster of players as well as the ability to remove individual players from your lineup. Of course, at this stage, your lineup will be empty. Click "Pick Team" in the navbar. This link will take you to form.html where you can select players for your team. At the top of this page are 5 independent input fields that correspond to the five different player-positions that you will need to fill to create a team. To see the list of available players in a particular position, click on the blue buttons to display a list of available players in that position. Clicking on "QB" for instance, will display a list of all available quarterbacks and their most recent individual score. To select a particular player, click the green "Add" button that corresponds to that player. The player's full name will now appear in the "Quarterback" submission field. Click the "Submit" button to add that player to your team. If successful, a green "success" message will appear at the top of the screen. Once you have selected one player for each position, go back to "My Team" and check out your lineup. You can remove a player from your lineup anytime by clicking the corresponding "Remove" button beside a player's name.

To view the scores of all users, visit the "Scoreboard" via the "Scores" link in the navbar. Here you can see a list of all users, their team name, and their current score. Great for comparing how your team is doing against other users.

This app is mobile responsive.

**File Structure**

- game- main application directory
    
 - migrations - current migrations
 - static/game - contains JavaScript and CSS files
      - main.js - all JavaScript code
      - styles.css - contains some css styling
 - templates/game - contains all html templates for application
    - createname.html - New users create their team's name here.
    - editname.html - A logged in user can change their team's name.
    - form.html -  Logged in users can select players for their team.
    - layout.html - Base layout template for all html templates in the app.
    - login.html - Existing users can log in/follow link to register.html.
    - register.html - New users can register.
    - scoreboard.html - Displays all users and all scores.
    - show.html - Displays a user's current lineup and score.
 - admin.py - All models in models.py registered here.
 - apps.py - 'game' application registered here.
 - models.py - Contains User, player positions and team models.
 - forms.py - contains forms linked to all object models.
 - urls.py - Contains all application's urls.
 - views.py - Contains all application's views.

