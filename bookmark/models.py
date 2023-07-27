from django.db import models

from django.db import models

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)  # 컬럼의 별칭, 제약조건 설정
    url = models.URLField('URL', unique=True)

    def __str__(self) -> str:  # 객체를 문자열로 표현할 때 사용하는 함수
        return self.title
# Create your models here.
