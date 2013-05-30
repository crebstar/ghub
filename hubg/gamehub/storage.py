from storages.backends.s3boto import S3BotoStorage
from django.utils.functional import SimpleLazyObject

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
# Paul :: Uncommented for now
#MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')