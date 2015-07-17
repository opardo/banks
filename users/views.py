from django.shortcuts import get_object_or_404, render

from users.models import Investor, Bank


def index(request):
    latest_users_list = Investor.objects.order_by('name')[:4]
    banks_list = Bank.objects.all()

    examples = []

    for user in latest_users_list:
        information = {}
        information['name'] = user.name
        information['banks'] = user.investment()
        examples.append(information)

    context = {'examples': examples, 'banks_list': banks_list}
    return render(request, 'users/index.html', context)


def detail(request, investor_id):
    try:
        user = get_object_or_404(Investor, pk=investor_id)
    except KeyError:
        return render(request, 'users/error.html', {
            'error_message': "El numero de usuario es incorrecto"
        })
    else:

        try:
                investment = user.investment()
        except AttributeError:
            return render(request, 'users/error.html', {
                'error_message': "El monto de dicho usuario no puede ser asignado a los bancos correspondientes. Intente con otro monto, o cambie la asignacion de bancos."
            })
        else:
            context = {'investment': investment, 'user': user}
            return render(request, 'users/detail.html', context)
