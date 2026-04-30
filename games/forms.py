from django import forms
from .models import Review
from .models import ContactMessage


class ReviewForm(forms.ModelForm):
    # behaviour of form
    class Meta:
        # define what model to use
        model = Review
        # show only 'rating' & 'commenr'
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.NumberInput(attrs={
                # appearance of rating fields
                "min": 1,
                "max": 5,
                "placeholder": "1 to 5",
            }),
            "comment": forms.Textarea(attrs={
                # 4 line tall (for now)
                "rows": 4,
                # placeholder text to guide user
                "placeholder": "Write your review here...",
            }),
        }


class ContactMessageForm(forms.ModelForm):
    # overide defoult form
    topic = forms.ChoiceField(
        # mandating choises (added by me)
        choices=ContactMessage.TOPIC_CHOICES,
        # radio chooices, not drop down
        widget=forms.RadioSelect,
        # one option must be chosen - failsafe
        required=True,
    )

    class Meta:
        model = ContactMessage
        fields = ["topic", "message"]
        widgets = {
            # I hate dropd downs menus!!! "topic": forms.Select(),
            # cannot be selected by default "topic": forms.RadioSelect(), 
            "message": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Write your message here...",
            }),
        }
