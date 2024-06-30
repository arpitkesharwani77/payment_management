# subscriptions/models.py

from django.db import models

class ServiceUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_CHOICES = [
        ('MR', 'Mobile Recharge'),
        ('DR', 'DTH Recharge'),
        ('IP', 'Insurance Payment'),
    ]

    PAYMENT_CHOICES = [
        ('UPI', 'UPI'),
        ('IB', 'Internet Banking'),
        ('CP', 'Card Payment'),
    ]

    type = models.CharField(max_length=2, choices=SERVICE_CHOICES, unique=True)
    mode_of_payment = models.CharField(max_length=3, choices=PAYMENT_CHOICES)
    company = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_type_display()} - {self.company}"

class Subscription(models.Model):
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = self.generate_transaction_id()
        super().save(*args, **kwargs)

    def generate_transaction_id(self):
        import uuid
        return str(uuid.uuid4())

    def __str__(self):
        return f"{self.user} - {self.service} - {self.amount}"
