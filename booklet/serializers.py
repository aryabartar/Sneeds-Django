from rest_framework import serializers
from .models import BookletField, BookletTopic, Booklet, Tag

BOOKLET_SERIALIZER_FIELDS = [
    'title', 'booklet_url', 'information', 'teacher', 'slug', 'number_of_pages', 'format', 'language',
    'booklet_content', 'booklet_image', 'number_of_likes',
    'topic', 'topic_slug', 'topic_url', 'field', 'field_slug',
    'field_url', 'tags',
]


class FieldSerializerWithNoBookletShow(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField()
    field_url = serializers.SerializerMethodField()

    def get_field_url(self, field):
        """ This method returns a complete url for a field. """
        request = self.context.get('request')
        field_url = field.get_absolute_url()
        return request.build_absolute_uri(field_url)

    def get_topics(self, field):
        all_field_topics = field.topics.all()
        return TopicSerializerWithNoBooklet(all_field_topics, many=True, context=self.context).data

    class Meta:
        model = BookletField
        fields = [
            'title', 'field_url', 'slug', 'topics'
        ]


class FieldSerializer(FieldSerializerWithNoBookletShow):
    def get_topics(self, field):
        all_field_topics = field.topics.all()
        return TopicSerializer(all_field_topics, many=True, context=self.context).data


class TopicSerializerWithNoBooklet(serializers.ModelSerializer):
    topic_url = serializers.SerializerMethodField()

    def get_topic_url(self, topic):
        request = self.context.get('request')
        topic_url = topic.get_absolute_url()
        return request.build_absolute_uri(topic_url)

    class Meta:
        model = BookletTopic
        fields = [
            'title', 'topic_url', 'slug',
        ]


class TopicSerializer(TopicSerializerWithNoBooklet):
    field = serializers.SerializerMethodField()
    field_url = serializers.SerializerMethodField()

    topic_booklets = serializers.SerializerMethodField()

    def get_field_url(self, topic):
        request = self.context.get('request')
        field_url = topic.field.get_absolute_url()
        return request.build_absolute_uri(field_url)

    def get_field(self, topic):
        return topic.field.title

    def get_topic_booklets(self, topic):
        topic_booklets = topic.booklets.all()
        topic_booklets_serialize = BookletSerializer(topic_booklets, many=True, context=self.context)
        return topic_booklets_serialize.data

    # TODO: Make this more flexible later
    class Meta:
        model = BookletTopic
        fields = [
            'title', 'topic_url', 'field', 'field_url', 'slug',
            'topic_booklets',
        ]


class TagSerializer(serializers.ModelSerializer):
    tag_url = serializers.SerializerMethodField()

    def get_tag_url(self, tag):
        request = self.context.get('request')
        tag_url = tag.get_absolute_url()
        return request.build_absolute_uri(tag_url)

    class Meta:
        model = Tag
        fields = "__all__"


class TagAndBookletsSerializer(TagSerializer):
    booklets = serializers.SerializerMethodField()

    def get_booklets(self, tag):
        booklets = tag.booklets.all()
        request = self.context["request"]
        return BookletSerializer(booklets, context={"request": request}, many=True).data

    class Meta:
        model = Tag
        fields = "__all__"


class BookletSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    information = serializers.SerializerMethodField()
    booklet_url = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()
    topic_slug = serializers.SerializerMethodField()
    topic_url = serializers.SerializerMethodField()
    field = serializers.SerializerMethodField()
    field_slug = serializers.SerializerMethodField()
    field_url = serializers.SerializerMethodField()

    def get_information(self, booklet):
        information = booklet.topic.information
        return information

    def get_tags(self, booklet):
        tags = booklet.tags.all()
        return TagSerializer(tags, context=self.context, many=True).data

    def get_booklet_url(self, booklet):
        request = self.context.get('request')
        booklet_url = booklet.get_absolute_url()
        return request.build_absolute_uri(booklet_url)

    def get_topic(self, booklet):
        return booklet.topic.title

    def get_topic_slug(self, booklet):
        return booklet.topic.slug

    def get_topic_url(self, booklet):
        request = self.context.get('request')
        topic_url = booklet.topic.get_absolute_url()
        return request.build_absolute_uri(topic_url)

    def get_field(self, booklet):
        return booklet.topic.field.title

    def get_field_slug(self, booklet):
        return booklet.topic.field.slug

    def get_field_url(self, booklet):
        request = self.context.get('request')
        field_url = booklet.topic.field.get_absolute_url()
        return request.build_absolute_uri(field_url)

    class Meta:
        model = Booklet
        fields = [
            'title', 'booklet_url', 'information', 'teacher', 'slug', 'number_of_pages', 'format', 'language',
            'booklet_content', 'booklet_image', 'number_of_likes', 'writer', 'year',
            'topic', 'topic_slug', 'topic_url', 'field', 'field_slug',
            'field_url', 'tags',
        ]
