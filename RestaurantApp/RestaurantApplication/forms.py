from django import forms
from .models import Utilisateur, Addresses, Restaurant, NoteRestaurant


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

        def save(self, commit=True):
            user = super(UtilisateurForm, self).save(commit=False)
            user.emailUtilisateur = self.cleaned_data['emailUtilisateur']
            if commit:
                user.save()


class RestaurantFrom(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        def save(self, commit=True):
            restaurant = super(RestaurantFrom, self).save(commit=False)
            Restaurant.nomRestaurant = self.cleaned_data['nomRestaurant']
            if commit:
                restaurant.save()


class AdressessFrom(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = '__all__'


class NoteRestaurantForm(forms.ModelForm):
    class Meta:
        model = NoteRestaurant
        fields = '__all__'
