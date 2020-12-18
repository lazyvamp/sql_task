from django.db import models

# Create your models here.

class table1(models.Model):
    userid = models.CharField(max_length=40, blank=False, null=False)
    uploaded_time = models.DateField(auto_now_add=True, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    country_name = models.CharField(max_length=10, blank=False, null=False)
    state_code = models.CharField(max_length=20, blank=False, null=False)
    state_name = models.CharField(max_length=40, blank=False, null=False)

    def get_info(self):
        requested_data = [
            self.userid,
            self.uploaded_time,
            self.city,
            self.price,
            self.year,
            self.country_name,
            self.state_code,
            self.state_name
        ]
        return requested_data
