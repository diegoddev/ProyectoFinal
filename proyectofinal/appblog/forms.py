from django import forms

class PostFormulario(forms.Form):

    titulo = forms.CharField(label='Título')
    subtitulo = forms.CharField(label='Subtítulo', widget=forms.Textarea(attrs={"rows": 2}))
    autor = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea(attrs={"rows": 8}))
    imagen = forms.ImageField()


