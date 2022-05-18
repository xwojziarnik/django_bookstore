from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the book")
    authors = models.ManyToManyField('Author', through="books.BookAuthor")
    acquired = models.BooleanField(default=False, verbose_name="Status of the book: acquired?")
    publication_date = models.DateField(verbose_name="Publication date of the book.", null=True , blank=True)
    thumbnail = models.URLField(blank=True, verbose_name="URL to thumbnail of the book")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="The contributors name/names")
    last_name = models.CharField(max_length=50, verbose_name="The contributors last name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
