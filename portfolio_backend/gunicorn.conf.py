import multiprocessing

# Server socket
bind = "0.0.0.0:8080"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 2

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process naming
proc_name = 'portfolio_backend'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL
keyfile = None
certfile = None

# Django WSGI application path
wsgi_app = 'portfolio_backend.wsgi:application'

# Debugging
reload = True
reload_engine = 'auto'

# Timeouts
graceful_timeout = 120
timeout = 120

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190 