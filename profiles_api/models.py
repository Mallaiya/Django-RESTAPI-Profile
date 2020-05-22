import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# User Manager Model
class UserManager(BaseUserManager):

    def create_user(self, email, name, dob, password=None):
        if not email:
            raise ValueError('User mush have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, dob=dob)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, dob, password):

        user = self.create_user(email, name, dob, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# User Model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    def get_full_name(self):
        return self.name
    
    def get_avatar_name(self):
        return self.name[0].toUpper()
    
    def __str__(self):
        return self.email
