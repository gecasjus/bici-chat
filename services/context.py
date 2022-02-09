from starlette.middleware import Middleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware

RequestContext = [
    Middleware(
        ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]
