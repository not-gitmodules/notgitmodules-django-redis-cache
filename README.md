# Simple Redis-based cache for Django

## Usage

1. Install this `not_gitmodule` using our brand tool, or gitmodules. 
2. Add the containing of `requirements.txt` to your `requirements.txt` file, and rerun `pip install -r requirements.txt`. (if not yet done)
3. Add `redis_cache` to your `INSTALLED_APPS` in your Django settings file.

---
Example `settings.py`:
1. Add the following to your `settings.py` file's imports:

```python
from django.core.cache import cache # this is the default cache designed for Django
from cache.cache import Cache # this is this module with cache interface
```

2. Add caching to your project

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 100,
                'retry_on_timeout': True,
            }
        }
    }
}
```

3. Use the cache in your project

```python
from django.conf import settings

REDIS_CACHE = settings.CACHE
```

4. Example usage:

```python
def find_entry(some_id):
    if not (entry := REDIS_CACHE.get_instance(some_id)):
        try:
            entry: list = SomeModel.objects.get(id=some_id)
        except SomeModel.DoesNotExist:
            return {"status": False, "message": "Entry not found"}
    return {"status": True, "data": entry}
```

---

## Installation with `not_gitmodules`

- Example of `notgitmodules.yaml`:

```yaml
utils:
  django_redis_cache: https://github.com/not-gitmodules/notgitmodules-django-redis-cache
```

- Run the following command:

```bash
not_gitmodules -y path/to/notgitmodules.yaml
```

