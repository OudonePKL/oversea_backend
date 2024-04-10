from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = 'users'

urlpatterns = [
    path("", views.UserListView.as_view(), name='user-list'),
    path("<int:pk>", views.UserDetailsView.as_view(), name='user-details'),
    path("current", views.CurrentUserView.as_view(), name='current-user'),
    path('users/<int:id>/delete/', views.UserDetailsView.as_view(), name='user-delete'),

    # join the membership
    path("signup", views.SignupView.as_view(), name="signup"),
    path('create-superuser', views.CreateSuperuserView.as_view(), name='create-superuser'),
    path('admin-users/<int:user_id>/get', views.GetAdminUserByIdView.as_view(), name='get-admin-user-by-id'),
    path('admin-users/<int:user_id>', views.DeleteAdminUserView.as_view(), name='delete-admin-user'),
    path('admin-users/<int:user_id>/update', views.UpdateAdminUserView.as_view(), name='update-admin-user'),
    path('admin-users', views.ListAdminUsersView.as_view(), name='list-admin-users'),
    path("seller-signup", views.SellerSignup.as_view(), name="seller_google_signup"),
    # Email Authentication
    path("send-email", views.SendEmail.as_view(), name="send_email"),
    path("check-email", views.CheckEmailView.as_view(), name="check_email"),
    # social login
    path("social", views.SocialUrlView.as_view(), name="social_login"),
    path("google", views.GoogleLoginView.as_view(), name="google_login"),
    # log in
    path("signin", views.LoginView.as_view(), name="signin"),
    path("check-token", views.CheckToken.as_view(), name="CheckToken"),
    # User information related
    path("my-page", views.UserView.as_view(), name="my_page"),
    path("my-page/profile", views.ChangeUserProfile.as_view(), name="ChangeUserProfile"),
    # page render
    path("page", views.my_page_render, name="my_page_render"),
    path("find", views.find_password_render, name="find_password_render"),
    path("more", views.more_page_render, name="more_page_render"),
    path("profile", views.user_profile_render, name="user_profile_render"),
    path("change-seller", views.change_seller_render, name="change_seller_render"),
    path("intro", views.intro_render, name="intro_render"),
    path("terms", views.term_render, name="intro_render"),
    path("policy", views.policy_render, name="intro_render"),
]
