from django.dispatch import receiver
from django.db.models.signals import pre_save
from app_groups.models import Group, Homework
from django.utils.text import slugify


@receiver(pre_save, sender=Group)
def generate_slug_for_post(sender, instance, **kwargs):
    if not instance.slug:
        original_slug = slugify(instance.name)
        slug = original_slug
        count = 0
        while Group.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{count}"
            count += 1

        instance.slug = slug

    
@receiver(pre_save, sender=Homework)
def generate_slug_for_post(sender, instance, **kwargs):
    if not instance.slug:
        original_slug = slugify(instance.title)
        slug = original_slug
        count = 0
        while Homework.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{count}"
            count += 1

        instance.slug = slug

        