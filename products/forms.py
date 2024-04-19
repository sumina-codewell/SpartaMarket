from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        error_messages = {
            'price': {'max_digits': '스파르타마켓은 안전한 거래를 위해 백만 단위 가격의 물건만 이용 가능합니다.',}
        }