from django.db import models

# Create your models here.

# Feature Model
class Feature(models.Model):
    feature_image = models.ImageField(upload_to='static/')
    feature_title = models.CharField(max_length=255)
    feature_details = models.TextField()

    def __str__(self):
        return self.feature_title


# About Model
class About(models.Model):
    about_heading = models.CharField(max_length=255)
    about_details = models.TextField()
    about_image = models.ImageField(upload_to='static/')
    about_point_1_title = models.CharField(max_length=255)
    about_point_1_details = models.TextField()
    about_point_2_title = models.CharField(max_length=255)
    about_point_2_details = models.TextField()
    about_point_3_title = models.CharField(max_length=255)
    about_point_3_details = models.TextField()
    about_point_4_title = models.CharField(max_length=255)
    about_point_4_details = models.TextField()

    def __str__(self):
        return self.about_heading


# Counter Model
class Counter(models.Model):
    counter_image = models.ImageField(upload_to='static/')
    count_1_title = models.CharField(max_length=255)
    count_1_value = models.IntegerField()
    count_2_title = models.CharField(max_length=255)
    count_2_value = models.IntegerField()
    count_3_title = models.CharField(max_length=255)
    count_3_value = models.IntegerField()
    count_4_title = models.CharField(max_length=255)
    count_4_value = models.IntegerField()

    def __str__(self):
        return f"Counter - {self.count_1_title}"


# Service Model
class Service(models.Model):
    service_title = models.CharField(max_length=255)
    service_details = models.TextField()
    service_image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.service_title


# Challenge Model
class Challenge(models.Model):
    challenge_title = models.CharField(max_length=255)
    challenge_image = models.ImageField(upload_to='static/')
    challenge_1_title = models.CharField(max_length=255)
    challenge_1_details = models.TextField()
    challenge_2_title = models.CharField(max_length=255)
    challenge_2_details = models.TextField()
    challenge_3_title = models.CharField(max_length=255)
    challenge_3_details = models.TextField()
    challenge_4_title = models.CharField(max_length=255)
    challenge_4_details = models.TextField()

    def __str__(self):
        return self.challenge_title


# Project Model
class Project(models.Model):
    project_image = models.ImageField(upload_to='static/')
    project_title = models.CharField(max_length=255)
    project_details = models.TextField()

    def __str__(self):
        return self.project_title


# Why Choose Us Model
class WhyChooseUs(models.Model):
    wcu_title = models.CharField(max_length=255)
    wcu_details = models.TextField()
    wcu_image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.wcu_title


# Testimonial Model
class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    client_image = models.ImageField(upload_to='static/')
    client_position = models.CharField(max_length=255)
    client_review = models.TextField()

    def __str__(self):
        return f"Testimonial from {self.client_name}"


# Blog Model
class Blog(models.Model):
    blog_image = models.ImageField(upload_to='static/')
    blog_sub_title = models.CharField(max_length=255)
    blog_title = models.CharField(max_length=255)
    blog_date = models.DateField()
    blog_details = models.TextField()

    def __str__(self):
        return self.blog_title


# Partners Model
class Partner(models.Model):
    partner_logo = models.ImageField(upload_to='static/')

    def __str__(self):
        return "Partner - {self.partner_logo.name}"


# Slider Model
class Slider(models.Model):
    slider_subtitle = models.CharField(max_length=255)
    slider_title = models.CharField(max_length=255)
    slider_details = models.TextField()
    slider_image = models.ImageField(upload_to='static/')
    slider_video_link = models.URLField()

    def __str__(self):
        return self.slider_title
        

#about page
class Header(models.Model):
    header_title = models.CharField(max_length=100)
    header_icon = models.ImageField(upload_to='static/')
    header_heading = models.CharField(max_length=100)
    header_point_1 =models.CharField(max_length=50)
    header_point_2 =models.CharField(max_length=100)


class Security(models.Model):
    securitey_title = models.CharField(max_length=100)
    securitey_subtitle_1 = models.CharField(max_length=100)
    securitey_details_1 = models.CharField(max_length=100)
    securitey_subtitle_2 = models.CharField(max_length=100)
    securitey_details_2 = models.CharField(max_length=100)
    securitey_subtitle_3 = models.CharField(max_length=100)
    securitey_details_3 = models.CharField(max_length=100)

class Cardsection(models.Model):
    cardsection_title = models.CharField(max_length=100)
    cardsection_details = models.CharField(max_length=100)
    cardsection_image = models.ImageField(upload_to='static/')





#service section start page
class Servicesection(models.Model):
  service_title = models.CharField(max_length=100)
  service_icon = models.ImageField(upload_to='static/')
  service_sub_title = models.CharField(max_length=100)
  service_details = models.CharField(max_length=100)
  service_learn_more = models.CharField(max_length=100)




#blog page
class RecentSection(models.Model):
    recent_image = models.ImageField(upload_to='static/')
    recent_details = models.CharField(max_length=100)
    recent_date = models.CharField(max_length=100)
    
class Featuredpost(models.Model):
    featured_image = models.ImageField(upload_to='static/')
    featured_date = models.CharField(max_length=100)
    featured_title = models.CharField(max_length=100)
    featured_details = models.CharField(max_length=100)

class Catepost(models.Model):
    catepost_title = models.CharField(max_length=100)
    catepost_number = models.IntegerField()
#contact us
class contact(models.Model):
    contact_image = models.ImageField(upload_to='static/')


class Contcard(models.Model):
    contcard_image = models.ImageField(upload_to='static/')
    contcard_title = models.CharField(max_length=100)
    contcard_icon = models.ImageField(upload_to='static/')
    contcard_details = models.CharField(max_length=100)

#  py manage.py makemigrations
# py manage.py migrate