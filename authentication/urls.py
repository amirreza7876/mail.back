from authentication import views
from django.urls import path

urlpatterns = [

    # * user managment [Admin permission]
    path('admin/users/', views.AllUser.as_view()),
    path('admin/users/<str:id>/', views.GetUser.as_view()),
    path('admin/login/username/', views.AdminLogin.as_view()),
    path('micro/service/auth/', views.MicroAuth.as_view()),
    
    # Set or Remove Coadmin Role by Admin
    path('setcoadmin/', views.SetCoadminRoleView.as_view()),
    path('delcoadmin/', views.RemoveCoadminRoleView.as_view()),
    
    # ! type can be { user , co-admin  }
    path('register/', views.Register.as_view()),

    # ! type can be { admin , user , co-admin }
    path('login/username/', views.Login.as_view()),
    path('my_info/', views.MyUserInfo.as_view()),
    path('my_info/update/', views.MyInfoUpdate.as_view()),
    path('logout/', views.Logout.as_view()),
    path('delete_my_account/', views.DeleteAccount.as_view()),
    path('re_info/', views.ReInfo.as_view()),

    # ! Address
    path('my/address/', views.MyAddress.as_view()),
    path('address/see/', views.AddressSee.as_view()),

    # ! Company
    path('my/company/', views.MyCompany.as_view()),
    path('company/see/', views.CompanySee.as_view()),

    # ! Social Media
    path('my/social-media/', views.MySocialMedia.as_view()),
    path('social-media/see/', views.SocialMediaSee.as_view()),

    # ! other info
    path('my/info/', views.MyInfo.as_view()),
    path('info/see/', views.InfoSee.as_view()),

    # ! session
    path('session/', views.Session.as_view()),
    path('session/see/', views.SessionSee.as_view()),

    # ! security Questions
    # * user :
    path('user/security-questions/', views.SecurityQuestions.as_view()),
    path('user/security-answer/', views.SecurityAnswer.as_view()),
    path('user/recovery/by-last-password/',
         views.RecoveryByLastPassword.as_view()),
    path('user/recovery/new-password/', views.RecoveryNewPassword.as_view()),

    path('update-token/', views.UpdateToken.as_view()),

]
