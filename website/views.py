from django.views.generic.edit import UpdateView
from helloworld.models import Funcionario
class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = [
    'nome',
    'sobrenome',
    'cpf',
    'tempo_de_servico',
    'remuneracao'
]
context_object_name = 'funcionario'
def get_object(self, queryset=None):
funcionario = None
# Os campos {pk} e {slug} estão presentes em self.kwargs
id = self.kwargs.get(self.pk_url_kwarg)
slug = self.kwargs.get(self.slug_url_kwarg)
if id is not None:
# Busca o funcionario apartir do id
funcionario = Funcionario.objects.filter(id=id).first()
class FuncionarioDeleteView(DeleteView):
template_name = "website/exclui.html"
model = Funcionario
context_object_name = 'funcionario'
success_url = reverse_lazy(
"website:lista_funcionarios"
)
from django.views.generic import CreateView
class FuncionarioCreateView(CreateView):
template_name = "website/cria.html"
model = Funcionario
form_class = InsereFuncionarioForm
success_url = reverse_lazy("website:lista_funcionarios")


