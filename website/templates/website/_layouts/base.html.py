< !DOCTYPE
html >
< html >
{ % load
static %}
< head >
< title > { % block
title %}Gerenciador
de
Funcionários
{ % endblock %} < / title >

< !-- Estilos -->
< link
rel = "shortcut icon"
type = "image/png"
href = "{% static 'website/img/favicon.png' %}" >
< link
rel = "stylesheet"
href = "{% static 'website/css/bootstrap.min.css' %}" >
< link
rel = "stylesheet"
href = "{% static 'website/css/master.css' %}" >
{ % block
styles %}{ % endblock %}
< / head >

< body >
< nav


class ="navbar navbar-expand-lg navbar-light bg-white" >

< a


class ="navbar-brand" href="{% url 'website:index' %}" >

< img
src = "{% static 'website/img/favicon.png' %}"
height = "45px" >
< / a >
< button


class ="navbar-toggler" type="button" data-toggle="collapse" data-target="#conteudo-navbar"


aria - controls = "conteudo-navbar"
aria - expanded = "false"
aria - label = "Ativar navegação" >
< span


class ="navbar-toggler-icon" > < / span >

< / button >

< div


class ="collapse navbar-collapse" id="conteudo-navbar" >

< ul


class ="navbar-nav mr-auto" >

< li


class ="nav-item active" >

< a


class ="nav-link" href="{% url 'website:index' %}" > Página Inicial < / a >

< / li >
< li


class ="nav-item" >

< a


class ="nav-link" href="{% url 'website:lista_funcionario' %}" > Funcionários < / a >

< / li >
< / ul >
< / div >
< / nav >

{ % block
conteudo %}{ % endblock %}

< !-- Scripts -->
< script
src = "{% static 'website/js/jquery.min.js' %}" > < / script >
< script
src = "{% static 'website/js/bootstrap.min.js' %}" > < / script >
{ % block
scripts %}{ % endblock %}
< script
src = "{% static 'website/js/scripts.js' %}" > < / script >
< / body >
< / html >
