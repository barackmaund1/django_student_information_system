# Django Student Information System

The school I work at doesn't have the funding to purchase a student information system (SIS), so I thought it would be best to build one myself.

During development, the SIS will be created with dummy data, and the student information will be added at a later date when it goes live.

### Short Term Goals

- Notice Board for teachers and students (school-wide and class specific)
- Clean, responsive layout across devices (most likely using Bootstrap)
- Student models organised into classes (naturally) that are easily editable by management.
- Details on students (parent details, address, etc)
- Google sign-in (we use G-Suite as the backend for email/cloud storage)

### Long Term Goals

- Behaviour reports that teachers can submit
- Simple grading system to track student attainment
- Basic timetable system for both teachers and students

### Environment Variables / Config
- export `DJANGO_SECRET_KEY` (your secret key)
- export `SCHOOL_NAME` (used when running `python manage.py createschoolstructure`)
- `client.json` to be downloaded from [Google App Console](https://console.cloud.google.com/), put it in the base directory (with the `Pipfile`)