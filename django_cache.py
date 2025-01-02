from django.core.cache import cache


class Cache:
    """
    Oversimplified Redis cache, where you store model instances by their ID.
    Recommended to use uuid or custom unique id to use for the instance_id (if not using the model's primary key).
        Otherwise, using this cache may lead to bugs.

    Should be initialized in settings.py with the desired TTL (in seconds).
    The cache is not persistent.
    No separate bulk operations are provided, use add_instance and get_instance.

    """

    def __init__(self, ttl: str | int):
        self.ttl = ttl if isinstance(ttl, int) else int(ttl)

    def add_instance(self, instance_id, instance: list[object]) -> None:
        """
        Adds the model instance to the cache with a TTL.
        """
        cache.set(instance_id, instance, timeout=self.ttl)

    def get_instance(self, instance_id) -> list[object] | None:
        """
        Returns the model instance from the cache.
        """
        return cache.get(instance_id)
