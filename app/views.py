from uuid import uuid4

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView

from . import forms

# Create your views here.

# 関数ビューによるAjax
def index(request):
    template = 'index.html'
    if request.method == 'GET':
        return render(request, template)
    elif request.method == 'POST':
        name = request.POST.get('name-of-form')
        return render(request, template, context={'name': name})


def ajax(request):
    import time
    time.sleep(3)
    name = request.GET.get('name')
    return HttpResponse(f'こんにちは、{name}さん！')


# クラスベースによるAjaxサンプル
class GreetView(FormView):
    template_name = 'greet.html'  # テンプレート名(htmlファイル名)
    form_class = forms.GreetForm
    success_url = '/greet'

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if request.is_ajax():
                """Ajax 処理を別メソッドに切り離す"""
                print('### Ajax request')
                return self.ajax_response(form)
            # Ajax 以外のPOSTメソッドの処理
            return super().form_valid(form)
        # フォームデータが正しくない場合の処理
        return super().form_invalid(form)

    def ajax_response(self, form):
        """jQuery に対してレスポンスを返すメソッド"""
        name = form.cleaned_data.get('name')
        return HttpResponse(f'こんにちは、{name}さん！')
