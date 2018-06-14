Note: This is a rebuild of an internal project I created for my employer. It works, however I didn't want to put the repo pulic for two reasons
* Privacy issues, it wasn't created with the intention of ever been shown to the world, as such there is sensitive information strewn throughout the repo.
* Code quality: this project is inspired by the original, but built from the ground up after learning from many (not all!) of my previous mistakes.

# Django Student Information System

The school I work at doesn't have the funding to purchase a student information system (SIS), so I thought it would be best to build one myself.

During development, the SIS will be created with dummy data, and the student information will be added at a later date when it goes live.

### Short Term Goals

* Notice Board for teachers and students (school-wide and class specific)
* Clean, responsive layout across devices (most likely using Bootstrap)
* Student models organised into classes (naturally) that are easily editable by management.
 Details on students (parent details, address, etc)
* Google sign-in (we use G-Suite as the backend for email/cloud storage)

### Long Term Goals

* Behaviour reports that teachers can submit
* Simple grading system to track student attainment
* Basic timetable system for both teachers and students

### Environment Variables / Config
* export `DJANGO_SECRET_KEY` (your secret key)
* export `SCHOOL_NAME` (used when running `python manage.py createschoolstructure`)
* The next three are for creating test accounts when running `python manage.py createtestusers`. They need to be real Google accounts so you can check out what each type of user can do.
    * export `ADMIN_EMAIL` for admin user
    * export `STAFF_EMAIL` for staff user
    * export `STUDENT_EMAIL` for student user
* `client.json` to be downloaded from [Google App Console](https://console.cloud.google.com/), put it in the base directory (with the `Pipfile`)