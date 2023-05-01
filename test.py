def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World!"]

upstream django {
	server unix:///home/lava/Work/web_sql_django/web_sql_proj/web_sql_proj.sock;
}
server {
	listen 8888;
	server_name django django;
	charset utf-8;
	client_max_body_size 75M;

	location /media {
		alias /home/lava/Work/web_sql_django/media;
	}
	location /static {
		alias /home/lava/Work/web_sql_django/static;
	}

	location / {
		uwsgi_pass django;
		include /home/lava/Work/web_sql_django/web_sql_proj/uwsgi_params;
	}
}
