from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission, AbstractUser


class Level(models.Model):
    label = models.CharField(max_length=100)
    capacity = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.label
    
    def serialize(self):
        return {
            'id': self.id,
            'label': self.label,
            'capacity': self.capacity,
        }

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        permissions = models.ManyToManyField(
            Permission,
            blank=True,
            related_name='myuser_set',
            related_query_name='user',
        )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self):
        return self.email

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }