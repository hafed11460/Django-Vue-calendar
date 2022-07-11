from rest_framework.permissions import BasePermission



class IsSourceOwner(BasePermission):
    def has_object_permission(self, request, view, source):
        if source.user == request.user:
            return True
        return False


class IsEventOwner(BasePermission):
    def has_object_permission(self, request, view, event):
        if event.source.user == request.user:
            return True
        return False
