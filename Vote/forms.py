from django .forms import ModelForm
from .models import Votes,Member

class createvoteform(ModelForm):
    class Meta:
        model= Votes
        fields =['creator_name','quetion','option_one','option_two','option_three','option_four','date','img']


