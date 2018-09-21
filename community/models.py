from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=250, default="")
    type = models.CharField(max_length=200, default="")
    density = models.FloatField(default=0)
    area = models.FloatField(default=0)
    kindergarten = models.IntegerField(default=0)
    primary_school = models.IntegerField(default=0)
    secondary_school = models.IntegerField(default=0)
    p12_school = models.IntegerField(default=0)
    other_school = models.IntegerField(default=0)
    born_overseas = models.FloatField(default=0)
    except_eng = models.FloatField(default=0)
    culture_group1_name = models.CharField(max_length=250, default="")
    culture_group2_name = models.CharField(max_length=250, default="")
    culture_group3_name = models.CharField(max_length=250, default="")
    culture_group4_name = models.CharField(max_length=250, default="")
    culture_group1_per = models.FloatField(default=0)
    culture_group2_per = models.FloatField(default=0)
    culture_group3_per = models.FloatField(default=0)
    culture_group4_per = models.FloatField(default=0)
    child_protection = models.IntegerField(default=0)
    community_health = models.IntegerField(default=0)
    homeless = models.IntegerField(default=0)
    disability = models.IntegerField(default=0)
    mental_health = models.IntegerField(default=0)
    human = models.IntegerField(default=0)
    dental = models.IntegerField(default=0)
    general_practice = models.IntegerField(default=0)
    pharmacy = models.IntegerField(default=0)
    allied_health = models.IntegerField(default=0)
    complementary_health = models.IntegerField(default=0)
    residential_aged_care = models.IntegerField(default=0)
    licensed_aged_care = models.IntegerField(default=0)
    nearest_health = models.CharField(max_length=250, default="")
    dis_nearest_health = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Language(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    language = models.CharField(max_length=200, default="")
    count = models.IntegerField(default=0)
    sub_location = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.language


class Country(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, default="")
    code = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.country


class Suburblocation(models.Model):
    postcode = models.IntegerField(default=0)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return str(self.postcode) + "," + str(self.community.name)


class School(models.Model):
    name = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=50, default="")
    address_line = models.CharField(max_length=200, default="")
    address_town = models.CharField(max_length=100, default="")
    postcode = models.IntegerField(default=0)
    contact = models.CharField(max_length=50, default="")
    education_sector = models.CharField(max_length=50, default="")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)


class Hospital(models.Model):
    name = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=50, default="")
    street_number = models.CharField(max_length=50, default="")
    road_name = models.CharField(max_length=200, default="")
    road_type = models.CharField(max_length=200, default="")
    suburb = models.CharField(max_length=200, default="")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)





