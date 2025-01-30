# Course Management System

This is a Django-based Course Management System that allows users to manage courses, instructors, classrooms, and student enrollments. The system provides a user-friendly interface for administrators to add, edit, and delete courses, as well as manage student registrations and course schedules.

## Table of Contents

- [Course Management System](#course-management-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Models](#models)
  - [Forms](#forms)
  - [Views](#views)
  - [URLs](#urls)
  - [Templates](#templates)
  - [Static Files](#static-files)
  - [Contributing](#contributing)

## Features

- **User Authentication**: Students can register and log in to the system.
- **Course Management**: Admins can add, edit, and delete courses.
- **Classroom Management**: Admins can manage classrooms and their capacities.
- **Enrollment Management**: Students can enroll in courses, and admins can manage enrollments.
- **Schedule Management**: Admins can create and manage course schedules.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/course_management_system.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the migrations:

```bash
python manage.py migrate
```

4. Create a superuser for the admin interface:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

## Usage

- Visit `http://localhost:8000/` to access the home page.
- Log in as a student or admin to access the respective dashboards.
- Use the navigation menu to access different parts of the system.

## Models

The system includes several models to represent the data:

- `Course`: Represents a course with details like name, code, credits, capacity, etc.
- `Department`: Represents a department or faculty.
- `Instructor`: Represents an instructor associated with a department.
- `Classroom`: Represents a classroom with a capacity and associated department.
- `CourseClassroom`: Represents a course offered in a specific classroom.
- `Prerequisite`: Represents a prerequisite course for another course.
- `Corequisite`: Represents a corequisite course for another course.
- `CourseSchedule`: Represents the schedule for a course, including the day, start time, and end time.
- `Enrollment`: Represents a student's enrollment in a course.
- `WeeklySchedule`: Represents a student's weekly schedule.

## Forms

The system uses Django forms to handle data input and validation:

- `CourseForm`: Used for adding and editing courses.
- `StudentForm`: Used for student registration and profile editing.
- `CustomUserForm`: Used for creating and managing user accounts.
- `CourseScheduleForm`: Used for creating and editing course schedules.
- `CourseClassroomForm`: Used for adding and managing course-classroom relationships.

## Views

The system includes various views to handle user requests:

- `Home`: Displays the home page.
- `StudentProfileView`: Displays the student's profile.
- `StudentProfileEditView`: Allows students to edit their profile.
- `course_selection_view`: Allows students to select courses.
- `drop_course`: Allows students to drop a course.
- `get_enrolled_courses`: Retrieves a list of courses in which a student is enrolled.
- `enroll_course`: Handles course enrollment for students.
- `get_department_courses`: Retrieves a list of courses offered by a department.
- `weekly_schedule_view`: Displays the student's weekly schedule.

## URLs

The system's URL patterns are defined in the `urls.py` files:

- `core/urls.py`: Contains the main URL patterns for the application.
- `course/urls.py`: Contains URL patterns related to course management.
- `course_management/urls.py`: Contains URL patterns for administrative tasks.
- `accounts/urls.py`: Contains URL patterns for user authentication and registration.

## Templates

The system uses Django templates to render HTML pages:

- Templates are organized in the `templates` directory.
- The `include` directory contains reusable template components.
- The `shared` directory contains shared templates used across the application.

## Static Files

The system includes static files for styling and client-side scripting:

- CSS files are located in the `static/css` directory.
- JavaScript files are located in the `static/js` directory.

## Contributing

Contributions to the Course Management System are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to the repository.
5. Create a pull request.