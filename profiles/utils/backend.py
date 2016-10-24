from enum import IntEnum, unique


@unique
class BackendType(IntEnum):
    AUTH = 1
    FACEBOOK = 2
    GOOGLE = 3


class AuthBackend(object):
    @staticmethod
    def get_backend_text(backend):
        return {
            BackendType.AUTH: "auth",
            BackendType.FACEBOOK: "facebook",
            BackendType.GOOGLE: "google-oauth2",
        }[int(backend)]
