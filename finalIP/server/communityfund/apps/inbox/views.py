from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from communityfund.apps.inbox.models import Message

@login_required
def msg_send(request):
	sender = request.user
	receiver = request.POST.get('messages_recieved', '')
	receiver = User.objects.filter(username=receiver)
	title = request.POST.get('title', '')
	content = request.POST.get('content', '')
	msg = Message.objects.create(sender=sender, receiver=receiver, title=title, content=content)
	msg.save()

def get_msg(username):
	return Message.objects.filter(receiver=username)
