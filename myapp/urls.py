from django.urls import path, include

from . import views

urlpatterns = [
    # path("",views.IndexView,name="index"),

    #  path("",views.htmlform,name="htmlform"),

    
       path("",views.InsertPageView,name="InsertPage"),

       path("insert/",views.InsertData,name="Insert"),
       
        path("showpage/",views.ShowPage,name="showpage"),

        path("editpage/<int:pk>",views.EditPage,name="editpage"),

        path("update/<int:pk>",views.UpdateData,name="update"),


        path("delete/<int:pk>",views.DeleteData,name="delete"),
]
