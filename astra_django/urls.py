from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('qa_app.urls')),
    path('datasets/', include('data_sets.urls'))
]
