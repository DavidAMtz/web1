from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def PaginaMuebleria(request):

    doc_externo=open("C:/Users/usuar/projects/web1/web1/site/index.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)
      

    return HttpResponse(documento)

