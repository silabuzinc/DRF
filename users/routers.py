from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'get'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}$',
            mapping={'post': 'post'},
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'put': 'put'},
            name='{basename}-update',
            detail=True,
            initkwargs={'suffix': 'Update'}
        ),
    ]