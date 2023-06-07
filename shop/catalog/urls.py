from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('earrings/', earrings, name='earrings'),
    path('medallion/', medallion, name='medallion'),
    path('ring/', ring, name='ring'),
    path('post_earring/<int:earrings_id>/', show_post_earring, name='post_earring'),
    path('post_medallion/<int:medallion_id>/', show_post_medallion, name='post_medallion'),
    path('post_ring/<int:ring_id>/', show_post_ring, name='post_ring'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]