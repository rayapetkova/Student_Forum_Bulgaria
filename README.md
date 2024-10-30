# Student_Forum_Bulgaria
#### Deployed version: https://rayapetkova.pythonanywhere.com/

A Django-based application that provides a user-friendly interface for students, teachers, and external users to engage in discussions, share knowledge, and connect with peers. Whether you're seeking academic support, facilitating discussions, or sharing insights, you'll find a welcoming community here.

## ✨ Features
### 🔐 Authentication
- **Register**: Users can sign up to the platform with basic information - first name, last name, email and password.
- **Login**: Users can log in to the platform by providing email and password.
- **Logout**: Users can log out of their account after they have been logged in.

### Role-Based Access
- The platform supports different user roles which are students, teachers and external users, each with specific permissions.
- Students and teachers can add topics and comments.
- External users don't have access to add new topics and can add only comments.
- Superuser has the permission to modify everything on the platform.

### 🏠 Home page
- Section including the title and the description of the platform.
- About section providing information about the application and its developer.

### 📚 Subjects page
- See all subjects added by the superuser.
- A button that allows only the superuser to add new subject.

### Add new subject page
- Only superuser can add a new subject.
- He needs to provide title and description of the new subject.
- After successfully adding the new subject, the user is redirected back to the subjects page.

### 📕 Topics page
- After clicking on a subject, the user will be redirected to the topics page allowing him to see all the topics added for that subject.
- A button that allows the superuser, teachers and students to add a new topic for that subject.

### Add new topic page
- Only the superuser, students and teachers can add a new topic.
- They need to provide tile and description of the new topic.
- After successfully adding the new topic, the user is redirected back to the topics page.

### 🏷️ Comments page
- After clicking a specific topic, the user is redirected to the comments page.
- Displays all the comments for the specific topic.
- A button which allows all types of users to add a new comment including external users.

### Add new comment page
- All types of users are allowed to add a new comment.
- The user only needs to provide the content of his comment.

### 👨‍🦱 Profile Details page
- Every user can see his profile details - email, first name, last name and role.
- A button Edit which allows the user to edit his information.
- A button Delete which allows the user to delete his profile in the platform.

### Edit Profile Details page
- The user can edit his first name, last name and role.

### Delete Profile page
- A page which asks the user for confirmation for deleting his profile.


## 🛠 Technologies
- **Python**
- **Django**
- **PostgreSQL**
- **Docker**
- **Visual Studio Code**
- **PyCharm**
- **DBeaver**
- **GitHub**
- **HTML**
- **Python Decouple**
- **CSS**

## 🧪 Data for testing purposes
- **Students**
  - **Email:** petar_ivanov@hotmail.com; **Password:** petarII123!
  - **Email:** elena_petkova@hotmail.com; **Password:** elenaPP123!
- **Teachers**
  - **Email:** radoslav_zahariev@hotmail.com; **Password:** radoslavZZ123!
  - **Email:** stanislava_angelova@hotmail.com; **Password:** stanislavaAA123!
- **External users**
  - **Email:** daniel_zlatanov@hotmail.com; **Password:** danielZZ123!

---
Thank you for using Studen Forum! If you have any questions or feedback, feel free to reach out!
