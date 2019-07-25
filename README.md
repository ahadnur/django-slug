# Django Slug Project

***Things To Remember***
> - First you have to make utils.py file in you project root directory.
> - Second you have to add some functionalities to your database model.
> - The codes are given bellow.

> - utils.py

```python
import string, random

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
```
> - In models.py You have to import "from yourporject.utils import utils.py"
> - You also need to import pre_save from django.db.models.signals
> - Then you have to create your model.
> - After that you have to write your slug code.

> - models.py
```python
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
```