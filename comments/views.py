from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserComment
from .forms import UserCommentForm

from checkout.models import Order


@login_required
def comment(request):
    """ Display the user's comment. """
    comment = get_object_or_404(UserComment, user=request.user)

    if request.method == 'POST':
        form = UserCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commment updated successfully')
        else:
            messages.error
            (request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserCommentForm(instance=comment)
    orders = comment.orders.all()

    template = 'comments/comment.html'
    context = {
        'form': form,
        'orders': orders,
        'on_comment_page': True
    }

    return render(request, template, context)
