from django.http import HttpResponse


def required_groups(groups=[]):
    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = set([group.name for group in request.user.groups.all()])
            if user_groups.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized")

        return wrapper

    return decorator


def denied_groups(groups=[]):
    groups_set = set(groups)
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = set([group.name for group in request.user.groups.all()])
            if user_groups.intersection(groups_set):
                return HttpResponse("You are not authorized")
            else:
                return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
