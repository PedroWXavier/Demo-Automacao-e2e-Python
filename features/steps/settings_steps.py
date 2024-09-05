from behave import given, when, then

from features.page_objects.settings_home import SettingsHome


@given(u'que clico no botao de pesquisa na pagina inicial de settings')
def step_impl(context):
    context.settings_home = SettingsHome()
    context.settings_home.clicar_no_botao_de_procurar()


@when(u'busco por "{texto}"')
def step_impl(context, texto):
    pass


@then(u'devo encontrar a opcao de wifi')
def step_impl(context):
    pass
