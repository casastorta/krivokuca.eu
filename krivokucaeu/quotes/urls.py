from django.conf.urls import patterns, url
import quotes.views as qv


urlpatterns = patterns('',
    url(r'^author/(\d+)', qv.author_by_id),
)
