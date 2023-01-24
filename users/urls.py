from django.urls import path
from .views import (
    profiles,
    userProfile,
    loginUser,
    logoutUser,
    registerUser,
    userAccount,
    editAccount,
    addSkills,
    updateSkills,
    deleteSkill,
    inbox,
)


urlpatterns = [
    path("", profiles, name="profiles"),
    path("profile/<str:pk>", userProfile, name="user-profile"),
    path("login/", loginUser, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", registerUser, name="register"),
    path("account/", userAccount, name="user-account"),
    path("edit-account/", editAccount, name="edit-account"),
    path("add-skill/", addSkills, name="add-skill"),
    path("update-skill/<str:pk>", updateSkills, name="update-skill"),
    path("delete-skill/<str:pk>", deleteSkill, name="delete-skill"),
    path("inbox/", inbox, name="inbox")
]
