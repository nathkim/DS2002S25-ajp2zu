-- SQL Exercises (With Answers)

-- 1. Retrieve all students who enrolled in 2023.
SELECT * FROM students
WHERE YEAR(enrollmentdate) = 2023;

-- 2. Find students whose email contains 'gmail.com'.
SELECT * FROM students
WHERE email like '%gmail.com';

-- 3. Count how many students are enrolled in the database.
SELECT count(*) AS total_students FROM students;

-- 4. Find students born between 2000 and 2005.
SELECT * FROM students
WHERE YEAR(dateofbirth) BETWEEN 2000 and 2005;

-- 5. List students sorted by last name in descending order.
SELECT * FROM students
ORDER BY lastname DESC;

-- 6. Find the names of students and the courses they are enrolled in.
SELECT Students.studentID, Students.firstname, Students.lastname, Courses.coursename
FROM Students
INNER JOIN Enrollments ON Students.studentid = Enrollments.studentid
INNER JOIN Courses ON Enrollments.courseid = Courses.courseid;

-- 7. List all students and their courses, ensuring students without courses are included (LEFT JOIN).
SELECT Students.studentID, Students.firstname, Students.lastname, Courses.coursename
FROM Students
LEFT JOIN Enrollments ON Students.studentid = Enrollments.studentid
LEFT JOIN Courses ON Enrollments.courseid = Courses.courseid;

-- 8. Find all courses with no students enrolled (LEFT JOIN).
SELECT Courses.coursename
FROM Courses
LEFT JOIN Enrollments ON Courses.courseid = Enrollments.courseid
WHERE Enrollments.studentid IS NULL;

-- 10. List courses and show the number of students enrolled in each course.
SELECT Courses.coursename, count(Enrollments.studentid) AS amount_enrolled
FROM Courses
LEFT JOIN Enrollments ON Courses.courseid = Enrollments.courseid
GROUP BY Courses.coursename;
