from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse

from models import Notes

def notes_list(request):
    """Menampilkan semua notes yang ada"""
    
    return object_list(request, 
        queryset=Notes.objects.all(),
        template_name='notes/list.html',
        template_object_name='note'
    )
    
def notes_detail(request, id):
    """Melihat rincian dari salah satu note"""
    
    return object_detail(request,
        queryset=Notes.objects.all(),
        object_id=id,
        template_name='notes/detail.html',
        template_object_name='note'
    )
    
def notes_create(request):
    """Membuat sebuah note baru"""
    
    return create_object(request,
        model=Notes,
        template_name='notes/create.html',
        post_save_redirect=reverse("notes_list")
    )            
    
def notes_update(request, id):
    """Update sebuah note"""
    
    return update_object(request,
        model=Notes,
        object_id=id,
        template_name='notes/update.html',
        post_save_redirect=reverse("notes_list")
    )            
    
def notes_delete(request, id):
    """Hapus sebuah note"""
    
    return delete_object(request,
        model=Notes,
        object_id=id,
        template_name='notes/delete.html',
        template_object_name='note',
        post_delete_redirect=reverse("notes_list")
    )                
