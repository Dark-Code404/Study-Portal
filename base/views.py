from django.contrib import messages
 
 
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from base.forms import MessageForm, RoomForm
from base.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
	if request.GET.get('q') != None:
		q=request.GET.get('q') 
	else :
		q=''
	
	rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q( name__icontains=q) | 
		Q( host__first_name__icontains=q) | Q( host__last_name__icontains=q))
	topics=Topic.objects.all()
	count=rooms.count()
	recent_messages=Message.objects.filter(Q(room__topic__name__icontains=q))

	

	dict={'rooms':rooms ,'topics':topics,'count':count,'recent_messages':recent_messages}
	return render(request,"base/home.html",dict)

# @login_required
def room(request,pk):

	
	
	room=Room.objects.get(id=pk) 
	messagess=room.message_set.all().order_by('-created')
	participants=room.participants.all()
	
	form=MessageForm()
	if request.method=='POST':
		form=MessageForm(request.POST,request.FILES)
		if form.is_valid():
			messagess=form.save(commit=False)
			messagess.user=request.user
			messagess.room=room
			messagess.save()

			
		
		else:
			messages.error(request,"There was an error with your message. Please try again.")
			form=MessageForm()
		room.participants.add(request.user)
		return redirect('room',pk=room.id)
	context={'room':room,'messagess':messagess,'participants':participants,'form':form}
	return render(request,"base/room.html",context)

@login_required()

def create_rooms(request):

	form=RoomForm()

	if request.method=='POST':
		topic_name=request.POST.get('topic')
		form=RoomForm(request.POST)
		print("Topic name : ",topic_name)

		if form.is_valid():
			print("Form is valid.")
			room=form.save(commit=False)

			room.host=request.user
			topic, created = Topic.objects.get_or_create(name=topic_name)	
			if created:
				topic.creator = request.user
				topic.save()
			
			room.topic=topic
			room.save()
			print("Room created successfully:", room)
			return redirect('home')
		
		else:
			print("Forms errors : ",form.errors)
		

	topics=Topic.objects.all()
	
	context={'form':form,'topics':topics}
	return render(request,"base/create_rooms.html",context)

@login_required()
def update_rooms(request,pk):
	room=Room.objects.get(id=pk)
	form=RoomForm(instance=room)

	if request.user != room.host:
		return HttpResponse("You are not owner of this room so you are not allowed here..")
	
	if request.method=='POST':

		topic_name=request.POST.get('topic')
		form=RoomForm(request.POST,instance=room)
		if form.is_valid():
			room=form.save(commit=False)
			topic,created=Topic.objects.get_or_create(name=topic_name)
			room.topic=topic
			room.save()

			return redirect('home')

	context={'form':form,'room':room}
	return render(request,"base/update_rooms.html",context)


@login_required()
def delete_rooms(request,pk):
	room=Room.objects.get(id=pk)
	context={'room':room}
	if request.user != room.host:
		return HttpResponse("You are not owner of this room so you are not allowed here..")
	if request.method=='POST':

		room.delete()

		return redirect('home')
	return render(request,"base/delete_rooms.html",context)

@login_required()
def delete_message(request,pk):
	message=Message.objects.get(id=pk)
	if request.user != message.user:
		return HttpResponse("You are not owner of this message so you are not allowed here..")
	
	if request.method=='POST':

		message.delete()

		return redirect('home')
	
	context={'room':message}
	
	return render(request,"base/delete_rooms.html",context)
@login_required()
def delete_topic(request,pk):
	topic=Topic.objects.get(id=pk)
	if request.user != topic.creator:
		return HttpResponse("You are not owner of this message so you are not allowed here..")
	
	if request.method=='POST':
		if topic.room_set.count() == 0:

			topic.delete()

			return redirect('home')
		else:
			messages.error(request,"You can't delete this topic because it has rooms.")
	
	context={'room':topic}
	
	return render(request,"base/delete_rooms.html",context)






 
	

	


	
	