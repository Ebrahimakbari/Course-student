document.addEventListener('DOMContentLoaded', function() {
    const departmentSelect = document.getElementById('department-select');
    const coursesTable = document.getElementById('courses-table');
    const coursesTbody = document.getElementById('courses-tbody');
    const enrolledCoursesTbody = document.getElementById('enrolled-courses-tbody');

    // تابع نمایش دروس انتخاب شده
    function loadEnrolledCourses() {
        fetch('/get-enrolled-courses/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    enrolledCoursesTbody.innerHTML = '';
                    data.courses.forEach(course => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${course.code}</td>
                            <td>${course.name}</td>
                            <td>${course.credits}</td>
                            <td>${course.instructor}</td>
                            <td>
                                <button class="btn btn-danger btn-sm drop-btn" 
                                        data-course-id="${course.id}">
                                    حذف درس
                                </button>
                            </td>
                        `;
                        enrolledCoursesTbody.appendChild(row);
                    });

                    // اضافه کردن event listeners برای دکمه‌های حذف
                    document.querySelectorAll('.drop-btn').forEach(button => {
                        button.addEventListener('click', dropCourse);
                    });

                    // به‌روزرسانی وضعیت دکمه‌ها در جدول دروس موجود
                    updateEnrollButtons(data.courses);
                }
            })
            .catch(error => {
                console.error('Error loading enrolled courses:', error);
            });
    }

    // تابع به‌روزرسانی دکمه‌ها
    function updateEnrollButtons(enrolledCourses) {
        const enrolledIds = enrolledCourses.map(course => course.id);
        document.querySelectorAll('#courses-tbody [data-course-id]').forEach(button => {
            const courseId = parseInt(button.dataset.courseId);
            if (enrolledIds.includes(courseId)) {
                button.classList.remove('btn-primary');
                button.classList.add('btn-danger');
                button.textContent = 'حذف درس';
                button.removeEventListener('click', enrollCourse);
                button.addEventListener('click', dropCourse);
            } else {
                button.classList.remove('btn-danger');
                button.classList.add('btn-primary');
                button.textContent = 'انتخاب درس';
                button.removeEventListener('click', dropCourse);
                button.addEventListener('click', enrollCourse);
            }
        });
    }

    // Event listener برای تغییر دانشکده
    departmentSelect.addEventListener('change', function() {
        const departmentId = this.value;
        if (departmentId) {
            fetch(`/get-department-courses/?department_id=${departmentId}`)
                .then(response => response.json())
                .then(data => {
                    coursesTbody.innerHTML = '';
                    coursesTable.style.display = 'table';
                    
                    data.courses.forEach(course => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${course.code}</td>
                            <td>${course.name}</td>
                            <td>${course.credits}</td>
                            <td>${course.instructor__first_name} ${course.instructor__last_name}</td>
                            <td>${course.capacity}/${course.initial_capacity}</td>
                            <td>
                                <button class="btn btn-primary btn-sm" 
                                        data-course-id="${course.id}">
                                    انتخاب درس
                                </button>
                            </td>
                        `;
                        coursesTbody.appendChild(row);
                    });

                    // به‌روزرسانی وضعیت دکمه‌ها
                    loadEnrolledCourses();

                    // اضافه کردن event listeners
                    document.querySelectorAll('#courses-tbody [data-course-id]').forEach(button => {
                        button.addEventListener('click', enrollCourse);
                    });
                });
        } else {
            coursesTable.style.display = 'none';
        }
    });

    // تابع انتخاب درس
    function enrollCourse(e) {
        e.preventDefault();
        const courseId = this.dataset.courseId;
        
        fetch('/enroll-course/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `course_id=${courseId}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showNotification(data.message, 'success');
                loadEnrolledCourses();
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(error => {
            showNotification('خطا در ثبت درس', 'error');
        });
    }

    // تابع حذف درس
    function dropCourse(e) {
        e.preventDefault();
        if (!confirm('آیا از حذف این درس اطمینان دارید؟')) {
            return;
        }

        const courseId = this.dataset.courseId;
        
        fetch('/drop-course/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `course_id=${courseId}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showNotification(data.message, 'success');
                loadEnrolledCourses();
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(error => {
            showNotification('خطا در حذف درس', 'error');
        });
    }

    function showNotification(message, type) {
        const notificationDiv = document.createElement('div');
        notificationDiv.className = `alert alert-${type === 'success' ? 'success' : 'danger'} notification`;
        notificationDiv.style.position = 'fixed';
        notificationDiv.style.top = '20px';
        notificationDiv.style.right = '20px';
        notificationDiv.style.zIndex = '1000';
        notificationDiv.textContent = message;
        
        document.body.appendChild(notificationDiv);
        
        setTimeout(() => {
            notificationDiv.remove();
        }, 3000);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // فراخوانی اولیه دروس انتخاب شده
    loadEnrolledCourses();
});