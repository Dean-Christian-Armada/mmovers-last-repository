from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# Defines fields that get serialized/derserialized
# A simple way to share snippets of text and code with others.
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
	code = serializers.CharField(style={'base_template':'textarea.html'})
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	# def create(self, validated_data):
	# 	"""
	# 	Create and return a new `Snippet` instance, givern the validated data.
	# 	"""
	# 	return Snippet.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	"""
	# 	Update and return an existing `Snippet` instance, given the  validated data.
	# 	"""
	# 	instance.title = validated_data.get('title', instance.title)
	# 	instance.code = validated_data.get('code', instance.code)
	# 	instance.linenos = validated_data.get('linenos', instance.linenos)
	# 	instance.language = validated_data.get('language', instance.language)
	# 	instance.style = validated_data.get('style', instance.style)
	# 	instance.save()
	# 	return instance
	class Meta:
		model = Snippet
		fields = ('pk', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	# snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all)
	snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')