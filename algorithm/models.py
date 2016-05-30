# from django.db import models
#
#
# class RSA(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     p = models.CharField(max_length=200, verbose_name="Prime number P")
#     q = models.CharField(max_length=200, verbose_name="Prime number Q")
#     n = models.CharField(max_length=200, verbose_name="Number N")
#     e = models.CharField(max_length=200, verbose_name="Public key")
#     d = models.CharField(max_length=200, verbose_name="Private key")
#
#     f = models.CharField(max_length=200, verbose_name="Number f")
#     public_key = models.CharField(max_length=200, verbose_name="Public key")
#     private_key = models.CharField(max_length=200, verbose_name="Private key")
#     a1 = models.CharField(max_length=200, verbose_name="First number")
#     b1 = models.CharField(max_length=200, verbose_name="Second number")
#     a2 = models.CharField(max_length=200, verbose_name="Encrypted first number")
#     b2 = models.CharField(max_length=200, verbose_name="Encrypted second number")
#     a1b1 = models.CharField(max_length=200, verbose_name="Multiples of two numbers")
#     a2b2 = models.CharField(max_length=200, verbose_name="Multiples of encrypted two numbers")
#
#     def __str__(self):
#         return self.title