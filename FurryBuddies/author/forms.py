from django import forms

from FurryBuddies.author.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }

        labels = {
            'first_name': "First Name:",
            'last_name': "Last Name:",
            'passcode': "Passcode:",
            'pets_number': "Pets Number:",
        }

        help_texts = {
            'passcode': "Your passcode must be a combination of 6 digits",
        }


class AuthorCreateForm(BaseAuthorForm):
    pass


class AuthorEditForm(BaseAuthorForm):
    info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Provide some information about yourself...'}),
        label="Info:"
    )
    image_field = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Enter profile image URL...'}),
        label="Profile Image URL:"
    )

    class Meta(BaseAuthorForm.Meta):
        fields = BaseAuthorForm.Meta.fields + ['info', 'image_field']


class DeleteAuthorForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm that I want to delete my profile and all my posts.")
