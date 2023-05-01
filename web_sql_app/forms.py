from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'type': "inputUsername", 
            'id': "floatingInput"
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'type': "password",
            'id': "floatingPassword",
        })
    )

class Sp_get_amcom(forms.Form):
    
    fcard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Номер карты",
            'id': "fcard",
            'type': "number",
        }),
    )

    ncard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Серия карты",
            'id': "ncard",
            'type': "text",
        }),
    )

    scard = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"scard",
            'id': "scard",
            'type': "text",
        }),
    )

class Sp_get_talon(forms.Form):
    
    fcard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Номер карты",
            'id': "fcard",
            'type': "number",
        }),
    )

    ncard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Серия карты",
            'id': "ncard",
            'type': "text",
        }),
    )

    scard = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"scard",
            'id': "scard",
            'type': "text",
        }),
    )

class Sp_accept_amcom_pay(forms.Form):
    
    fcard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Номер карты",
            'id': "fcard",
            'type': "number",
        }),
    )

    ncard = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"Серия карты",
            'id': "ncard",
        }),
    )
    amcom = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"amcom",
            'id': "amcom",
            'type': "number",
        }),
    )
    kassid = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"kassid",
            'id': "kassid",
            'type': "number",
        }),
    )
    sum = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"sum",
            'id': "sum",
            'type': "number",
        }),
    )
    data = forms.DateTimeField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"data",
            'id': "data",
            'type': "date"
        }),
    )  
    #data = forms.DateTimeField(label='Дата рождения', 
    #    widget=forms.DateInput(format='%d-%m-%Y', 
    #            attrs={'type': 'date'}), 
    #            required=True)

    vid = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"vid",
            'id': "vid",
            'type': "number",
        }),
    )
    kol = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':"kol",
            'id': "kol",
            'type': "number",
        }
        ),
    )
    