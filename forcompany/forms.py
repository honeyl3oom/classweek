# -*- coding: utf-8 -*-

from django import forms
from forcompany.models import CompanyInfo

EMPTY_FORM_ERROR = 'have to fill this form'

class CompanyInfoForm(forms.models.ModelForm):

    class Meta:
        model = CompanyInfo
        fields = ('title', 'position', 'nearby_station', 'description', 'preparation_material', 'facility', 'class1_count', 'class1_price', 'class2_count', 'class2_price', 'class3_count', 'class3_price', 'class4_count', 'class4_price', 'class5_count', 'class5_price', 'class6_count', 'class6_price', 'teacher_image', 'teacher_name', 'teacher_career', 'refund_info', 'curriculum1_time', 'curriculum1_preparation_material', 'curriculum1_class_description', 'curriculum1_class_detail_description', 'curriculum2_time', 'curriculum2_preparation_material', 'curriculum2_class_description', 'curriculum2_class_detail_description', 'curriculum3_time', 'curriculum3_preparation_material', 'curriculum3_class_description', 'curriculum3_class_detail_description', 'curriculum4_time', 'curriculum4_preparation_material', 'curriculum4_class_description', 'curriculum4_class_detail_description', 'curriculum5_time', 'curriculum5_preparation_material', 'curriculum5_class_description', 'curriculum5_class_detail_description', 'curriculum6_time', 'curriculum6_preparation_material', 'curriculum6_class_description', 'curriculum6_class_detail_description', 'curriculum7_time', 'curriculum7_preparation_material', 'curriculum7_class_description', 'curriculum7_class_detail_description', 'curriculum8_time', 'curriculum8_preparation_material', 'curriculum8_class_description', 'curriculum8_class_detail_description',  )
        widgets = {
            'title': forms.fields.TextInput( attrs={
                'placeholder': '클래스 제목',
                'class': 'form-control',
            }),
            'position': forms.fields.TextInput( attrs={
                'placeholder': 'ex) 서울시 강남구 역삼동 아남타워 빌딩 7층',
                'class': 'form-control',
            }),
            'nearby_station': forms.fields.TextInput( attrs={
                'placeholder': 'ex) 선릉역, 역삼역',
                'class': 'form-control',
            }),
            'description': forms.fields.TextInput( attrs={
                'placeholder': '고객의 관심을 끌 수 있는 클래스에 대한 설명',
                'class': 'form-control',
            }),
            'preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '준비물, 없을경우 공란으로',
                'class': 'form-control',
            }),
            'facility': forms.fields.TextInput( attrs={
                'placeholder': 'ex) 개인락커, 화장실, 주차장',
                'class': 'form-control',
            }),

            'class1_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class1_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class2_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class2_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class3_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class3_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class4_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class4_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class5_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class5_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class6_count': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'class6_price': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum1_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum1_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum1_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum1_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum2_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum2_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum2_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum2_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum3_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum3_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum3_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum3_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum4_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum4_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum4_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum4_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum5_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum5_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum5_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum5_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum6_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum6_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum6_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum6_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum7_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum7_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum7_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum7_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum8_time': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum8_preparation_material': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum8_class_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'curriculum8_class_detail_description': forms.Textarea( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            # 'teacher_image': forms.fields.ClearableFileInput( attrs={
                # 'class': '',
            # }),
            'teacher_name': forms.fields.TextInput( attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'teacher_career': forms.Textarea(attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'refund_info': forms.Textarea(attrs={
                'placeholder': '환불 관련 정보를 입력해 주시면 됩니다.',
                'class': 'form-control',
                # 'width':'100%',
                # 'cols' : '80',
                # 'rows': '20',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CompanyInfoForm, self).__init__(*args, **kwargs)
        self.fields['title'].error_messages['required'] = EMPTY_FORM_ERROR