from django.db import models

from django.db import models

class Bookmark(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)  # 컬럼의 별칭, 제약조건 설정, 얘는 blank가 True로 되어있어서 어드민에서 굵은 글씨로 나오지 않는다.
    url = models.URLField('Url', unique=True)  # null=False, blank=false

    def __str__(self) -> str:  # 객체를 문자열로 표현할 때 사용하는 함수
        return self.title
# Create your models here.
