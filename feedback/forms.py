from django import forms


class FeedbackForm(forms.Form):
    """
    Simple form for user feedback.
    """
    message = forms.CharField(max_length=400, required=True,
        label="How can we improve this page?",
        widget=forms.TextInput(attrs={'class': 'text span-6'}))
    page = forms.CharField(max_length=400, required=True,
        widget=forms.HiddenInput)


class VoteForm(forms.Form):
    """
    Simple form for voting on user feedback.
    """
    vote = forms.IntegerField(required=True)


class DeleteForm(forms.Form):
    """
    Simple form for deleting user feedback.
    """
    delete = forms.IntegerField(required=True)
