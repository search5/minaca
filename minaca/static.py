from pyramid.static import static_view
from pathlib import Path

static_dir = Path(__file__).parent / 'static'
static_view = static_view(static_dir, use_subpath=True)
