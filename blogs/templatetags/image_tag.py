from django import template
from blogs.models import Image


register = template.Library()

@register.assignment_tag
def get_image(post,user):
	try:
		images = Image.objects.filter(blog__id=sales_id)[0]
		import pdb;pdb.set_trace()
		# image = images.image
		# return HttpResponse(image.read(),
  #                       mimetype="image/jpeg")
        return False
	except Exception, e:
		return True	

