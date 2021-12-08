from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField(max_length = 254)

    def __str__(self):
        return self.Email