from django.db import models


class RSA(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    p = models.CharField(max_length=200, verbose_name="Prime number P")
    q = models.CharField(max_length=200, verbose_name="Prime number Q")
    n = models.CharField(max_length=200, blank=True, null=True, verbose_name="Number N")
    e = models.CharField(max_length=200, verbose_name="Public key")
    d = models.CharField(max_length=200, blank=True, null=True, verbose_name="Private key")

    f = models.CharField(max_length=200, blank=True, null=True, verbose_name="Number F")
    public_key = models.CharField(max_length=200, blank=True, null=True, verbose_name="Public key")
    private_key = models.CharField(max_length=200, blank=True, null=True, verbose_name="Private key")
    a1 = models.CharField(max_length=200, verbose_name="First number")
    b1 = models.CharField(max_length=200, verbose_name="Second number")
    a2 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted first number")
    b2 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted second number")
    a1b1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Multiples of two numbers")
    a2b2 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Multiples of encrypted two numbers")

    def __str__(self):
        return self.title

    def evklid(self, a, b):
        u = [a, 1, 0]
        v = [b, 0, 1]
        t = [0, 0, 0]

        while v[0] != 1:
            q = u[0] % v[0]
            b = u[0] // v[0]
            t[0] = q
            t[1] = u[1] - a * v[1]
            t[2] = u[2] - b * v[2]
            u[0] = v[0]
            u[1] = v[1]
            u[2] = v[2]
            v[0] = t[0]
            v[1] = t[1]
            v[2] = t[2]
        if v[2] < 0:
            return v[2] + a
        return v[2]


class Sezar(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, blank=True, null=True)
    a = models.CharField(max_length=200, verbose_name="First word")
    b = models.CharField(max_length=200, verbose_name="second word")
    k = models.CharField(max_length=200, verbose_name="Key")
    ab = models.CharField(max_length=200, blank=True, null=True, verbose_name="Multiples of two word")
    a1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted first word")
    b1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted second word")
    a1b1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Addition of encrypted two words")
    ba = models.CharField(max_length=200, blank=True, null=True, verbose_name="Decrypt")

    def __str__(self):
        return self.title


# class Paillier(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200, blank=True, null=True)
#     a = models.CharField(max_length=200, verbose_name="First number")
#     b = models.CharField(max_length=200, verbose_name="second number")
#     ab = models.CharField(max_length=200, blank=True, null=True, verbose_name="Multiples of two number")
#     pub = models.CharField(max_length=200, blank=True, null=True, verbose_name="Public key")
#     priv = models.CharField(max_length=200, blank=True, null=True, verbose_name="Private key")
#     a1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted first number")
#     b1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Encrypted second number")
#     a1b1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Addition of encrypted two number")
#     ba = models.CharField(max_length=200, blank=True, null=True, verbose_name="Decrypt")
#
#     def __str__(self):
#         return self.title
