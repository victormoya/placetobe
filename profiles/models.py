from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        user.email_user('Subject', 'here the message', 'noreply@placetobe.com')
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email', unique=True)
    avatar = models.ImageField(upload_to='images/profile', default='images/default_usr.png')
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Additional information about personal data
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    hometown = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    category1 = models.ForeignKey('events.Category', related_name='profile', null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # User's short name is the first part of their email address
        return self.email.split('@')[0]

    def get_interest_list(self):
        """
        Get user interest based on events assistance
        """
        assistance = self.assists.all()
        interest_list = map(lambda x: x.event.category.name, assistance)
        return sorted(set(interest_list))

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return self.get_short_name()
