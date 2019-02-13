
import os

if __name__ == "__main__":
    # 设置django环境
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    import django

    django.setup()

    from blog import models

    # obj = models.Post.published.filter(title__startswith='独自')
