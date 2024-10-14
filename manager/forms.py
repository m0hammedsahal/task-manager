
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'staff', 'is_complete', 'is_verified']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2'}),
            'description': forms.Textarea(attrs={
                'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4, 
                'cols': 50  
            }),
            'staff': forms.Select(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2'}),
        }
