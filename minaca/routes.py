def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('api_test', '/api/gyeongsil')

    config.add_view('minaca.static.static_view', route_name='catchall_static')
    # config.add_view('minaca.static.static_view', route_name='catchall_static_css')
    config.add_route('catchall_static_js', '/js/{subpath:.+}')
    # config.add_route('catchall_static_css', '/css/*subpath')

    config.add_route('home', '/{route_path:.*}')



