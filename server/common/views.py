from rest_framework import authentication


class SessionCsrfExemptAuthentication(authentication.SessionAuthentication):
    """
    Class to use django authentication in django-rest-framework.
    Disables CSRF.
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening