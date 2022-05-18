from django.db.models import Q
from rest_framework import serializers
from .models import Book, Author, BookAuthor


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'acquired', 'publication_date', 'thumbnail']

    def create(self, validated_data):
        author_data = validated_data.pop('authors')

        book_instance = Book.objects.create(**validated_data)

        for author in author_data:
            if not Author.objects.filter(Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])):
                book_instance.authors.create(first_name=author['first_name'], last_name=author['last_name'])
            else:
                book_instance.authors.add(Author.objects.get(Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])))
        return book_instance

    def update(self, instance, validated_data):
        author_data = validated_data.pop('authors')
        book_author_id_pool = [bk.author_id for bk in BookAuthor.objects.filter(book_id=instance.id)]
        print(book_author_id_pool)

        for author in author_data:
            if not instance.authors.filter(
                    Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])).exists():
                if Author.objects.filter(
                        Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])):
                    instance.authors.create(first_name=author['first_name'], last_name=author['last_name'])
                else:
                    instance.authors.add(Author.objects.get(
                        Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])))

        for i in book_author_id_pool:
            if i not in [Author.objects.get(
                    Q(first_name__iexact=author['first_name']) | Q(last_name__iexact=author['last_name'])).id for e in
                         author_data]:
                BookAuthor.objects.get(author_id=i).delete()

        return super().update(instance, validated_data)
