from django.conf.urls import url
from django.contrib import admin
from search import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

	#Home page
    url(r'^$', views.index, name='index'),
	
    #Search results
    url(r'^search/', views.get_name, name='search-results'),

    #download csv
    url(r'^download/', views.download_csv, name='download'),
    
] 