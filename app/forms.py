from django.forms import ModelForm
from django.utils import timezone
from .models import Post

class PostForm(ModelForm):
	class Meta:
		model=Post
		fields=['PostName','Post']

	