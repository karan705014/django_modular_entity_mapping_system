from django.db import models
from vendor.models import Vendor
from product.models import Product
from common.models import TimeStampModel


class VendorProductMapping(TimeStampModel):

    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)

    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.product.name}"
