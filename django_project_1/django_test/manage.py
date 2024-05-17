#!/usr/bin/env python
# manage.py파일은 django 프로젝트를 관리하는데 사용되며, 프로젝트 설정, 앱 관리, 데이터베이스 마이그레이션
# 등의 명령을 실행하는 데 필요한 기본 설정을 포함하고 있다. 프로젝트의 구조와 명령 실행에 중요한 역할을 하지만
# 파일 수정은 불필요하다.
# 
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
