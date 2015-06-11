from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from jobs.models import Job

class JobResource(ModelResource):
	"""
	API Facet
	"""
	class Meta:
		queryset = Job.objects.all()
		resouce_name = 'job'
		allowed_method = ['post','get','patch','delete']
		authentication = Authentication()
		authorization = Authorization()
		always_return_data = True
