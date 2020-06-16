from django import forms


class SongFileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput())  # for creating file input

    def clean(self):
        cleaned_data = super().clean()
        # TODO: Make sure its a good music file here
        file = cleaned_data.get("file")
        #print(file)
        #raise forms.ValidationError("CC'ing yourself.")
