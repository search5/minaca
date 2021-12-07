def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('api_test', '/api/gyeongsil')
    config.add_route('catchall_static', '/*subpath')
    config.add_view('minaca.static.static_view', route_name='catchall_static')
