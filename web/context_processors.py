
from .forms import EmailForm,FeedbackForm

def main_context(request):
    email_form = EmailForm()
    return {
        'email_form':email_form,
        'domain' : request.META['HTTP_HOST'],
    }

def main_contexttwo(request):
    feedback_form = FeedbackForm()
    return {
        'feedback_form':feedback_form,
        'domain' : request.META['HTTP_HOST'],
    }

