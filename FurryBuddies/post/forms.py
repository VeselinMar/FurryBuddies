from django import forms
from .models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'context']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
                'maxlength': 50,
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Share your funniest furry photo URL!',
            }),
            'context': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...',
            }),
        }


class CreatePostForm(BasePostForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("Oops! That title is already taken. How about something fresh and fun?")
        return title


class EditPostForm(BasePostForm):
    pass


class DeletePostForm(BasePostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'
