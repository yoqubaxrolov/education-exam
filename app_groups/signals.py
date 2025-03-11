from django.dispatch import receiver
from django.db.models.signals import pre_save
from app_groups.models import Groups, Homeworks
from django.utils.text import slugify


@receiver(pre_save, sender=Groups)
def generate_slug_for_post(sender, instance, **kwargs):
    if not instance.slug:
        original_slug = slugify(instance.name)
        slug = original_slug
        count = 0
        while Groups.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{count}"
            count += 1

        instance.slug = slug

    
@receiver(pre_save, sender=Homeworks)
def generate_slug_for_post(sender, instance, **kwargs):
    if not instance.slug:
        original_slug = slugify(instance.title)
        slug = original_slug
        count = 0
        while Homeworks.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{count}"
            count += 1

        instance.slug = slug

        