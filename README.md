# Diglog

A Weblog Project Base On Django

[Mohammad Mousapour](https://github.com/mmd-punisher)

---

## General description of the Diglog project

This project is a complete web-based blog, which has a back-end with Django, a framework in Python, and a front-end with
HTML, CSS, Bootstrap and JavaScript. The back-end coding of this project has an object-oriented structure and has been
developed using Class Base Views and Generic Views. The project also supports MVT, which is the standard structure of a
web-based application; In short, it works in this way that the request sent by the user is sent to the app functions and
after processing, it is referred to the database to query the desired information and then the information is sent to
the template for execution.

## Different parts of the project and its details

A website has several parts, front end, back end and database, the front part is related to the design and interface of
the site and works with the user (client). The back-end section is for managing input and output data, and also the main
functional functions are implemented in this section; The Django framework has an Object Oriented structure and works
entirely with object orientation; The next part is the database of the website, which is used to store data. The
analysis of this model is my responsibility, and I have done the map and outline completely by myself, and I have
predicted and implemented the needs of a user.

### The external part of the website

- List of all posts (sort by newest first)
- Site bar
- Options such as creating posts and list of categories, profile settings and...
- Search capability
- Paging

### User access to the website

- User registration
- Account creation
- User login
- Username, password, email, etc.
- User logout
- Post construction
    - Title
    - Author Name
    - Header image
    - Publication date (day and time of publication)
    - Short description
    - The main text of the post (Django CKEditor)
        - Text with features such as the ability to underline words, make it familiar, etc.
        - Ability to print separately
        - Writing text as source
        - Format and templating of post text form
        - Record photo in text
        - Add graphs, symbols, emojis, quotes, etc.
- Post categories
    - Add categories
- The date of the last update
- The ability to edit the post
- The ability to delete posts
- Post deletion warning message
- Ability to like posts for logged in users
- View the view of a post (the ability to view the user who has seen the post from the admin and admin panel)
- Ability to register comments for logged in users
- The profile and profile of the author, the time of publication of the post and...

### User profile

- Name, surname, username, biography, useful links (website, Instagram, etc.)
- These specifications can only be updated by the user himself
- Ability to update the password and change it
- The date of the last login to the site, the date of the last connection to the site

### Admin access panel

- Access to all posts
- Access to all users and their accesses
- Access information (username, time and date) view a post and see who has seen a post
- Filter and sort information
- Separate admin login
- Search in admin panel

### database

The structure of the database is in the form of several tables that have different relationships. The database fields of
this website are built and implemented based on user needs and program design. The fields of these tables are as
follows:

**Post Table**

- Title = String (max_length=255 char)
- Author = Foreign Key (to User table, CASCADE)
- Header Image = Image Field (null able)
- Short Description = String (max_length=350)
- Body Text = Rich Text Field (Base on django-ckeditor)
- Category = String (max_length=255 characters)
- Published Date = Date Time Field (Auto generate)
- Slug = Slug Field (Auto create – Based on Title Field)
- Likes = Many to Many (to User table)
- Update Date = Date Time Field (Changes by updating the post)

**Profile Table**

- User = One to One Field (to User table)
- Biography = Text Field (max_length=500 characters)
- Profile Picture = Image Field (null able -> There is a default profile picture)
- Web Link = String (max_length=255, null able)
- Instagram Link = String (max_length=255, null able)
- Twitter Link = String (max_length=255, null able)
- Slug = Slug Field (Auto create – Based on Title Field)

**Comment Table**

- Post = Foreign Key (to Post table, CASCADE)
- Name = String (Auto Field based on first name and last_name of authenticated user)
- Body = Text Field
- Date = Date Time Field (Auto generate)

**Category Table**

- Category Name = String (max_length=255 characters)
- Related to posts by python list in ‘category_adder.py’

The User table is one of the default arguments in django.contrib.auth.models and there is no need to implement it again:

**User Table**

- Username = String
- FirstName = String
- LastName = String
- Is Staff = a boolean variable meaning whether it has access to admin access or not
- Is Active = A Boolean variable that is active by default and is used to activate the account, and for example, it can be expanded in  the future (to send an activation email)
- Is Super User = This is also a boolean variable and only the admin and the main owner have this capability, also this user can change the access of other admins and edit them.
- Last Login = the last login to the user account - date and time field
- Join Date = The date of joining the site, which is a date field
