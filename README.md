<h1 style="text-align: center;">app-entregas-v1</h1>

<br/>

## Deploy para visualização: 
<a href="https://app-entregas-v1.onrender.com" target="_blank">App Entregas Web Site</a>
>**NOTA:** O sistema é apenas um protótipo para prova de conceito e não deve ser usado como produto final. Os dados registrados desaparecerão em algumas horas

<br/>

## Instalação:

Depende:

- python3
- pip

### Para instalar esse projeto, execute:

  ```sh
  python -m pip install -r ./requirements.txt --break-system-packages
  ```
  >**NOTA:** A tag `--break-system-packages` serve para forçar a intalação das bibliotecas sem um ambiente virtual VENV. Você pode remover se já tiver configurado

### Para executar:

  ```sh
  python main.py
  ```

### Utilizando o docker:
  ```sh
  docker compose up -d
  ```
  >**NOTA:** Após executar o comando o container está rodando e você pode acessar o sistema em seu <a href="http://127.0.0.1/5050">localhost</a> na porta `5050`



<h2>Funcionamento Geral</h2>
  Este sistema foi feito para agilizar o atendimento ao cliente. Sendo possível registrar seus pedidos de entrega e coleta
  de equipamentos e materiais. Nele foi adicionado a aba de ferramentas, onde de inicio foi implementado o <b>"Zap sem Contato"</b>,
  que perimite informar um número de telefone para ser aberto uma nova conversa direto no WhatsApp. Além de uma ferramenta para
  calcular Banner, adesivo, etc, que ainda não foi desenvolvido. Ainda seriam adicionadas mais ferramentas nessa aba
  A <b>aba consulta</b>, permite editar ou remover pedidos de coleta cadastrados que foram criados na <b>aba Nova Ordem.</b>

  <br>Quando cursor do mouse sair da janela ou estiver parado, a aba entregas será atualizada automaticamente para retornar novas
  ordens criadas.
  
<h2>Gerenciador de Links</h2>
  Além disso, foi incluído em ferramentas, com o propósito de ajudar a empresa, a <b>aba Gerenciador de Links</b> que armazena links
  para o sites mais utilizados no setor de atendimento de LanHouse com seus respectivos nomes de identificação, onde lá mesmo,
  é possivel editar, modificar os já existentes, remover ou adicionar novos.

<h2>Criar Nova Ordem</h2>
  Nesta aba é onde você criar novas ordens de coleta ou entrega, onde na parte superior do formulário é mostrada o ID da ordem 
  atualmente sendo criada.
  Na forma de pagamento você pode selecionar "Sem Custo" e o valor será zerado
  
<h2>Aba Entregas</h2>
  Aqui é onde mostra as ordens criadas e você pode interagir. Onde, para fechar uma ordem tem que ser marcada como 
  "Pago", "Coletado" e "Entregue" para não apareça mais nessa aba. Retornando para o usuário "Sem Ordens Criadas".
  Em "Ações" no card da ordem, tem tembém o botão "Imprimir" caso necessário colocar junto ao material antes de seguir para o cliente
  
<h2>Aba DashBoard</h2>
  A ideia seria mostrar um relatório com os valores das entregas e do serviço feito em formato de gráfico e outros. Além de mostrar
  as ultimas ordens abertas, quantidades, ultimos clientes, clientes com mais pedidos, entre outros

<br><br><br>
<span><b><i>Não há mais suporte ou atualizações para essa aplicação.<br> Será desenvolvido outra plataforma com tecnologias
mais recentes em javascript com TypeScript</i></b></span>
