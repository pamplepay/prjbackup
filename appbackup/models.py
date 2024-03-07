from django.db import models

class PartTbl(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'part_tbl'

class RegionTbl(models.Model):
    name = models.CharField(max_length=6)

    class Meta:
        db_table = 'region_tbl'

class BackupTbl(models.Model):
    part = models.ForeignKey(PartTbl, on_delete=models.CASCADE, db_column='part_id')
    region = models.ForeignKey(RegionTbl, on_delete=models.CASCADE, db_column='region_id')  # 'region_id' -> 'region'으로 변경
    detailregion = models.CharField(max_length=30, default='null')
    pharmacy = models.CharField(max_length=30)
    businessnum = models.CharField(max_length=20)
    owner = models.CharField(max_length=10)
    phonenum = models.CharField(max_length=20)
    contractdate = models.DateField()
    expirydate = models.DateField()
    category = models.CharField(max_length=20, default='null')
    listprice = models.IntegerField()
    discount = models.IntegerField()
    salesamount = models.IntegerField()
    cost = models.IntegerField()
    profit = models.IntegerField()

    @property
    def region_name(self):
        return self.region.name if self.region else None

    class Meta:
        db_table = 'backup_tbl'
