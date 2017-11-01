from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from .models import Question, Choice, Measurementunit, Threaddiameter, Partnumber, Threaddesignation


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('name')[:5]


class PartsView(generic.ListView):
    context_object_name = 'parts'
    template_name = 'polls/partsearch.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Partnumber.objects. \
                   exclude(threaddesignation__isnull=True). \
                   values('name',
                          'threaddesignation__pitch2threaddiameter__threaddiameter__measurementunit__name',
                          'threaddesignation__pitch2threaddiameter__threaddiameter__name',
                          'threaddesignation__pitch2threaddiameter__pitch__name')[:25]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
