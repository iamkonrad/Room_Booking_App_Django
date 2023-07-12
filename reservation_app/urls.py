from django.contrib import admin
from django.urls import path
from reservation_app.views import (
    AddRoomView,
    RoomListView,
    DeleteRoomView,
    ModifyRoomView,
    ReservationView,
    RoomDetailsView,
    SearchView,
)

urlpatterns = [
    path('room/new/', AddRoomView.as_view(), name="add-room"),
    path('', RoomListView.as_view(), name="room-list"),
    path('room/delete/<int:room_id>/', DeleteRoomView.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>/', ModifyRoomView.as_view(), name="modify-room"),
    path('room/reserve/<int:room_id>/', ReservationView.as_view(), name="reserve-room"),
    path('room/<int:room_id>/', RoomDetailsView.as_view(), name="room-details"),
    path('search/', SearchView.as_view(), name="search-room"),
]