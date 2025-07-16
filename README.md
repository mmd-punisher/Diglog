# Diglog

A Complete Weblog Project Based on Django

**Developer:** [Mohammad Mousapour](https://github.com/mmd-punisher)

---

## 📌 General Description

Diglog is a full-featured web-based blog system built using Django (Python). The project follows the MVT architectural pattern and employs object-oriented programming principles with Class-Based and Generic Views. It includes both frontend and backend components, designed to provide a complete blogging platform.

---

## ⚙️ Technologies Used

- Django (Python)
- Django Channels (for scalability)
- MySQL
- HTML, CSS, Bootstrap
- JavaScript
- CKEditor (Rich Text Editor)
- Git

---

## 🚀 Key Features

### Frontend

- List and pagination of all posts (newest first)
- Sidebar with navigation (categories, profile, etc.)
- Search functionality
- Responsive design

### User Management

- User registration and login (username, password, email)
- Profile creation and editing (bio, social links, profile image)
- Password change
- Tracking last login and connection times

### Post Management

- Create, edit, delete posts (title, image, short description, main text)
- Rich-text editing using CKEditor (formatting, images, graphs, emojis, etc.)
- Categorize posts
- View count tracking
- Like system for logged-in users
- Comment system (only for registered users)

### Admin Panel

- Full post and user management
- Filter, search, and sort data
- View who has seen each post (tracking via admin)
- Dedicated admin login

### Database Structure

- **Posts:** title, author, image, short description, full body, category, likes, timestamps, slug
- **Profiles:** user, biography, profile picture, web/social links
- **Comments:** linked to posts, with body and timestamps
- **Categories:** organized via Python list for dynamic association

---

## 🎯 Project Goals

- Provide a stable, extensible, and scalable blogging platform  
- Practice Django’s MVT pattern and Class-Based Views in a real-world project  
- Enable rich user interaction through profiles, comments, likes, and admin management  

---

## 🔗 Project Link

[GitHub Repository](https://github.com/mmd-punisher/Diglog)

