from paradoxdjango.apps import apps
from paradoxdjango.conf import settings
from paradoxdjango.contrib.redirects.models import Redirect
from paradoxdjango.contrib.sites.shortcuts import get_current_site
from paradoxdjango.core.exceptions import ImproperlyConfigured
from paradoxdjango.http import HttpResponseGone, HttpResponsePermanentRedirect
from paradoxdjango.utils.deprecation import MiddlewareMixin


class RedirectFallbackMiddleware(MiddlewareMixin):
    # Defined as class-level attributes to be subclassing-friendly.
    response_gone_class = HttpResponseGone
    response_redirect_class = HttpResponsePermanentRedirect

    def __init__(self, get_response):
        if not apps.is_installed("paradoxdjango.contrib.sites"):
            raise ImproperlyConfigured(
                "You cannot use RedirectFallbackMiddleware when "
                "paradoxdjango.contrib.sites is not installed."
            )
        super().__init__(get_response)

    def process_response(self, request, response):
        # No need to check for a redirect for non-404 responses.
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        current_site = get_current_site(request)

        r = None
        try:
            r = Redirect.objects.get(site=current_site, old_path=full_path)
        except Redirect.DoesNotExist:
            pass
        if r is None and settings.APPEND_SLASH and not request.path.endswith("/"):
            try:
                r = Redirect.objects.get(
                    site=current_site,
                    old_path=request.get_full_path(force_append_slash=True),
                )
            except Redirect.DoesNotExist:
                pass
        if r is not None:
            if r.new_path == "":
                return self.response_gone_class()
            return self.response_redirect_class(r.new_path)

        # No redirect was found. Return the response.
        return response
