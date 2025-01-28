document.addEventListener('DOMContentLoaded', function() {
    const departmentSelect = document.getElementById('department-select');
    const coursesTable = document.getElementById('courses-table');
    const coursesTbody = document.getElementById('courses-tbody');

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
                                <button class="btn btn-primary btn-sm enroll-btn" 
                                        data-course-id="${course.id}">
                                    انتخاب درس
                                </button>
                            </td>
                        `;
                        coursesTbody.appendChild(row);
                    });

                    // اضافه کردن event listener برای دکمه‌های انتخاب درس
                    document.querySelectorAll('.enroll-btn').forEach(button => {
                        button.addEventListener('click', enrollCourse);
                    });
                });
        } else {
            coursesTable.style.display = 'none';
        }
    });

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
                alert(data.message);
                // به‌روزرسانی لیست دروس
                departmentSelect.dispatchEvent(new Event('change'));
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            alert('خطا در ثبت درس');
        });
    }

    // تابع کمکی برای گرفتن CSRF token
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
});