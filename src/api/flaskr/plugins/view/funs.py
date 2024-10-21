from flask import Flask
from .models import views
from flaskr.service.common.models import raise_error


def get_view(app: Flask, user_id: str, view_name: str):
    view = views.get(view_name, None)
    if view is None:
        raise_error("ADMIN.VIEW_NOT_FOUND")
    else:
        app.logger.info("get view:" + view_name)
        return view.get_view_def()


def query_view(
    app: Flask,
    user_id: str,
    view_name: str,
    page: int = 1,
    page_size: int = 20,
    query=None,
    sort=[],
):
    view = views.get(view_name, None)
    if view is None:
        raise_error("ADMIN.VIEW_NOT_FOUND")
    else:
        return view.query(app, page, page_size, query, sort)


def export_query(app: Flask, user_id: str, view_name: str, query=None):
    view = views.get(view_name, None)
    if view is None:
        raise_error("ADMIN.VIEW_NOT_FOUND")
    else:
        return view.export_query_to_excel(app, query)
