## Django Jet sidebar (rebuild)

### SOBRE
```
Este projeto substitui a antiga barra lateral do django jet e instala a nova barra lateral,
conta com ajustes no CSS e JS para o django jet.
```

### IMPLEMENTAÇÕES
```
- Sidebar
- Logo e icones na sidebar
- Contador de caracteres*
- JS Mascara em Campos*
- Melhorias de CSS 

* Irá ser lançado
```

### INSTALAÇÃO 
* **Baixe e instale a versão mais recente do SideBar para Django JET:**

```
Instale o django-jet mais recente para sua versão do Django no projeto, e configure 
o django jet antes de prosseguir
```

***

* **Instale a ultima versão do jet-sidebar**

```
pip install jet-sidebar
```

***

* **Adicione 'jet_sidebar' nas configurações antes de importar 'jet'**

[comment]: <> (.. code:: python)

    INSTALLED_APPS = (
        ...
        'jet_sidebar',
        'jet',
        'django.contrib.admin',
    )

***

* **Faça o collectstatic para pegar as dependências do css e js do projeto:**

[comment]: <> (.. code:: python)

    python manage.py collectstatic

***

### Adicione as suas opções a personalização de sua barra lateral, abra o settings.py e adicione suas opções


* **Titulo no topo do menu**

* ###### Sobre
  
```
- Para usar algum texto customizado configure o admin.site.site_header em urls.py, deve parecer 
com o modelo abaixo.

OBS: Coloque após urlpatterns.
```

* ###### Código

[comment]: <> (.. code:: python)

    admin.site.site_header = 'Your-Name'

***

* **Icone no topo do menu**

* ###### Sobre

```
Para configurar um icone de menu tem-se duas configurações: {
    'icon': 'Colocar o caminho da sua imagem depois da sua pasta static, como no exemplo. (obrigatório)'
    'width': 'Colocar a largura de ajuste do seu icone, como no exemplo. (não obrigatório)'
    'style': 'Colocar os estilos de ajustes de estilos, como no exemplo.(não obrigatório)'
}

- SID_ICON_SMALL -> Icone pequeno (menu reduzido);
- SID_ICON_LARGE -> # Icone grande (menu aberto);

OBS: Caso só configure apenas um tamanho de icone o menu reduzido/aberto poderá ficar desconfigurado
```

* ###### Código

[comment]: <> (.. code:: python)

    SID_ICON_SMALL = {
        'icon': '/img/example.png',
        'width': '70px',
        'style': 'padding: 1px; ...',
    }
    
    SID_ICON_LARGE = {
        'icon': '/img/example.png',
        'width': '150px',
        'style': 'padding: 1px; ...',
    }


***

* **Título das aplicações**
  
* ###### Sobre

``` 
- SID_TITLE_MENU -> Define se o menu vai ter o titulo na listagem das aplicações. Por padrão vem "Aplicações".
- SID_TEXT_MENU -> Define seu titulo no menu de aplicações.
```

* ###### Código

[comment]: <> (.. code:: python)

    SID_TITLE_MENU = True
    SID_TEXT_MENU = 'Your-Name'
    
***

* **Configuração dos icones de aplicações (settings.py)**

* ###### Sobre

``` 
- Por padrão poderá fazer isso no settings.py caso seja alguma biblioteca que vai ser usado no admin.
- Como exemplo tem a aplicação 'auth' e 'sites' apps do proprio django.

Irá receber um dict, retornando um dict para cada aplicação sendo sua 'key' o app_label da aplicação:
{
    'app_label':{
        'class_icon': 'Usamos os icones FREE do font awesome, basta colocar a classe neste atributo. (obrigatório)'
    },
    ...
}

- Caso você não saiba o nome da sua app_label olhe nos logs enquanto estiver com o runserver 
- ativo e dentro do site de admin
```

* ###### Código

[comment]: <> (.. code:: python)

    SID_APP_ICONS = {
        'auth': {
            'class_icon': 'fas fa-shield-alt',
        },
        'sites': {
            'class_icon': 'fas fa-link',
        }
    }

***

* **Configuração dos icones de aplicações (apps.py)**

* ###### Sobre
```
- Poderá configurar de forma descentralizada os icones de suas aplicações que você consegue acessar. 
- Para isso basta acessar o apps.py da aplicação de dentro da classe de configuração colocar o atributo class_icon
- Caso você não saiba o nome da sua app_label olhe nos logs enquanto estiver com o runserver ativo e dentro do site de admin
- Se quiser criar no settings, adicione a dict da sua aplicação como no exemplo acima, sua app_label deve ser 
igual o atributo 'name', que está em apps.py.
```

* ###### Código

[comment]: <> (.. code:: python)

    class ClientConfig(AppConfig):
        ...
        class_icon = 'fas fa-users'

***

* **Configuração dos links em destaque**

* ###### Sobre
```
- Agora você tem como adicionar links em destaque, basta setar os links no settings no formato abaixo.
O formato será uma lista de dicts nomeados com cada parâmetro para o link.
- name (obrigatório): recebe uma string, nome do link
- url (obrigatório): recebe uma string, endereço do link
- class_icon (opcional): recebe uma string, classe do awesome icon
- style (opcional): recebe uma string, custom style for icon
- perms (opcional): recebe uma lista, lista de permissões atribuidos a visualização do link,
caso não queira atribuir permissões ocultar este parâmetro

```

* ###### Código

[comment]: <> (.. code:: python)

    HIGHLIGHT_LINKS = [
        {'name': '', 'url': '', 'class_icon': '', 'style': '', 'perms': []},
    ]

***

