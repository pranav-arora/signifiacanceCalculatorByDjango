from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomeForm
# Create your views here.
class significance_view(TemplateView):
    template_name = 'sign/calculator.html'

    def get(self,request):
        form=HomeForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=HomeForm(request.POST)

        if form.is_valid():

            visitControl = form.cleaned_data['visitorControl']
            visitorVariation = form.cleaned_data['visitorVariation']
            conversionControl = form.cleaned_data['conversionControl']
            conversionVariation = form.cleaned_data['conversionVariation']
            if visitControl<15:
                error='Control value less than 15'
                PValue=0
                significance=''
            elif conversionControl<15:
                PValue = 0
                significance = ''
                error='Control value less than 15'
            else:
                error=''
                PValue=((visitorVariation+conversionVariation)/2)

                if (visitControl > conversionControl):
                    significance= "yes"
                else:
                    significance= "no"


        args = {'form': form, 'significance': significance,'pvalue':PValue,'error': error}

        return render(request,self.template_name,{'args':args})
