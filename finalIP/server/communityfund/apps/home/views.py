from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db.models import ForeignKey
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView
from django.views.generic import UpdateView
from django.views.generic.detail import SingleObjectMixin, DetailView
from communityfund.apps.home.models import Idea, Category
from communityfund.apps.inbox.views import get_msg
from communityfund.apps.home.forms import IdeaForm, IdeaUpdateForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt


class LoginRequiredMixin(object):
    """
    Class-based views can inherit from this to provide restricted access to the view unless the user is logged in
    """

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class ModelOwnershipMixin(SingleObjectMixin):
    """
    Class-based views can inherit from this to provide restricted access to the view unless the user accessing it
    owns the model in question.
    """
    model_owner_field = None

    def dispatch(self, request, *args, **kwargs):
        # Staff can access everything
        if not request.user.is_staff:
            # Determine the models owner field name by picking the first foreign key that references the User model
            if not self.model_owner_field:
                for f in self.model._meta.get_fields_with_model():
                    if isinstance(f[0], ForeignKey) and f[0].rel.to == User:
                        self.model_owner_field = f[0].name

            # Redirect if the user doesn't own this
            obj = self.get_object()
            if getattr(obj, self.model_owner_field) != request.user:
                return redirect(obj)
        return super(ModelOwnershipMixin, self).dispatch(request, *args, **kwargs)


class IdeaCreate(LoginRequiredMixin, CreateView):
    """
    Class-based view that allows a logged in user to create a idea.
    """
    model = Idea
    form_class = IdeaForm
    template_name = 'home/idea_create.html'

    def form_valid(self, form):
        # Set the initiator before the form is saved
        form.instance.initiator = self.request.user
        return super(IdeaCreate, self).form_valid(form)


class IdeaUpdate(LoginRequiredMixin, ModelOwnershipMixin, UpdateView):
    """
    Class-based view that allows a logged in idea owner to edit their idea.
    """
    model = Idea
    form_class = IdeaUpdateForm
    model_owner_field = 'initiator'
    template_name = 'home/idea_update.html'


class IdeaDelete(LoginRequiredMixin, ModelOwnershipMixin, DeleteView):
    """
    Class-based view that allows a logged in idea owner to delete their idea.
    """
    model = Idea
    success_url = reverse_lazy('profile')


def index(request):
    return render(request, 'home/index.html', {
        'ideas': Idea.objects.all(),
        'categories': Category.objects.all(),
    })


def ideas(request):
    all_ideas = Idea.objects.all()
    paginator = Paginator(all_ideas, 12)  # 12 ideas per page
    page = request.GET.get('page')
    try:
        ideas = paginator.page(page)
    except PageNotAnInteger:
        ideas = paginator.page(1)
    except EmptyPage:
        ideas = paginator.page(paginator.num_pages)
    return render(request, 'home/ideas.html', {
        'ideas': ideas
    })


def categories(request):
    all_communities = Category.objects.all()
    paginator = Paginator(all_communities, 12)  # 12 categories per page
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, 'home/categories.html', {
        'categories': categories
    })


@login_required
def create_category(request):
    # TODO
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        return render(request, 'home/create_category.html', {
            'category_form': {},
        })


@csrf_exempt
def user(request, user_id):
    return render(request, 'home/user.html', {
        'user_profile': get_object_or_404(User, pk=user_id),
        'user_message': get_msg(user_id),
    })

def user_details(request, pk):
    return render(request, 'home/user.html', {
        'user_profile': get_object_or_404(User, pk=pk),
    })


def idea_details(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'home/idea.html', {
        'idea': idea,
    })


def category_details(request, pk):
    category = get_object_or_404(Category, pk=pk)
    ideas = category.ideas.all()
    paginator = Paginator(ideas, 3)  # 3 ideas per page
    page = request.GET.get('page')
    try:
        ideas = paginator.page(page)
    except PageNotAnInteger:
        ideas = paginator.page(1)
    except EmptyPage:
        ideas = paginator.page(paginator.num_pages)
    return render(request, 'home/category.html', {
        'category': get_object_or_404(Category, pk=pk),
        'ideas': ideas,
        'paginator': paginator
    })

@login_required
@require_POST
def category_subscribe(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.subscribers.add(request.user)
    return redirect(category)


@login_required
@require_POST
def category_unsubscribe(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.subscribers.remove(request.user)
    return redirect(category)
