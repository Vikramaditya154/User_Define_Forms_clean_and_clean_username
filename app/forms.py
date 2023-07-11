from django import forms

def call_error(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError("First letter should not be a")

def len_error(name):
    if len(name)<=5:
        raise forms.ValidationError('len is less than 5')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[call_error,len_error])
    Sage=forms.IntegerField()
    email=forms.EmailField()
    Re_email=forms.EmailField()
    url=forms.URLField()

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['Re_email']

        if e != re:
            raise forms.ValidationError('emails not matched')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')
