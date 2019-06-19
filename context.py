def global_constants(request):
    # NOTE(Dustin): request has request.user.is_authenticated()
    return {
        'APPNAME': "WorkingOn",
        'TEST': 123
    }
