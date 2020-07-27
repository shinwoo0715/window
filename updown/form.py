from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo

        # 태그를 안치고 form자체를 클래쓰로 이동시키는것
        # 2020 06 22 내가 봤을때 우리가 views 에서 db 안에 일일히 하나하나 쳐서 넣는 게
            # 귀찮아서 그냥 form을 하나 만들어서 form이랑 model이랑 연동해서 form에 넣으면
            # model로 가는 그런거 같다.
        # fields = ("사용자" , "사진" , 'content')
        fields = ('사진' , 'content') #  이거는 절대 admin에 display가 아니다.

        # fileds는
