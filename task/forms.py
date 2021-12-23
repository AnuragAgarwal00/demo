from django import forms
from .models import Task
from django.utils import timezone


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']

    def clean_deadline(self):
        current_date = timezone.now().date()
        print(current_date)
        deadline_line = self.cleaned_data['deadline'].date()
        print(deadline_line)
        if deadline_line <= current_date:
            raise forms.ValidationError('deadline date should be future date')
        return deadline_line