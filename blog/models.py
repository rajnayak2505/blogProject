from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ------------------this is for reverse----------------
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)

    # ------------------------------------------slug is for URL freindly(for SEO)---------------------------------------------------------------------
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author=models.ForeignKey(User, related_name='blog_posts')
    body= models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # -------------this two field is not created databases coz it will updated automatitically when  post is createdor updated-----
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # ---------------------------------------------------------------------------------------------------------------------------
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,default='draft')

    class Meta:
        # ----------------( - this is for descending order)[-publish]-----------------
        ordering=('-publish',)


    def __str__(self):
        return self.title
    # ---------------------------when we use canonical url we have declare get_absolute_url-----------------
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])




























# ----------------------------------------------------------
