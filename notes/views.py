from django.http import  HttpResponseRedirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Notes
from .forms import NoteForm
from django.views.generic.edit import DeleteView

# Create your views here.
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name='notes/notes_delete.html'
    

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=Notes
    success_url = '/smart/notes'
    form_class = NoteForm



class NotesCreateView(LoginRequiredMixin,CreateView):
    model=Notes
    success_url = '/smart/notes'
    form_class = NoteForm


    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin,ListView):
    model= Notes
    context_object_name = 'notes'
    template_name= 'notes/notes_list.html'


    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    login_url='/login'