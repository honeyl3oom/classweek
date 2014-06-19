# -*- coding: utf-8 -*-
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse, reverse_lazy

from .models import CompanyMasterProfile, CompanyClasses

def index_view(request):
    return render( request, 'forcompany/index.html' )

class IndexView(TemplateView):

    template_name = 'forcompany/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # user_ = self.request.user.select_related('get_company_master_profile')
        user_ = User.objects.select_related('master_profile').get(id=self.request.user.id)
        context['user'] = user_
        context['company_classes'] = CompanyClasses.objects.all()
        return context

COMPANY_CLASSES_FIELD = ['title', 'sub_category', 'description', 'personal_or_group', 'price_of_month', 'preparation',
                         'curriculum_in_first_week', 'curriculum_in_second_week', 'curriculum_in_third_week',
                         'curriculum_in_fourth_week', 'curriculum_in_fifth_week']
COMPANY_CLASSES_FIELD_LABEL = {
    'title': '제목',
    'sub_category': '카테고리',
    'description': '상세설명',
    'personal_or_group': '레슨유형(개인 또는 그룹)',
    'price_of_month': '한달가격',
    'preparation': '준비물',
    'curriculum_in_first_week': '커리큘럼(1주차)',
    'curriculum_in_second_week': '커리큘럼(2주차)',
    'curriculum_in_third_week': '커리큘럼(3주차)',
    'curriculum_in_fourth_week': '커리큘럼(4주차)',
    'curriculum_in_fifth_week': '커리큘럼(5주차)',
}

class CompanyMasterProfileUpdateView(UpdateView):
    model = CompanyMasterProfile
    fields = ['company_name', 'local_number', 'phone_number', 'address', 'nearby_station', 'refund_information']
    template_name = 'forcompany/company_master_profile_update.html'

class CompanyClassesCreateView(CreateView):
    model = CompanyClasses
    fields = COMPANY_CLASSES_FIELD
    template_name = 'forcompany/company_classes_create.html'

    def dispatch(self, *args, **kwargs):
        return super(CompanyClassesCreateView, self).dispatch(*args, **kwargs)

    def get_form(self, form_class):
        form = super(CompanyClassesCreateView, self).get_form(form_class)
        form.fields['title'].label = 'test'
        for key in form.fields.keys():
            if COMPANY_CLASSES_FIELD_LABEL.has_key(key):
                form.fields[key].label = COMPANY_CLASSES_FIELD_LABEL[key]
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class CompanyClassesDeleteView(DeleteView):
    model = CompanyClasses
    success_url = reverse_lazy('forcompany:index', args=[])
    template_name = 'forcompany/company_classes_delete.html'

class CompanyClassesUpdateView(UpdateView):
    model = CompanyClasses
    fields = COMPANY_CLASSES_FIELD
    template_name = 'forcompany/company_classes_update.html'

    def get_form(self, form_class):
        form = super(CompanyClassesUpdateView, self).get_form(form_class)
        form.fields['title'].label = 'test'
        for key in form.fields.keys():
            if COMPANY_CLASSES_FIELD_LABEL.has_key(key):
                form.fields[key].label = COMPANY_CLASSES_FIELD_LABEL[key]
        return form

    def get_success_url(self):
        return reverse_lazy('forcompany:company_classes_detail', args=[self.object.pk])

class CompanyClassesDetailView(DetailView):
    model = CompanyClasses
    template_name = 'forcompany/company_classes_detail.html'

# from .forms import CompanyUserCreateForm

# class CompanyUserCreateView(View):
#
#     template_name = 'company_user_create.html'
#
#     # def post(self, request, *args, **kwargs):
#     #     user_form = CompanyUserCreateForm(request.POST)
#     #     if user_form.is_valid():
#     #         username = user_form.clean_username()
#     #         password = user_form.clean_password2()
#     #         user_form.save()
#     #         user = authenticate(username=username,
#     #                             password=password)
#     #         login(request, user)
#     #         return redirect("somewhere")
#     #
#     #     return render(request,
#     #                   self.template_name,
#     #                   { 'user_form' : user_form })
#
#     def get(self, request, *args, **kwargs):
#         user_form = CompanyUserCreateForm()
#
#         return render(request,
#                       self.template_name,
#                       { 'user_form' : user_form })
#
#

# from django.core.urlresolvers import reverse
#
# from django.views.generic import ListView, DetailView, UpdateView
#
# from .models import TCompany
#
# class TCompanyListView(ListView):
#     model = TCompany
#
# class TCompanyDetailView(DetailView):
#     model = TCompany
#
# class TCompanyResultsView(TCompanyDetailView):
#     template_name = "forcompany/results.html"
#
# class TCompanyUpdateView(UpdateView):
#     model = TCompany
#
#     def get_success_url(self):
#         return reverse("forcompany:detail",
#                        kwargs={"pk": self.object.pk})