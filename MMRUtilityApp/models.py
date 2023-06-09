from django.db import models
from django.db.models import CharField


# Create your models here.
class MMRmodel(models.Model):
    # def __str__(self):
    #      return self.cms_contract_id

    cms_contract_id: CharField = models.CharField(max_length=5)
    run_date = models.DateField()
    pay_proc_period = models.CharField(max_length=6)
    hic_no = models.CharField(max_length=12)
    mbr_last_name = models.CharField(max_length=7)
    mbr_first_init = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    mbr_dob = models.DateField()
    age_group = models.CharField(max_length=4)
