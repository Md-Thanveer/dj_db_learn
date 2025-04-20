from django.db import models

# One-to-One Relationship
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return f"Profile of {self.teacher.name}"


# One-to-Many (ForeignKey) Relationship
class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title


# Many-to-Many Relationship
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(
        Course,
        related_name='students'
    )

    def __str__(self):
        return self.name
