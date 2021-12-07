from pyramid.static import static_view

static_view = static_view('minaca:static', use_subpath=True)
