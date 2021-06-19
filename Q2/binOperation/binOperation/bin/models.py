from django.db import models


# Create your models here.


class Bin(models.Model):
    # id is automatically created as PK
    latitude = models.FloatField(default=0, verbose_name="latitude")
    longitude = models.FloatField(default=0, verbose_name="longitude")
    collection_frequency = models.IntegerField(default=0, verbose_name="collection frequency")
    last_collection = models.DateTimeField(auto_now_add=True, verbose_name="last collection time")

    def __str__(self):
        return str(self.id)


class Operation(models.Model):
    # id is automatically created as PK
    name = models.CharField(max_length=20, verbose_name="Operation name")

    def __str__(self):
        return self.name


class Execution(models.Model):
    # id is automatically created as PK
    bin_id = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="bin", editable=True, verbose_name="bin id")
    Op_id = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="operation", editable=True,
                              verbose_name="operation id")

    def __str__(self):
        return str(self.id)
