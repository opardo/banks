from django.shortcuts import render

from users.models import Investor, Bank


def index(request):
    latest_users_list = Investor.objects.order_by('-register_date')[:4]
    banks_list = Bank.objects.all()

    examples = []

    for user in latest_users_list:
        information = {}
        information['name'] = user.name
        try:
            information['banks'] = user.investment()
        except:
            information['banks'] = {'*Error': 'Leer nota en la parte inferior de la pagina.'}

        examples.append(information)

    context = {'examples': examples, 'banks_list': banks_list}

    return render(request, 'users/index.html', context)


