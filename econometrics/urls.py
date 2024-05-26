from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Econometrics"
admin.site.site_title = "Econometrics Administrator"
admin.site.index_title = "Econometrics Administrator Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webApp.urls'))
]
