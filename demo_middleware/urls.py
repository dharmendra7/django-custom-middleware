from django.urls import path
from .views import demoForProcessViewMiddleware, demoForProcessExceptionMiddleware

urlpatterns = [
    path("", demoForProcessViewMiddleware, name = 'demo-process-view-middleware'),
    path("exception", demoForProcessExceptionMiddleware, name = 'demo-process-exception-middleware'),
]
