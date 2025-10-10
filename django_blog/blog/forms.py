from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    # Taggit automatically handles tags as a TaggableManager
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g. travel, lifestyle, tech)",
        widget=forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        # Clear old tags and re-add new ones
        instance.tags.clear()
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
        instance.tags.add(*tag_names)

        return instance


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        max_length=2000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment can't be empty.")
        return content
