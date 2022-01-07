from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_titles = [(c.id, c.get_friendly_title()) for c in categories]

        self.fields['category'].choices = friendly_titles
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'