from uuid import uuid4
import os
def path_and_rename(instance, filename):
    upload_to = f'{instance.__class__.__name__}'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}_{}.{}'.format(instance.name,uuid4().hex, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
# Create your models here.