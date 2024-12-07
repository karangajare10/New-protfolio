from django.shortcuts import render
from website import models
# Create your views here.
def home(req):
   features = models.Feature.objects.all()
   about = models.About.objects.all()
   counter = models.Counter.objects.all()
   service = models.Service.objects.all()
   slider = models.Slider.objects.all()
   challenge = models.Challenge.objects.all()
   project = models.Project.objects.all()
   whychooseus = models.WhyChooseUs.objects.all()
   Testimonial = models.Testimonial.objects.all()
   blog = models.Blog.objects.all()






   obj  = {"features":features,"about":about,"counter":counter,"service":service,"slider":slider,"challenge":challenge,"project":project,"whychooseus":whychooseus,"Testimonial":Testimonial,"blog":blog}


   return render(req,"home.html",obj)

def about(req):
    header = models.Header.objects.all()
    counter = models.Counter.objects.all()
    security = models.Security.objects.all()
    cardsection = models.Cardsection.objects.all()

    obj = {"header":header,"counter":counter,"security":security,"cardsection":cardsection}
    return render(req,"about.html",obj)

def services(req):
   header = models.Header.objects.all()
   servicesection = models.Servicesection.objects.all()
   counter = models.Counter.objects.all()
   header = models.Header.objects.all()

   obj = {"header":header,"servicesection":servicesection,"counter":counter,"header":header}
   return render(req,"services.html",obj)

def blog(req):
    recentsection = models.RecentSection.objects.all()
    featuredpost = models.Featuredpost.objects.all()
    catepost = models.Catepost.objects.all()

    obj = {"recentsection":recentsection,"featuredpost":featuredpost,"catepost":catepost}
    return render(req,"blog.html",obj)

def contact(req):
    contcard = models.Contcard.objects.all()

    obj = {"contcard":contcard}
    return render(req,"contact.html",obj)