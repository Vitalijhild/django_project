from django.http.response import HttpResponseForbidden
class UserIsOwnerMixin(object):

    def  dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creator != request.user:
            return  HttpResponseForbidden("You do not have permission to view this page.")