import sqlalchemy.exc


class AlreadyExistsError(RuntimeError):
    def __init__(
        self, instance
    ):
        super().__init__(
            f"Object [{instance.__class__.__name__}] pk={instance.get_primary_key()} already exists."
        )


def handle_db_errors(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except sqlalchemy.exc.IntegrityError as e:
            if "already exists" in str(e):
                instance = kwargs.get("instance") or args[0]
                raise AlreadyExistsError(instance)

            raise

    return wrapper
