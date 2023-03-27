from rest_framework import serializers

from book.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'genre', 'language', 'price', 'description', 'author', 'discount_price')

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail',

    )
    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return book.price * 25 / 100

    # fields = ('id', 'title', 'isbn', 'description')

    # TODO to implement the author in the book but this only applies to string data types in the author model
    # author = serializers.StringRelatedField()


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'genre', 'language', 'price', 'author', 'discount_price')

# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     birth_day = serializers.DateField(source='date_of_birth')
