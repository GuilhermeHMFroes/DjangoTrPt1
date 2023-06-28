"""
URL configuration for DjangoTrPt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trabalho import views

urlpatterns = [
    path('controle/', admin.site.urls),

    path('', views.index, name='index'),
    path('aluno/<str:nome>/', views.aluno, name='aluno'),

    #Nota individual para a página contato carregar sem conflito ele deve ter essa estrutura na url 'aluno/<str:nome>/'
    #Se for usar a rota somente como '<str:nome>/' a página que tiver embaixo vai dar erro e deve ser colocada acima desse elemento
    #Recomendo usar a primeira opção pois evita ficar dando esses erros e pode ser que em aplicações onde seja necessário usar várias requisições desse tipo

    path('contato/', views.contato, name='contato'),

]
