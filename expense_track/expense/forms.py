from django import forms
class CredentialsForm(forms.Form):
    email = forms.EmailField()
    mob = forms.CharField(max_length=15)
    pwd = forms.CharField(widget=forms.PasswordInput)
class UserDetailsForm(forms.Form):
    name = forms.CharField(max_length = 50)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    profile_image = forms.ImageField(required=False)
    occupation = forms.CharField(max_length = 50)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    m_s = forms.CharField(max_length = 20)
    income = forms.CharField(max_length = 100)
class ExpenseForm(forms.Form):
    category = forms.ChoiceField(choices=[('Fuel', 'Fuel'), ('Shopping', 'Shopping'), ('Travel', 'Travel'),('Withdraw','Withdraw'),('Food','Food'),('grocery','grocery'),('Beautyparlor','Beautyparlor'),('EMI','EMI'),('Hospital','Hospital'),('Others','Others')], required = False)
    write_category = forms.CharField(max_length = 100,required = False,widget =forms.TextInput(attrs = {'placeholder':'Write Category'}))
    amount = forms.IntegerField(widget =forms.TextInput(attrs = {'placeholder':'Enter Amount'}))
