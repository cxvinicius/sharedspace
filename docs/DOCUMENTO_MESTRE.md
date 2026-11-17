# SharedSpace --- Checkpoint 00

**Visão Geral\
**SharedSpace é um Web App para monitorar a ocupação de espaços
compartilhados em ambientes corporativos. A ideia nasceu de um problema
real observado no ambiente de trabalho: colaboradores se deslocam até a
copa sem saber se há vagas, perdendo tempo e interrompendo suas
atividades.

## Propósito

Construir uma solução simples, visual e útil que permita consultar a
ocupação de um espaço em tempo real, registrar entradas e saídas,
organizar filas quando necessário e gerar informações para apoiar
decisões da empresa.

## Problema

• Deslocamentos desnecessários.\
• Perda de tempo.\
• Frustração ao encontrar espaços lotados.\
• Falta de dados sobre utilização dos ambientes.

## Quem usa?

Colaboradores que utilizam espaços compartilhados com capacidade
limitada.

## Quem é o cliente?

A empresa, que deseja melhorar a experiência dos colaboradores e
compreender como seus espaços são utilizados.

## Primeiro cenário

O MVP será focado na copa da empresa, mas a arquitetura será genérica
para suportar salas de descanso, academias, laboratórios, salas de
reunião e outros espaços.

## Valor para o colaborador

• Saber se há vagas antes de sair da mesa.\
• Registrar entrada e saída rapidamente.\
• Entrar em fila quando o espaço estiver cheio.\
• Evitar deslocamentos desnecessários.

## Valor para a empresa

• Dados de ocupação.\
• Horários de pico.\
• Tempo médio de permanência.\
• Tempo médio de espera.\
• Apoio à tomada de decisões.

## Ideias aprovadas

• Interface visual.\
• Representação do espaço com mesa, cadeiras e avatares.\
• Exibição opcional dos nomes dos ocupantes.\
• Sistema de fila.\
• Histórico e dashboard com gráficos.\
• Web App responsivo (sem instalação).

## Fora do escopo inicial

• Login complexo.\
• Integrações externas.\
• IoT e sensores.\
• QR Code.\
• Notificações avançadas.\
Esses recursos poderão ser avaliados após o MVP.

## Objetivos de aprendizado

• Descoberta do problema.\
• Levantamento de requisitos.\
• Prototipação.\
• Arquitetura.\
• Backend.\
• Frontend.\
• Banco de dados.\
• APIs.\
• Deploy.\
• Trabalho orientado por produto.

## Estratégia

Desenvolver por versões (v0.1, v0.2, \... v1.0), entregando uma versão
utilizável rapidamente para coleta de feedback de usuários reais.

## Prazo

Objetivo de concluir uma primeira versão utilizável em aproximadamente
35 dias, aproveitando a possibilidade de validação com colaboradores da
empresa.

## Visão do Produto

\"Transformar um problema cotidiano de ocupação de espaços em uma
solução simples, intuitiva e baseada em dados, proporcionando melhor
experiência aos colaboradores e informações úteis para a gestão.\"

# SharedSpace --- Checkpoint 01

**Fase 1 --- Discovery**

**Objetivo deste checkpoint.** Consolidar as decisões, hipóteses, riscos
e aprendizados obtidos durante a Fase 1, antes do levantamento formal de
requisitos e de qualquer implementação.

## 1. Problem Statement

Em ambientes corporativos com espaços compartilhados e capacidade
limitada, colaboradores nem sempre conseguem saber antecipadamente se há
disponibilidade. Isso pode gerar deslocamentos desnecessários,
aglomerações, espera e interrupções na rotina de trabalho. No cenário
inicialmente observado, esse problema acontece principalmente nos
horários de pico da copa, quando colaboradores precisam se deslocar até
o local apenas para descobrir se há uma vaga disponível.

## 2. Hipótese de Produto

Se colaboradores puderem conhecer a disponibilidade de espaços
compartilhados antes de se deslocarem até eles, podemos reduzir
deslocamentos desnecessários, espera e aglomerações, tornando o uso
desses ambientes mais previsível e eficiente.

Esta é uma hipótese a ser validada com usuários reais durante o piloto;
não é tratada como resultado garantido.

## 3. Escopo conceitual

O problema inicial nasceu da copa, mas o SharedSpace não será
conceitualmente limitado a esse ambiente. O produto é pensado para
espaços corporativos compartilhados com capacidade limitada, como salas
de descanso, academias, laboratórios, salas de reunião e outros
ambientes semelhantes.

O piloto, entretanto, começará com uma única organização e um primeiro
espaço: a copa. A generalização será validada posteriormente, sem
implementar complexidade futura antes de existir necessidade real.

## 4. Atores do produto

  -----------------------------------------------------------------------
  Ator                    Papel                   Necessidades principais
  ----------------------- ----------------------- -----------------------
  Colaborador             Usuário do espaço       Consultar
                          compartilhado           disponibilidade;
                                                  registrar entrada e
                                                  saída; utilizar fila
                                                  quando aplicável.

  Organização             Cliente do SharedSpace  Melhorar a experiência
                                                  de uso dos espaços e
                                                  obter informações
                                                  agregadas sobre
                                                  utilização.

  Administrador da        Responsável pela gestão Gerir espaços e
  organização             do produto na empresa   capacidades, acompanhar
                                                  adoção e consultar
                                                  analytics. No piloto, o
                                                  RH é o departamento de
                                                  referência.
  -----------------------------------------------------------------------

## 5. Jornada principal identificada

-   Antes de se deslocar, o colaborador consulta a disponibilidade do
    espaço.

-   Ao chegar, registra manualmente sua entrada por meio de uma
    interação extremamente rápida.

-   A ocupação é atualizada, por exemplo, de 0/5 para 1/5.

-   Ao terminar de utilizar o espaço, o colaborador registra manualmente
    sua saída.

-   A ocupação é novamente atualizada e uma vaga volta a ficar
    disponível.

## 6. Modelo inicial de ocupação

A ocupação será registrada manualmente. Sensores, IoT e automações
físicas não fazem parte do MVP. Entrada e saída serão ações manuais e
devem exigir pouquíssima interação, idealmente um ou poucos cliques.

A saída automática por timeout não foi adotada como comportamento
inicial. Uma futura confirmação ou expiração de sessões abandonadas
poderá ser avaliada após observarmos se o esquecimento de check-out é
realmente um problema frequente.

## 7. Risco central identificado

A confiabilidade da ocupação depende da colaboração dos usuários. Se uma
pessoa não registrar a entrada ou esquecer de registrar a saída, o
estado apresentado pelo sistema poderá divergir da ocupação real.

Hipótese a validar: se o processo for muito rápido e o próprio
colaborador perceber valor na consulta de disponibilidade e na fila,
haverá incentivo suficiente para manter os registros atualizados.

## 8. Privacidade por padrão

O SharedSpace monitora espaços, não pessoas. A visualização pública da
ocupação será anônima. Avatares, pratos ou assentos poderão representar
vagas ocupadas sem identificar nominalmente os colaboradores.

Os analytics corporativos deverão priorizar informações agregadas sobre
o espaço, como ocupação, horários de pico, permanência e demanda. Dados
pessoais só deverão ser considerados futuramente quando existir uma
necessidade funcional concreta e justificável.

## 9. Sessão anônima como solução candidata

Foi identificado um novo problema: sem qualquer distinção técnica entre
usuários, uma mesma pessoa poderia registrar múltiplas entradas. Uma
solução candidata para o MVP é utilizar uma sessão anônima por
navegador/dispositivo, permitindo que o sistema saiba que aquela sessão
já possui uma ocupação ativa sem precisar conhecer nome, e-mail ou
outros dados pessoais.

Essa alternativa ainda deverá ser avaliada tecnicamente nas próximas
fases e não é uma decisão de implementação fechada.

## 10. Fila --- conceito aprovado, comportamento em aberto

A fila permanece como parte importante da visão do produto,
especialmente quando um espaço atingir sua capacidade máxima.
Entretanto, o comportamento exato ainda precisa ser definido.

-   Reserva automática da vaga para a primeira pessoa da fila.

-   Oferta da vaga com um período para confirmação.

-   Fila apenas informativa, avisando que uma vaga foi liberada.

A opção de confirmação é uma candidata interessante, mas o tempo de
espera e a regra de liberação dependerão do contexto real do ambiente e
serão discutidos posteriormente.

## 11. Administração e analytics

O administrador de referência no piloto será o RH, sem tornar essa
função exclusiva desse departamento. Em outras empresas, Facilities,
Administração, Workplace, People ou outra equipe poderá exercer o mesmo
papel.

-   Cadastrar e gerenciar espaços.

-   Definir ou alterar capacidade.

-   Acompanhar ocupação e adoção do SharedSpace.

-   Consultar dados agregados e históricos.

-   Analisar horários de pico, ocupação média, permanência e demanda.

Princípio: o SharedSpace fornece informação; a organização decide como
utilizá-la.

## 12. Organização e multi-tenancy

O MVP atenderá uma única organização. A visão futura permite múltiplas
empresas, mas multi-tenancy, isolamento entre organizações e
complexidades associadas não serão implementados antecipadamente.

Princípio de engenharia adotado: projetar sabendo que o futuro existe,
sem implementar o futuro antes de existir necessidade.

## 13. Métricas de sucesso do piloto

  -----------------------------------------------------------------------
  Indicador                           O que queremos observar
  ----------------------------------- -----------------------------------
  Adoção                              Colaboradores utilizam o sistema
                                      voluntariamente e retornam em dias
                                      diferentes.

  Confiabilidade                      A ocupação apresentada geralmente
                                      corresponde à situação real do
                                      espaço.

  Impacto                             Usuários relatam ter evitado
                                      deslocamentos, espera ou situações
                                      de lotação.

  Retenção                            Após experimentar o SharedSpace,
                                      parte dos colaboradores continua
                                      utilizando-o.

  Satisfação                          Usuários consideram a experiência
                                      simples e útil e demonstram
                                      interesse em continuar utilizando.

  Feedback qualitativo                Usuários identificam benefícios,
                                      dificuldades e melhorias concretas
                                      após o uso.
  -----------------------------------------------------------------------

## 14. Perguntas de validação para usuários

-   O SharedSpace já evitou que você fosse até o espaço quando ele
    estava cheio?

-   Você confiou na ocupação mostrada?

-   O que mais ajudou durante o uso?

-   O que incomodou ou dificultou a utilização?

-   Houve algum momento em que você deixou de usar? Por quê?

-   Você continuaria utilizando o SharedSpace?

-   Se o SharedSpace desaparecesse amanhã, faria alguma diferença para
    você?

## 15. Decisões consolidadas da Discovery

  -----------------------------------------------------------------------
  Tema                                Decisão atual
  ----------------------------------- -----------------------------------
  Ocupação                            Manual

  Entrada                             Manual e rápida

  Saída                               Manual

  Identidade pública                  Anônima

  Representação visual                Assentos/avatares anônimos

  Proteção contra duplicidade         Sessão anônima é candidata; decisão
                                      técnica futura

  Timeout                             Fora do comportamento inicial;
                                      poderá ser validado depois

  Analytics                           Agregado por espaço

  Fila                                Aprovada conceitualmente; fluxo
                                      ainda em aberto

  Sensores / IoT                      Fora do MVP

  QR Code                             Possível evolução futura

  Organizações                        Uma no MVP

  Multi-tenancy                       Possível evolução futura

  Piloto                              Uma organização e inicialmente a
                                      copa
  -----------------------------------------------------------------------

## 16. Princípios do SharedSpace

-   SharedSpace monitora espaços, não pessoas.

-   A interação principal deve ser rápida, leve e intuitiva.

-   Coletar apenas os dados necessários para entregar valor.

-   SharedSpace fornece informação; a organização toma a decisão.

-   Projetar para evolução sem implementar complexidade futura
    antecipadamente.

-   Validar hipóteses com usuários reais antes de adicionar soluções
    mais complexas.

## 17. Encerramento da Fase 1

A Fase 1 --- Discovery é considerada concluída. O projeto possui um
problema definido, uma hipótese de solução, atores identificados, fluxo
inicial, riscos conhecidos, princípios de privacidade, limites de escopo
e critérios iniciais de sucesso. O próximo passo é a Fase 2 ---
Requisitos, na qual essas descobertas serão transformadas em requisitos
funcionais, requisitos não funcionais, regras de negócio, user stories e
critérios de aceitação antes da definição final do MVP.

# SharedSpace --- Checkpoint 02

**Fase 2 --- Requisitos**

Este checkpoint consolida o levantamento de requisitos do SharedSpace
após a Discovery. O objetivo da fase foi transformar as necessidades
identificadas em comportamentos, restrições, regras de negócio,
histórias de usuário e critérios de aceitação, sem antecipar decisões de
arquitetura ou implementação.

## 1. Escopo funcional levantado

O SharedSpace possui dois atores principais nesta fase:

-   Colaborador: consulta disponibilidade, realiza check-in/check-out e
    utiliza a política de espera configurada para o espaço.

-   Administrador da organização: cadastra e gerencia espaços, configura
    regras operacionais e consulta indicadores agregados.

## 2. Requisitos Funcionais (RF)

  -----------------------------------------------------------------------
  Código                  Nome                    Descrição
  ----------------------- ----------------------- -----------------------
  RF-01                   Consultar espaços       Permitir que o
                                                  colaborador visualize
                                                  os espaços disponíveis,
                                                  sua ocupação atual e
                                                  disponibilidade.

  RF-02                   Entrar na fila          Permitir que o
                                                  colaborador entre na
                                                  fila de espera quando a
                                                  política do espaço for
                                                  fila prioritária e não
                                                  houver vaga.

  RF-03                   Check-in                Permitir que o
                                                  colaborador registre
                                                  sua entrada ao chegar
                                                  ao espaço.

  RF-04                   Check-out               Permitir que o
                                                  colaborador registre
                                                  sua saída ao terminar
                                                  de utilizar o espaço.

  RF-05                   Cadastrar espaço        Permitir que o
                                                  administrador cadastre
                                                  um espaço, incluindo
                                                  nome, capacidade máxima
                                                  e descrição.

  RF-06                   Editar espaço           Permitir que o
                                                  administrador edite
                                                  nome, capacidade,
                                                  descrição e
                                                  configurações
                                                  permitidas.

  RF-07                   Desativar/reativar      Permitir que o
                          espaço                  administrador desative
                                                  temporariamente e
                                                  reative um espaço,
                                                  preservando cadastro e
                                                  histórico.

  RF-08                   Excluir espaço          Permitir que o
                                                  administrador exclua um
                                                  espaço quando
                                                  necessário; o
                                                  comportamento
                                                  definitivo sobre
                                                  histórico permanece
                                                  pendente.

  RF-09                   Visualizar ocupação     Permitir que o
                          administrativa          administrador acompanhe
                                                  informações de ocupação
                                                  dos espaços.

  RF-10                   Identificar picos       Permitir que o
                                                  administrador
                                                  identifique períodos de
                                                  maior utilização.

  RF-11                   Tempo médio             Permitir que o
                                                  administrador visualize
                                                  o tempo médio de
                                                  utilização dos espaços.

  RF-12                   Indicadores agregados   Permitir acompanhamento
                                                  de utilizações, sessões
                                                  concluídas e outros
                                                  indicadores agregados,
                                                  sem identificação
                                                  individual.

  RF-13                   Fila prioritária        Permitir que o
                                                  colaborador entre em
                                                  fila quando o espaço
                                                  estiver lotado e essa
                                                  política estiver
                                                  configurada.

  RF-14                   Aviso de prioridade     Informar ao primeiro
                                                  usuário elegível da
                                                  fila quando uma vaga
                                                  for liberada.

  RF-15                   Política de espera      Permitir que o
                                                  administrador configure
                                                  por espaço: sem espera,
                                                  alerta de
                                                  disponibilidade ou fila
                                                  com prioridade.

  RF-16                   Controle de permanência Permitir que o
                                                  administrador
                                                  ative/desative e
                                                  configure um tempo
                                                  esperado de utilização
                                                  por espaço, sujeito às
                                                  regras de confirmação.
  -----------------------------------------------------------------------

## 3. Funcionalidade candidata --- QR Code

O QR Code não foi tratado como requisito central, pois é uma solução
específica para uma necessidade já existente: tornar o check-in
presencial rápido e contextual. A ideia evoluiu de possibilidade futura
para candidata real ao MVP.

-   Cada espaço poderá possuir um QR Code associado.

-   Ao escanear, o usuário poderá acessar diretamente o espaço
    correspondente e confirmar o check-in.

-   O QR Code não deve ser obrigatório para consultar disponibilidade
    remotamente.

-   O QR Code facilita o gatilho de entrada, mas não elimina sozinho o
    risco de check-out esquecido.

-   A decisão final de inclusão será tomada na Fase 3 --- MVP.

## 4. Regras de Negócio (RN)

  -----------------------------------------------------------------------
  Código                  Regra                   Definição
  ----------------------- ----------------------- -----------------------
  RN-01                   Fila disponível         A entrada em fila deve
                          conforme política       obedecer à política
                                                  configurada para o
                                                  espaço.

  RN-02                   Ocupação única por      Uma mesma sessão não
                          sessão                  pode possuir mais de
                                                  uma ocupação ativa
                                                  simultaneamente no
                                                  mesmo espaço.

  RN-03                   Limite de capacidade    Um check-in nunca pode
                                                  elevar a ocupação acima
                                                  da capacidade máxima.

  RN-04                   Liberação no check-out  O check-out encerra a
                                                  ocupação ativa e libera
                                                  uma vaga, acionando a
                                                  política de espera
                                                  aplicável.

  RN-05                   Capacidade válida       A capacidade máxima
                                                  deve ser um valor
                                                  positivo maior que
                                                  zero.

  RN-06                   Redução de capacidade   A capacidade não pode
                                                  ser reduzida abaixo da
                                                  quantidade de ocupações
                                                  ativas.

  RN-07                   Campos mínimos          Nome e capacidade são
                                                  obrigatórios; descrição
                                                  é opcional.

  RN-08                   Espaço desativado       Espaço desativado não
                                                  deve aceitar uso dos
                                                  colaboradores, mas deve
                                                  preservar histórico e
                                                  informações
                                                  administrativas.

  RN-09                   Exclusão restritiva     Excluir é uma ação mais
                                                  restritiva que
                                                  desativar; o efeito
                                                  definitivo sobre dados
                                                  históricos será
                                                  definido
                                                  posteriormente.

  RN-10                   Ordem da fila           A fila prioritária deve
                                                  respeitar a ordem de
                                                  entrada.

  RN-11                   Prioridade temporária   Ao liberar uma vaga, o
                                                  primeiro usuário
                                                  elegível da fila recebe
                                                  prioridade temporária.

  RN-12                   Expiração da prioridade Se a prioridade não for
                                                  utilizada dentro da
                                                  janela definida, ela
                                                  expira e passa ao
                                                  próximo usuário
                                                  elegível.

  RN-13                   Alerta sem reserva      No modo alerta de
                                                  disponibilidade, avisos
                                                  não reservam vagas nem
                                                  estabelecem prioridade.

  RN-14                   Fila realmente          No modo fila
                          prioritária             prioritária, a ordem
                                                  deve ser protegida
                                                  durante a janela de
                                                  prioridade.

  RN-15                   Timeout configurável    O administrador pode
                                                  configurar por espaço
                                                  um tempo esperado de
                                                  utilização e
                                                  ativar/desativar esse
                                                  controle.

  RN-16                   Confirmação de          Ao se aproximar do
                          permanência             limite configurado, o
                                                  sistema deve solicitar
                                                  confirmação de
                                                  permanência.

  RN-17                   Expiração por ausência  A sessão poderá expirar
                          de resposta             após uma janela
                                                  adicional sem resposta;
                                                  duração e comportamento
                                                  exatos permanecem em
                                                  aberto.

  RN-18                   Abandono da fila        O usuário pode sair
                                                  voluntariamente da fila
                                                  enquanto aguarda.

  RN-19                   Prioridade abandonada   Prioridade não
                                                  utilizada deve expirar
                                                  automaticamente e
                                                  seguir para o próximo
                                                  elegível.

  RN-20                   Múltiplas vagas         Quando múltiplas vagas
                                                  forem liberadas, o
                                                  mesmo número de
                                                  usuários no início da
                                                  fila recebe prioridade,
                                                  respeitando a ordem.

  RN-21                   Desativação sem         Um espaço só pode ser
                          ocupação                desativado quando não
                                                  possuir ocupações
                                                  ativas.

  RN-22                   Confirmação de operação O sistema não deve
                                                  apresentar uma operação
                                                  como concluída sem
                                                  confirmação de que foi
                                                  efetivamente
                                                  registrada.

  RN-23                   Repetição segura de     Repetir uma tentativa
                          check-in                da mesma sessão não
                                                  deve criar múltiplas
                                                  ocupações ativas.
  -----------------------------------------------------------------------

## 5. Requisitos Não Funcionais (RNF)

  -----------------------------------------------------------------------
  Código                  Tema                    Requisito
  ----------------------- ----------------------- -----------------------
  RNF-01                  Baixa fricção           As ações principais
                                                  devem exigir o mínimo
                                                  possível de etapas e
                                                  interação.

  RNF-02                  Aprendizado imediato    Consulta, check-in e
                                                  check-out devem ser
                                                  compreensíveis sem
                                                  treinamento.

  RNF-03                  Responsividade          A interface deve
                                                  funcionar adequadamente
                                                  em smartphones, tablets
                                                  e computadores.

  RNF-04                  Desempenho percebido    Operações principais
                                                  devem responder
                                                  rapidamente em
                                                  condições normais de
                                                  uso.

  RNF-05                  Atualização de ocupação Alterações de ocupação
                                                  devem ser refletidas
                                                  para os demais usuários
                                                  com baixo atraso.

  RNF-06                  Privacidade pública     A visualização pública
                                                  não deve expor dados
                                                  pessoais dos ocupantes.

  RNF-07                  Minimização de dados    O sistema deve coletar
                                                  somente informações
                                                  necessárias às
                                                  funcionalidades
                                                  previstas.

  RNF-08                  Acesso administrativo   Funcionalidades
                                                  administrativas devem
                                                  ser restritas a
                                                  usuários autorizados.

  RNF-09                  Consistência            Ações simultâneas não
                          concorrente             devem produzir estados
                                                  inválidos, como
                                                  ocupação acima da
                                                  capacidade.

  RNF-10                  Clareza                 A interface do
                                                  colaborador deve
                                                  priorizar
                                                  disponibilidade e
                                                  ocupação, evitando
                                                  informações
                                                  desnecessárias.

  RNF-11                  Confiabilidade          O estado do sistema
                                                  deve permanecer
                                                  consistente com os
                                                  registros efetivamente
                                                  realizados.

  RNF-12                  Feedback                Check-in, check-out,
                                                  fila e outras ações
                                                  relevantes devem
                                                  produzir feedback
                                                  visual imediato e
                                                  claro.

  RNF-13                  Acessibilidade visual   Estados importantes não
                                                  podem ser comunicados
                                                  exclusivamente por
                                                  cores.

  RNF-14                  Legibilidade            Textos, botões e
                                                  informações essenciais
                                                  devem ter contraste,
                                                  tamanho e organização
                                                  adequados.

  RNF-15                  Interação por toque     Controles essenciais
                                                  devem possuir áreas
                                                  adequadas para uso em
                                                  dispositivos móveis.

  RNF-16                  Disponibilidade do      O sistema deve
                          sistema                 permanecer acessível
                                                  nos períodos esperados
                                                  de utilização, salvo
                                                  falhas ou interrupções
                                                  planejadas.

  RNF-17                  Tratamento de falhas    Falhas devem ser
                                                  comunicadas claramente
                                                  e não podem produzir
                                                  feedback falso de
                                                  sucesso.
  -----------------------------------------------------------------------

## 6. Políticas de espera por espaço

O administrador poderá, conceitualmente, escolher entre três
comportamentos:

-   Sem espera: quando lotado, o usuário apenas consulta novamente em
    outro momento.

-   Alerta de disponibilidade: interessados são avisados quando surge
    vaga, mas não existe reserva nem prioridade.

-   Fila com prioridade: a ordem de espera é respeitada e vagas
    liberadas concedem prioridade temporária aos primeiros usuários
    elegíveis.

A flexibilidade foi definida por espaço, e não obrigatoriamente por
empresa inteira, pois ambientes distintos podem exigir políticas
diferentes.

## 7. Controle de permanência e check-out esquecido

-   O comportamento principal continua sendo check-in e check-out
    manuais.

-   O administrador poderá configurar um tempo esperado de utilização
    por espaço.

-   Ao se aproximar desse tempo, o usuário poderá receber uma
    solicitação de confirmação de permanência.

-   Confirmar permanência mantém a ocupação ativa; realizar check-out
    libera a vaga.

-   Se não houver resposta, poderá existir uma janela adicional antes da
    expiração.

-   Os tempos exatos e o comportamento definitivo da expiração
    permanecem pendentes para MVP/UX/arquitetura.

## 8. Privacidade e identificação técnica

Permanece válido o princípio: "SharedSpace monitora espaços, não
pessoas". A aplicação pública não precisa exibir nomes dos ocupantes e
os analytics devem permanecer agregados.

Entretanto, ocupação única, fila e alertas exigem distinguir
tecnicamente participantes. Uma sessão anônima persistente por
navegador/dispositivo permanece como solução candidata, sem necessidade
de nome, e-mail ou outro dado pessoal. A implementação não foi fechada
nesta fase.

## 9. Analytics definidos

-   Ocupação atual e histórica por espaço.

-   Períodos/horários de maior movimento.

-   Ocupação máxima e padrões de demanda.

-   Tempo médio de utilização.

-   Quantidade de utilizações/check-ins e sessões concluídas.

-   Indicadores agregados de utilização do SharedSpace.

A métrica "porcentagem de colaboradores que usam o app" não foi aprovada
como métrica confiável nesta fase, pois o produto não identifica
individualmente colaboradores. Quantidade de sessões não equivale a
quantidade de pessoas únicas.

## 10. User Stories e critérios de aceitação

### US-01 --- Consultar disponibilidade

Como colaborador, quero visualizar a ocupação atual dos espaços para
decidir se devo me deslocar até eles.

**Critérios de aceitação:**

1.  Exibir nome do espaço.

2.  Exibir ocupação atual, como 3/5.

3.  Informar claramente se há vaga.

4.  Informar quantidade de vagas livres.

5.  Indicar explicitamente quando estiver lotado.

6.  Apresentar a ação de espera compatível com a política configurada.

7.  Não depender apenas de cor para comunicar o estado.

### US-02 --- Realizar check-in

Como colaborador, quero realizar o check-in ao chegar a um espaço, para
manter sua ocupação atualizada e ajudar meus colegas a consultarem sua
disponibilidade.

**Critérios de aceitação:**

8.  Permitir check-in quando houver vaga.

9.  Aumentar a ocupação em uma unidade após sucesso.

10. Impedir duas ocupações ativas da mesma sessão no mesmo espaço.

11. Nunca ultrapassar a capacidade máxima.

12. Exibir confirmação clara de sucesso.

13. Não apresentar sucesso se a operação falhar.

### US-03 --- Realizar check-out

Como colaborador, quero realizar o check-out ao sair de um espaço, para
manter sua ocupação atualizada e permitir que meus colegas saibam que
uma vaga foi liberada.

**Critérios de aceitação:**

14. Só permitir check-out quando houver ocupação ativa.

15. Encerrar a ocupação ativa.

16. Reduzir a ocupação em uma unidade.

17. Aplicar a política de espera à vaga liberada.

18. Exibir confirmação clara.

19. Não apresentar sucesso em caso de falha.

20. Permitir novo check-in futuro após a saída.

### US-04 --- Fila prioritária

Como colaborador, quero entrar na fila de um espaço lotado para ter
prioridade quando uma vaga for liberada.

**Critérios de aceitação:**

21. Disponibilizar a opção apenas quando a política aplicável for fila
    prioritária.

22. Exibir a posição do usuário.

23. Impedir múltiplas posições da mesma sessão.

24. Permitir abandono da fila.

25. Respeitar ordem de entrada.

26. Conceder prioridade temporária ao primeiro elegível.

27. Passar a prioridade adiante quando expirar.

28. Tratar múltiplas vagas respeitando a ordem.

### US-05 --- Alerta de disponibilidade

Como colaborador, quero solicitar um alerta quando um espaço lotado
liberar uma vaga para saber quando existe uma nova oportunidade de
utilizá-lo.

**Critérios de aceitação:**

29. Disponibilizar conforme política de alerta.

30. Permitir solicitação quando não houver disponibilidade.

31. Avisar interessados quando houver liberação.

32. Não reservar a vaga.

33. Deixar claro que o alerta não garante prioridade.

### US-06 --- Cadastrar espaço

Como administrador, quero cadastrar um espaço compartilhado para
disponibilizá-lo no SharedSpace com suas regras de utilização.

**Critérios de aceitação:**

34. Permitir nome e capacidade máxima.

35. Permitir descrição opcional.

36. Exigir nome e capacidade.

37. Exigir capacidade maior que zero.

38. Permitir definir política de espera.

39. Disponibilizar o espaço conforme status/configuração após cadastro
    válido.

### US-07 --- Editar espaço

Como administrador, quero editar um espaço cadastrado para manter suas
informações e regras adequadas à realidade da organização.

**Critérios de aceitação:**

40. Permitir alterar nome, descrição e capacidade.

41. Permitir alterar configurações suportadas.

42. Impedir capacidade inferior à ocupação atual.

43. Não substituir dados válidos por alterações inválidas.

44. Refletir alterações válidas no sistema.

### US-08 --- Desativar e reativar espaço

Como administrador, quero desativar temporariamente um espaço para
impedir sua utilização sem perder seu cadastro e histórico.

**Critérios de aceitação:**

45. Permitir desativação quando não houver ocupações ativas.

46. Bloquear desativação com ocupações ativas.

47. Impedir novos check-ins em espaços desativados.

48. Preservar histórico.

49. Permitir reativação posterior.

### US-09 --- Excluir espaço

Como administrador, quero excluir um espaço quando seu cadastro não for
mais necessário.

**Critérios de aceitação:**

50. A exclusão deve ser uma ação administrativa explícita.

51. O tratamento de histórico, exclusão física ou lógica permanece
    pendente para decisão de dados/arquitetura.

### US-10 --- Configurar controle de permanência

Como administrador, quero configurar o controle de tempo de utilização
de um espaço para reduzir ocupações que permanecem ativas por
esquecimento.

**Critérios de aceitação:**

52. Permitir ativar/desativar por espaço.

53. Permitir definir tempo esperado.

54. Solicitar confirmação ao atingir o período configurado.

55. Manter ocupação se o usuário confirmar permanência.

56. Liberar vaga se houver check-out.

57. Definir posteriormente a regra exata para ausência de resposta.

### US-11 --- Visualizar analytics

Como administrador, quero visualizar dados agregados sobre a utilização
dos espaços para compreender padrões de ocupação e apoiar decisões da
organização.

**Critérios de aceitação:**

58. Exibir dados de ocupação.

59. Identificar períodos de maior movimento.

60. Exibir tempo médio de utilização.

61. Exibir quantidade de utilizações.

62. Manter indicadores agregados por espaço.

63. Não identificar individualmente colaboradores.

## 11. Casos extremos revisados

  -----------------------------------------------------------------------
  Caso                                Decisão
  ----------------------------------- -----------------------------------
  Check-out esquecido                 Controle de permanência
                                      configurável e confirmação são
                                      candidatos; comportamento manual
                                      permanece base.

  Usuário abandona fila               Saída voluntária permitida;
                                      prioridade não utilizada expira.

  Duas ou mais vagas liberadas        Prioridades distribuídas aos
                                      primeiros usuários elegíveis em
                                      quantidade equivalente às vagas.

  Desativação com ocupação ativa      Bloqueada no MVP; estado
                                      intermediário \'encerrando\' foi
                                      deliberadamente adiado.

  Falha durante check-in/check-out    Não informar sucesso sem
                                      confirmação e impedir duplicidade
                                      em novas tentativas.

  Usuário fora da fila chega quando   No modo fila prioritária, a
  vaga abre                           prioridade deve ser efetivamente
                                      protegida durante a janela; no modo
                                      alerta, não existe proteção.
  -----------------------------------------------------------------------

## 12. Decisões deliberadamente pendentes

-   Implementação técnica da sessão anônima e sua persistência.

-   Mecanismo técnico para alertas/notificações.

-   Duração exata da janela de prioridade da fila.

-   Duração padrão e janela adicional do controle de permanência.

-   Comportamento definitivo quando o usuário ignora a confirmação de
    permanência.

-   Semântica de exclusão de espaços e preservação de histórico.

-   Inclusão ou não do QR Code no MVP.

-   Metas quantitativas finais de desempenho e disponibilidade, a serem
    definidas quando houver arquitetura e ambiente de teste.

## 13. Decisões de escopo preservadas

-   MVP pensado inicialmente para uma única organização.

-   Piloto inicial focado na copa, embora o domínio suporte múltiplos
    tipos de espaço.

-   Multi-tenancy permanece evolução futura.

-   Sensores e IoT permanecem fora do MVP.

-   Identidade pública dos ocupantes permanece fora do escopo.

-   O administrador de referência do piloto pode ser o RH, mas o domínio
    utiliza o papel genérico \'administrador da organização\'.

-   A interface do colaborador prioriza consulta rápida; a área
    administrativa pode concentrar gestão e analytics.

## 14. Princípios reafirmados na Fase 2

-   SharedSpace monitora espaços, não pessoas.

-   Ações recorrentes devem ter baixa fricção.

-   Uma fila só deve ser chamada de fila se a prioridade for realmente
    protegida.

-   Configuração deve existir quando há necessidade real, não apenas
    possibilidade futura.

-   Privacidade não deve ser sacrificada apenas para obter métricas
    adicionais.

-   Erros humanos e erros do sistema devem ser distinguidos.

-   Projetar para evolução sem implementar antecipadamente toda a
    complexidade futura.

-   Requisito descreve necessidade; arquitetura e tecnologia serão
    escolhidas depois.

## 15. Status da Fase 2

A Fase 2 --- Requisitos é considerada concluída. Os requisitos
funcionais, não funcionais, regras de negócio, histórias de usuário,
critérios de aceitação e principais casos extremos foram levantados e
revisados. As incertezas restantes estão explicitamente registradas para
serem resolvidas nas fases adequadas, sem bloquear o avanço.

Próxima etapa: Fase 3 --- Definição do MVP. Nela, os requisitos serão
priorizados e o time decidirá o conjunto mínimo de funcionalidades
necessário para colocar uma primeira versão utilizável nas mãos dos
colaboradores e validar as hipóteses centrais do SharedSpace.

**SharedSpace**

**Checkpoint 03**

**FASE 3 --- DEFINIÇÃO DO MVP**

  -----------------------------------------------------------------------
  **Escopo congelado para o primeiro piloto: 1 organização • 1 espaço
  (Copa) • capacidade 5**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

*Documento oficial de priorização e encerramento da Fase 3*

# 1. Objetivo deste checkpoint

Este checkpoint consolida as decisões tomadas durante a Fase 3 ---
Definição do MVP. Seu objetivo é transformar o conjunto de requisitos
levantado na Fase 2 em um escopo priorizado, pequeno, coerente e
utilizável para o primeiro piloto real do SharedSpace.

A Fase 3 não redefine os requisitos anteriores sem necessidade. Ela
determina quais deles são necessários agora para validar a hipótese
principal, quais melhoram significativamente o piloto, quais podem
entrar apenas se houver tempo e quais foram deliberadamente adiados.

# 2. Conceito de MVP adotado

MVP (Minimum Viable Product) não é uma versão ruim ou incompleta do
produto. Para o SharedSpace, MVP significa a menor versão capaz de
entregar valor real em um ambiente real e produzir aprendizado confiável
sobre a hipótese do produto.

  -----------------------------------------------------------------------
  **Princípio da Fase 3: uma funcionalidade só pertence ao MVP quando sua
  ausência compromete a entrega de valor, a confiabilidade do piloto ou a
  capacidade de validar a hipótese escolhida.**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

# 3. Objetivo exato do MVP

Disponibilizar uma primeira versão utilizável do SharedSpace na copa
piloto, permitindo que colaboradores consultem sua disponibilidade e
mantenham a ocupação atualizada por meio de check-in e check-out, para
avaliar se o sistema reduz incerteza e deslocamentos desnecessários e se
os registros manuais são confiáveis o suficiente para sustentar essa
experiência.

Como objetivo complementar, o MVP deverá registrar e apresentar dados
agregados básicos que permitam compreender a utilização do espaço e
avaliar o comportamento do piloto.

# 4. Hipótese do MVP

  -----------------------------------------------------------------------
  **Se os colaboradores conseguirem consultar rapidamente a
  disponibilidade da copa e registrar sua entrada e saída com baixa
  fricção, então o SharedSpace poderá fornecer uma ocupação
  suficientemente confiável para ajudá-los a decidir quando utilizar o
  espaço e evitar deslocamentos desnecessários.**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

A hipótese será validada com usuários reais. Ela não é tratada como
resultado garantido. O piloto deverá produzir evidências quantitativas e
qualitativas para confirmar, refutar ou ajustar essa hipótese.

# 5. Priorização do escopo

A priorização utiliza quatro categorias: MUST HAVE, SHOULD HAVE, COULD
HAVE e NOT NOW. Prioridade representa necessidade para este piloto, e
não importância absoluta para a visão futura do produto.

## MUST HAVE

  -----------------------------------------------------------------------
  **Item**                            **Decisão / justificativa**
  ----------------------------------- -----------------------------------
  **Consulta de ocupação**            Nome do espaço, ocupação atual,
                                      vagas livres e indicação explícita
                                      de lotação.

  **Check-in manual e simples**       Registra entrada, respeita
                                      capacidade, evita duplicidade e só
                                      confirma sucesso após registro
                                      efetivo.

  **Check-out manual e simples**      Encerra a ocupação ativa, libera
                                      vaga e permite novo check-in
                                      futuro.

  **Sessão anônima**                  Distingue tecnicamente sessões sem
                                      exigir nome, e-mail ou conta
                                      individual.

  **Atualização com baixo atraso**    Mudanças de ocupação devem chegar
                                      aos demais usuários em tempo
                                      compatível com a utilidade da
                                      consulta.

  **Clareza visual da ocupação**      Estados devem ser compreendidos
                                      rapidamente e não podem depender
                                      exclusivamente de cor.

  **Histórico mínimo do piloto**      Registra informações necessárias
                                      para avaliar utilizações, sessões
                                      concluídas e duração.

  **Proteção simples da área          Restringe funções administrativas
  administrativa**                    sem exigir sistema completo de
                                      identidade.

  **Controle de permanência 30 + 5**  Após 30 minutos solicita
                                      confirmação; sem resposta por mais
                                      5 minutos, encerra automaticamente
                                      a sessão.

  **Analytics administrativo básico** Apresenta indicadores agregados
                                      essenciais para acompanhamento e
                                      avaliação do piloto.
  -----------------------------------------------------------------------

## SHOULD HAVE

  -----------------------------------------------------------------------
  **Item**                            **Decisão / justificativa**
  ----------------------------------- -----------------------------------
  **Fila prioritária**                Organiza espera quando lotado,
                                      protege ordem e concede prioridade
                                      temporária.

  **Editar espaço**                   Permite alterar informações
                                      básicas, especialmente nome,
                                      descrição e capacidade.

  **Desativar/reativar espaço**       Permite indisponibilidade
                                      temporária; desativação é bloqueada
                                      com ocupações ativas.
  -----------------------------------------------------------------------

## COULD HAVE

  -----------------------------------------------------------------------
  **Item**                            **Decisão / justificativa**
  ----------------------------------- -----------------------------------
  **QR Code**                         Reduz atrito do check-in
                                      presencial, mas o check-in funciona
                                      sem ele.

  **Alerta de disponibilidade**       Avisa quando surge vaga, sem
                                      reserva nem prioridade.

  **Representação elaborada do        Mesa, cadeiras/assentos e avatares
  espaço**                            anônimos como refinamento visual.

  **Dashboard e gráficos elaborados** Visualizações adicionais além dos
                                      analytics básicos obrigatórios.

  **Animações e microinterações**     Polimento visual que não condiciona
                                      a validação do MVP.
  -----------------------------------------------------------------------

## NOT NOW

  -----------------------------------------------------------------------
  **Item**                            **Decisão / justificativa**
  ----------------------------------- -----------------------------------
  **Cadastro de novos espaços**       O primeiro piloto já possui uma
                                      copa conhecida.

  **Exclusão de espaços**             Não resolve necessidade atual e
                                      exigiria fechar a semântica do
                                      histórico.

  **Uso efetivo de múltiplos          O domínio permanece genérico, mas o
  espaços**                           piloto utiliza somente uma copa.

  **Multi-tenancy**                   O MVP atende uma única organização.

  **Sistema completo de               Cadastro, recuperação de senha,
  autenticação**                      OAuth e gestão completa de usuários
                                      ficam adiados.

  **Conta/login individual de         A identificação técnica será
  colaboradores**                     anônima no piloto.

  **Sensores e IoT**                  Ocupação permanece baseada em
                                      check-in/check-out manual.

  **Identificação pública de          Ocupação pública permanece anônima.
  ocupantes**                         
  -----------------------------------------------------------------------

# 6. Decisões específicas do piloto

-   O piloto atenderá uma única organização.

-   O primeiro e único espaço utilizado no piloto será a Copa.

-   A capacidade inicial da Copa será 5.

-   O domínio continuará utilizando o conceito genérico de espaço
    > (Space), evitando acoplamento conceitual à Copa.

-   O colaborador não terá conta ou login individual no MVP.

-   A distinção técnica entre participantes será realizada por uma
    > sessão anônima; sua implementação será definida na arquitetura.

-   A mesma pessoa usando navegadores ou dispositivos diferentes poderá
    > ser percebida como sessões diferentes; essa limitação é aceita no
    > MVP.

-   A área administrativa terá proteção simples apropriada ao piloto,
    > sem sistema completo de gerenciamento de identidade.

-   O controle de permanência utilizará tempo fixo no piloto; não haverá
    > tela administrativa para configurar esse tempo.

# 7. Controle de permanência

O controle de permanência foi promovido a MUST HAVE por proteger a
confiabilidade da ocupação em um cenário no qual o esquecimento de
check-out é considerado provável.

  -----------------------------------------------------------------------
  **Regra do piloto: 30 minutos → solicitar confirmação → 5 minutos
  adicionais → sem resposta, encerramento automático.**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

-   Se o usuário confirmar que continua utilizando a Copa, a sessão
    > permanece ativa.

-   Se o usuário realizar check-out, a sessão é encerrada imediatamente.

-   Se nenhuma resposta ocorrer durante a janela adicional de 5 minutos,
    > a sessão é encerrada automaticamente e a vaga é liberada.

-   Os 30 minutos representam o tempo esperado para confirmação, e não
    > um limite obrigatório de permanência física no espaço.

# 8. Analytics e dados do piloto

O MVP deverá registrar histórico mínimo e apresentar analytics
administrativos básicos e agregados. A coleta de dados e a visualização
administrativa são partes distintas, mas ambas foram classificadas como
MUST HAVE.

-   Quantidade de utilizações/check-ins.

-   Quantidade de sessões concluídas.

-   Tempo médio de utilização.

-   Períodos ou horários de maior movimento.

-   Informações de ocupação necessárias para avaliar o piloto.

Gráficos sofisticados, múltiplas visualizações, filtros avançados e
dashboards elaborados permanecem COULD HAVE. Os indicadores não devem
identificar individualmente colaboradores.

# 9. Fluxo principal do MVP

64. O colaborador abre o SharedSpace e consulta a Copa.

65. O sistema apresenta ocupação atual, capacidade, vagas livres e
    estado de lotação.

66. Com base nessa informação, o colaborador decide se deve se deslocar.

67. Ao chegar, realiza check-in manual.

68. O sistema valida capacidade e a sessão anônima, impede duplicidade e
    confirma a operação somente após registro efetivo.

69. A ocupação é incrementada e refletida aos demais usuários com baixo
    atraso.

70. Durante a utilização, a sessão permanece ativa.

71. Após 30 minutos, o sistema solicita confirmação de permanência.

72. Se o usuário confirmar, a sessão continua; se fizer check-out, a
    vaga é liberada; sem resposta por 5 minutos, a sessão é encerrada
    automaticamente.

73. Ao sair normalmente, o colaborador realiza check-out.

74. A ocupação é reduzida e a vaga volta a ficar disponível.

75. Os dados necessários da sessão alimentam o histórico e os analytics
    agregados do piloto.

# 10. Comportamento quando o espaço estiver lotado

A indicação de lotação faz parte do núcleo obrigatório. Um MVP sem fila
ainda é considerado válido se informar corretamente que a Copa está 5/5
e sem vagas.

A fila prioritária permanece SHOULD HAVE. Caso seja implementada, deverá
respeitar ordem de entrada, impedir posições duplicadas, permitir
abandono, conceder prioridade temporária, tratar expiração e distribuir
múltiplas vagas aos primeiros elegíveis. A duração exata da janela de
prioridade será definida na fase de UX.

# 11. Limites explícitos de escopo

-   Não implementar funcionalidades apenas porque podem ser úteis
    > futuramente.

-   Não transformar a proteção administrativa do piloto em um sistema
    > completo de usuários.

-   Não implementar login individual de colaboradores para obter
    > métricas de pessoas únicas.

-   Não implementar multi-tenancy.

-   Não implementar sensores ou IoT.

-   Não exigir QR Code para consulta ou check-in.

-   Não depender de representação visual elaborada da Copa para
    > comunicar disponibilidade.

-   Não transformar analytics básico em uma plataforma extensa de BI.

-   Não exigir fila prioritária para considerar o MVP pronto.

-   Não adicionar novos MUST HAVE sem revisar conscientemente o impacto
    > sobre o escopo congelado.

# 12. Definição objetiva de "MVP pronto"

O SharedSpace estará pronto para iniciar o piloto quando todos os
critérios abaixo forem atendidos:

76. O colaborador consegue consultar a ocupação atual e a quantidade de
    vagas livres da Copa.

77. O colaborador consegue realizar check-in quando houver capacidade
    disponível.

78. O colaborador consegue realizar check-out de sua ocupação ativa.

79. O sistema impede que a ocupação ultrapasse a capacidade máxima de 5.

80. A mesma sessão não consegue criar ocupações ativas duplicadas no
    mesmo espaço.

81. Alterações de ocupação são refletidas aos demais usuários com baixo
    atraso.

82. A visualização pública da ocupação permanece anônima.

83. O controle de permanência de 30 minutos + janela adicional de 5
    minutos funciona conforme definido.

84. O histórico mínimo necessário para avaliar o piloto é registrado
    corretamente.

85. O administrador acessa, de forma protegida, analytics básicos e
    agregados.

86. Falhas de check-in, check-out e demais operações relevantes não são
    apresentadas falsamente como sucesso.

87. O fluxo principal funciona adequadamente em smartphone e desktop,
    com clareza, feedback visual e acessibilidade básica.

# 13. Requisitos não funcionais preservados

A priorização funcional não elimina os requisitos de qualidade definidos
na Fase 2. O MVP deverá continuar priorizando:

-   Baixa fricção e aprendizado imediato nas ações recorrentes.

-   Responsividade e abordagem mobile-first.

-   Desempenho percebido adequado nas operações principais.

-   Atualização da ocupação com baixo atraso.

-   Privacidade pública e minimização de dados.

-   Acesso administrativo restrito.

-   Consistência em ações simultâneas.

-   Feedback visual claro e ausência de falso sucesso.

-   Acessibilidade visual, legibilidade e controles adequados para
    > toque.

-   Confiabilidade e tratamento correto de falhas.

# 14. Riscos aceitos no MVP

-   A ocupação continua dependente da colaboração dos usuários para
    > check-in e check-out.

-   O encerramento automático após 35 minutos sem confirmação pode
    > liberar uma vaga enquanto a pessoa ainda estiver fisicamente no
    > espaço.

-   A sessão anônima não garante reconhecimento da mesma pessoa em
    > navegadores ou dispositivos diferentes.

-   A fila prioritária pode não estar presente na primeira versão
    > testável, pois permanece SHOULD HAVE.

-   A utilização em outros tipos de espaço ainda não será validada neste
    > piloto.

-   Os analytics do MVP serão deliberadamente básicos.

# 15. Decisões que pertencem às próximas fases

As decisões abaixo não devem ser antecipadas neste checkpoint, pois
pertencem a UX, arquitetura ou implementação:

-   Mecanismo técnico e persistência da sessão anônima.

-   Tecnologia utilizada para atualização de ocupação com baixo atraso.

-   Estratégia técnica para o temporizador e encerramento de sessões.

-   Stack de frontend, backend e banco de dados.

-   Modelo de persistência e estrutura das entidades.

-   Forma técnica da proteção administrativa.

-   Design final das telas e componentes.

-   Duração exata da prioridade da fila, caso a fila entre no piloto.

-   Mecanismo técnico de alertas/notificações, caso o alerta seja
    > implementado.

-   Detalhes de deploy, observabilidade e ambiente.

# 16. Princípios reafirmados

-   SharedSpace monitora espaços, não pessoas.

-   A interação principal deve ser rápida, leve e intuitiva.

-   Coletar apenas os dados necessários para entregar e avaliar valor.

-   Uma fila só deve ser chamada de fila se sua prioridade for realmente
    > protegida.

-   Boa UX é obrigatória; polimento sofisticado não é.

-   Dados e dashboard são decisões diferentes.

-   Projetar para evolução sem implementar antecipadamente a
    > complexidade futura.

-   Uma necessidade pode ser obrigatória sem que uma solução tecnológica
    > específica também seja.

-   O MVP é um experimento utilizável, não uma versão ruim do produto
    > final.

# 17. Escopo congelado e controle de mudanças

  -----------------------------------------------------------------------
  **A partir deste checkpoint, o escopo do MVP é considerado congelado.
  Novas funcionalidades não serão adicionadas automaticamente.**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

Qualquer proposta de inclusão deverá apresentar uma necessidade
concreta, demonstrar impacto sobre a hipótese ou confiabilidade do
piloto e considerar explicitamente prazo, complexidade e possível
substituição ou rebaixamento de outro item.

# 18. Status da Fase 3

A Fase 3 --- Definição do MVP é considerada concluída. O SharedSpace
possui agora objetivo de MVP, hipótese de validação, priorização
funcional, limites de escopo, fluxo principal, regras específicas do
piloto e uma definição objetiva de pronto.

O projeto pode avançar para a próxima etapa sem iniciar programação
prematuramente. As decisões de UX, arquitetura, stack e implementação
deverão respeitar o escopo congelado neste checkpoint.

# 19. Próxima etapa

A próxima fase deverá transformar o escopo do MVP em uma experiência de
uso concreta antes da implementação, definindo fluxos, telas, estados,
feedbacks e interações essenciais. Em seguida, as decisões de
arquitetura e stack poderão ser tomadas com base nas necessidades reais
do produto, e não em preferências tecnológicas antecipadas.

**Base documental:** SharedSpace --- Checkpoint 02 \| Fase 2 ---
Requisitos, complementado pelas decisões de priorização tomadas durante
a Fase 3.

**SharedSpace --- Checkpoint 04**

**FASE 4 --- UX, FLUXOS E PROTOTIPAÇÃO**

*Documento oficial de consolidação e encerramento da Fase 4*

**1. Objetivo deste checkpoint**

Este checkpoint consolida as decisões tomadas durante a Fase 4 --- UX,
Fluxos e Prototipação.

O objetivo da fase foi transformar o escopo congelado na Fase 3 em uma
experiência de uso concreta, simples, previsível e coerente com o
contexto real do SharedSpace.

A fase foi conduzida sem iniciar programação. Foram definidos e
revisados:

arquitetura da informação;

fluxo do colaborador;

fluxo administrativo;

jornada principal;

telas necessárias;

estados de interface;

feedbacks;

mensagens de erro e conflito;

comportamento do controle de permanência;

comportamento quando a Copa estiver lotada;

responsividade;

abordagem mobile-first;

acessibilidade;

redução de fricção;

wireframes e prototipação no Figma.

A Fase 4 teve como foco validar como o produto deve funcionar para o
usuário, deixando decisões de arquitetura e tecnologia para as fases
seguintes.

**2. Princípio central de UX**

A pergunta central da Fase 4 foi:

"Como tornar o caminho entre descobrir a disponibilidade e utilizar a
Copa o mais simples, rápido e confiável possível?"

O SharedSpace não deve adicionar telas, informações ou interações apenas
porque elas são tecnicamente possíveis.

A experiência deve priorizar o objetivo principal do colaborador:

consultar a disponibilidade → decidir se deve ir → realizar check-in →
utilizar → realizar check-out.

A informação de ocupação deve permanecer como elemento central durante
toda a experiência.

**3. Abordagem de UX adotada**

A Fase 4 seguiu uma abordagem progressiva:

Revisão da arquitetura da informação.

Mapeamento dos fluxos principais.

Definição da jornada do colaborador.

Definição da jornada administrativa.

Identificação das telas e estados necessários.

Definição dos comportamentos de exceção.

Definição de feedbacks e mensagens.

Construção dos wireframes no Figma.

Revisão dos fluxos e estados.

Validação de responsividade e acessibilidade.

Consolidação das decisões para orientar as próximas fases.

O objetivo da prototipação não foi produzir ainda um design visual
definitivo.

O objetivo foi responder:

o que o usuário vê;

o que ele pode fazer;

o que acontece depois;

como o sistema informa o resultado;

como o sistema reage quando algo dá errado.

**4. Fluxos prioritários**

Foram definidos dois fluxos principais para o MVP.

**C01 --- Fluxo do colaborador**

O fluxo principal é:

Consulta de ocupação → Check-in → Utilização → Controle de permanência →
Check-out ou encerramento automático

Esse fluxo representa a experiência central do SharedSpace.

**C02 --- Fluxo administrativo**

O fluxo administrativo é:

Acesso protegido → Dashboard → Analytics e histórico mínimo

O administrador terá acesso às informações necessárias para acompanhar o
piloto, sem transformar a área administrativa em uma plataforma completa
de BI.

**5. C01 --- Jornada do colaborador**

A jornada do colaborador foi consolidada em oito estados principais.

**Estado 01 --- Disponível**

A Copa possui pelo menos uma vaga.

O usuário deve conseguir visualizar rapidamente:

nome do espaço;

ocupação atual;

capacidade;

quantidade de vagas livres;

indicação clara de disponibilidade;

ação de check-in quando aplicável.

Exemplo:

Copa --- 3/5 ocupada

2 vagas disponíveis

**Estado 02 --- Lotado**

A Copa atingiu sua capacidade máxima.

No piloto:

5/5 ocupada

O sistema deve informar claramente que não existem vagas disponíveis.

Como a fila prioritária permanece como SHOULD HAVE, ela não é necessária
para que o MVP seja considerado pronto.

A experiência deve orientar o usuário:

Aguarde uma vaga ser liberada. Tente novamente mais tarde.

A mensagem deve evitar ambiguidade e deixar claro que o usuário não
conseguiu realizar o check-in porque o espaço está cheio.

**Estado 03 --- Sessão ativa**

Após um check-in realizado com sucesso, o usuário passa a possuir uma
sessão ativa.

A tela deve continuar apresentando a ocupação da Copa.

A sessão ativa deve permitir que o colaborador:

saiba que está utilizando o espaço;

visualize o estado atual da ocupação;

acompanhe a referência de tempo;

realize o check-out.

Não será criada uma experiência diferente para:

usuário que permanece na aplicação;

usuário que retorna posteriormente ao SharedSpace com uma sessão ativa.

Ambos devem encontrar a mesma experiência de sessão ativa.

**Estado 04 --- Confirmação de permanência**

Após os 30 minutos definidos para o piloto, o sistema deve solicitar que
o usuário confirme se ainda está utilizando a Copa.

A confirmação deve assumir caráter prioritário na interface.

Por isso, foi definido que a confirmação será apresentada como uma
modal/overlay bloqueante, impedindo que o usuário simplesmente ignore a
mensagem enquanto continua utilizando a sessão.

O objetivo é garantir que o estado registrado pelo sistema continue
próximo da situação real do espaço.

**Estado 05 --- Renovação confirmada**

Caso o usuário confirme que ainda está utilizando a Copa:

a sessão permanece ativa;

um novo período de 30 minutos é iniciado como referência;

o usuário recebe feedback de que a permanência foi renovada.

A renovação não representa uma autorização especial ou um limite físico
de utilização.

Ela representa uma confirmação de que a sessão continua ativa.

**Estado 06 --- Encerramento automático**

Caso o usuário não responda à solicitação de permanência durante a
janela adicional de 5 minutos:

a sessão é encerrada automaticamente;

a ocupação é reduzida;

a vaga é liberada;

o histórico é registrado;

o usuário recebe feedback de encerramento automático.

Regra consolidada:

30 minutos → confirmação → 5 minutos adicionais → sem resposta →
encerramento automático

**Estado 07 --- Check-out confirmado**

Quando o usuário decide sair normalmente:

realiza o check-out;

a sessão é encerrada;

a ocupação é reduzida;

a vaga é liberada;

o usuário recebe confirmação visual.

O check-out deve ser uma ação simples e direta.

**Estado 08 --- Conflito: última vaga**

Foi identificado um cenário importante de concorrência.

Exemplo:

O usuário consulta a Copa.

O sistema informa que existe uma vaga.

Outro usuário ocupa essa última vaga antes que o primeiro conclua seu
check-in.

O primeiro usuário tenta realizar o check-in.

A Copa já está lotada.

Nesse cenário, o sistema não deve simplesmente ignorar o clique ou
apresentar um erro genérico.

A experiência deve explicar o que aconteceu.

Exemplo de comportamento:

A última vaga acabou de ser ocupada.

Em seguida:

A Copa está lotada. Aguarde uma vaga ser liberada e tente novamente mais
tarde.

A decisão adotada foi priorizar transparência sobre o conflito, sem
revelar quem ocupou a vaga.

**6. C01 --- Decisões de experiência**

**6.1 Consulta de disponibilidade**

A consulta é a principal entrada do colaborador.

O usuário não precisa realizar login para consultar a ocupação.

A informação principal deve ser imediatamente compreensível.

O colaborador deve conseguir responder rapidamente:

"Tem vaga?"

**6.2 Ocupação como informação central**

A ocupação deve continuar visível mesmo durante uma sessão ativa.

Isso mantém o usuário consciente do estado do espaço e reforça o
objetivo central do SharedSpace.

**6.3 Tempo de permanência**

O tempo apresentado ao colaborador funciona como referência, e não como
limite físico obrigatório de permanência.

Os 30 minutos servem para iniciar o processo de confirmação de
permanência.

Portanto:

30 minutos não significa que o usuário obrigatoriamente precisa sair.

Significa:

"Você ainda está utilizando a Copa?"

Caso esteja, pode confirmar a permanência.

**6.4 Confirmação de permanência**

A confirmação deve bloquear visualmente a interface subjacente porque
representa uma informação importante para a consistência da ocupação.

O usuário deverá tomar uma decisão:

continuar;

ou encerrar a utilização.

Caso confirme, a sessão continua.

Caso faça check-out, a sessão termina.

Caso ignore, inicia-se a janela adicional de 5 minutos.

**6.5 Check-out**

O check-out encerra imediatamente a sessão ativa.

Não deve existir necessidade de confirmação excessiva para uma ação
simples e recorrente.

Após o registro efetivo:

a ocupação diminui;

a vaga é liberada;

o sistema informa o sucesso.

**6.6 Encerramento automático**

O encerramento automático existe para reduzir o risco de sessões
esquecidas permanecerem ocupando uma vaga indefinidamente.

A regra do piloto é:

30 minutos → confirmação → +5 minutos → encerramento automático

A vaga é liberada somente após o encerramento efetivo da sessão.

**7. C02 --- Jornada administrativa**

A experiência administrativa foi dividida em três partes:

Acesso administrativo.

Dashboard administrativo.

Histórico mínimo de utilização.

A área administrativa possui objetivo diferente da área do colaborador.

Enquanto o colaborador precisa de velocidade e clareza, o administrador
precisa de informação agregada para acompanhar o piloto.

**8. C02 --- Acesso administrativo**

A tela de acesso administrativo foi deliberadamente mantida simples.

Elementos definidos:

campo de usuário;

campo de senha;

botão de entrada.

Não será implementado neste momento:

cadastro de administradores;

recuperação complexa de senha;

OAuth;

gerenciamento completo de contas;

sistema completo de identidade.

A proteção deverá ser suficiente para o contexto do piloto.

**9. C02 --- Dashboard administrativo**

O dashboard administrativo deve apresentar os indicadores essenciais
definidos durante a Fase 3.

Indicadores principais:

ocupação atual;

vagas disponíveis;

quantidade de utilizações/check-ins;

sessões concluídas;

tempo médio de utilização;

períodos de maior movimento.

O objetivo é permitir que a organização compreenda o comportamento da
Copa durante o piloto.

Não fazem parte do MVP:

BI avançado;

dashboards sofisticados;

dezenas de gráficos;

filtros complexos;

análises preditivas;

visualizações elaboradas.

Esses recursos permanecem como possibilidades futuras.

**10. C02 --- Histórico mínimo**

O histórico deve registrar os eventos necessários para avaliar o piloto.

A visualização deve permanecer anônima.

Informações relevantes incluem:

data;

horário;

tipo de evento;

informações necessárias para compreender a utilização do espaço.

O histórico não deve apresentar:

nome do colaborador;

e-mail;

identificação pública do ocupante.

Também não foram priorizados:

pesquisa avançada;

filtros complexos;

exportação;

BI;

relatórios sofisticados.

**11. Erros, conflitos e recuperação**

Uma das decisões importantes da Fase 4 foi diferenciar erro de conflito
de estado.

Nem todo problema precisa possuir uma tela própria.

Entretanto, quando um acontecimento puder gerar dúvida ao usuário, o
sistema deve explicá-lo adequadamente.

Princípios definidos

**11.1 Nunca apresentar falso sucesso**

Se uma operação não foi confirmada pelo sistema, ela não pode ser
apresentada como concluída.

Isso se aplica especialmente a:

check-in;

check-out;

renovação;

demais operações que alteram ocupação.

**11.2 Conflitos devem ser compreensíveis**

Quando duas ações simultâneas disputarem uma mesma vaga, o usuário deve
entender o motivo da falha.

O exemplo principal é o conflito da última vaga.

**11.3 Evitar mensagens genéricas**

Sempre que possível, a interface deve explicar o que realmente
aconteceu.

Em vez de:

"Erro."

Preferir algo equivalente a:

"A última vaga acabou de ser ocupada. A Copa está lotada."

**11.4 Repetição segura**

Repetir uma tentativa de check-in não deve criar múltiplas ocupações
para a mesma sessão.

**11.5 Falhas de conectividade**

Problemas de conectividade ou processamento deverão receber tratamento
adequado durante a implementação.

A interface não deve informar sucesso quando o resultado real da
operação for desconhecido.

**12. Comportamento quando a Copa estiver lotada**

O estado lotado é obrigatório para o MVP.

Quando a Copa estiver em:

5/5

o sistema deve comunicar claramente:

que a Copa está lotada;

que não existem vagas;

que o usuário deve aguardar uma vaga;

que pode tentar novamente mais tarde.

Mensagem conceitualmente definida:

Aguarde uma vaga ser liberada. Tente novamente mais tarde.

A fila prioritária permanece como SHOULD HAVE.

Caso seja implementada futuramente, deverá respeitar as regras já
estabelecidas na Fase 2, incluindo ordem, prioridade temporária,
expiração e prevenção de duplicidade.

**13. Controle de permanência --- UX**

O comportamento consolidado para o piloto é:

Etapa 1

O colaborador realiza check-in.

Etapa 2

A sessão permanece ativa.

Etapa 3

Após 30 minutos, o sistema solicita confirmação.

Etapa 4

O colaborador pode:

Confirmar permanência

-   → sessão continua ativa

-   → novo período de 30 minutos como referência

-   → feedback de renovação.

Realizar check-out

-   → sessão termina

-   → vaga é liberada

-   → feedback de check-out.

Não responder

-   → inicia janela adicional de 5 minutos.

Etapa 5

Após os 5 minutos adicionais sem resposta:

-   → sessão encerrada automaticamente

-   → vaga liberada

-   → feedback de encerramento automático.

**14. Sessão anônima e privacidade na experiência**

A experiência pública do SharedSpace não deve identificar nominalmente
os ocupantes.

O princípio permanece:

"SharedSpace monitora espaços, não pessoas."

A sessão anônima foi mantida como requisito funcional do MVP porque
permite:

impedir duplicidade de ocupação;

manter uma sessão ativa;

realizar check-out;

controlar permanência;

identificar tecnicamente uma sessão sem conhecer a identidade do
colaborador.

A implementação técnica dessa sessão ainda não foi definida.

Essa decisão pertence à Fase 5 --- Arquitetura.

Uma limitação aceita no MVP é que o mesmo indivíduo utilizando
navegadores ou dispositivos diferentes poderá ser percebido como sessões
diferentes.

**15. Mobile-first e responsividade**

O smartphone foi definido como principal referência de uso.

Isso ocorre porque o principal contexto de utilização envolve:

consultar a disponibilidade antes de se deslocar;

acessar o sistema rapidamente;

realizar check-in presencialmente;

realizar check-out ao sair.

A experiência desktop utilizará a mesma arquitetura de informação e os
mesmos fluxos.

A diferença será principalmente a disposição dos elementos na tela.

Não serão criadas funcionalidades diferentes apenas para desktop.

Princípio:

Uma mesma experiência, adaptada a diferentes tamanhos de tela.

**16. Acessibilidade**

A acessibilidade foi tratada como requisito da experiência e não como
uma versão separada do produto.

Diretrizes consolidadas:

estados importantes não podem depender exclusivamente de cores;

textos devem possuir contraste adequado;

botões devem possuir tamanho e organização adequados;

informações essenciais devem ser legíveis;

controles importantes devem possuir áreas adequadas para toque;

mensagens devem ser compreensíveis sem treinamento;

a implementação deverá considerar navegação por teclado;

foco deve ser tratado adequadamente;

elementos devem possuir semântica apropriada.

O objetivo é que a interface seja simples não apenas visualmente, mas
também na forma como comunica seus estados.

**17. Wireframes e prototipação**

Os wireframes foram construídos no Figma.

O objetivo da prototipação foi representar visualmente:

telas;

estados;

fluxos;

hierarquia das informações;

ações principais;

feedbacks;

situações de conflito.

Cada estado relevante foi representado como um frame/tela quando
necessário.

Isso permitiu visualizar o comportamento esperado antes da
implementação.

A prototipação interativa não foi considerada obrigatória para o
encerramento da Fase 4.

O protótipo estático foi considerado suficiente para validar:

arquitetura da informação;

fluxos;

estados;

hierarquia;

comportamento da interface.

O design visual definitivo permanece para uma etapa posterior.

**18. Inventário consolidado de telas e estados**

**C01 --- Colaborador**

**Tela/Estado 01 --- Disponível**

Apresenta:

Copa;

ocupação;

capacidade;

vagas disponíveis;

ação principal.

**Tela/Estado 02 --- Lotado**

Apresenta:

Copa 5/5;

indicação explícita de lotação;

ausência de vaga;

orientação para aguardar liberação;

orientação para tentar novamente mais tarde.

**Tela/Estado 03 --- Sessão ativa**

Apresenta:

sessão ativa;

ocupação;

referência de tempo;

ação de check-out.

**Tela/Estado 04 --- Confirmação de permanência**

Apresenta uma confirmação prioritária/bloqueante.

Objetivo:

verificar se o colaborador continua utilizando a Copa após 30 minutos.

**Tela/Estado 05 --- Renovação confirmada**

Feedback após confirmação da permanência.

**Tela/Estado 06 --- Encerramento automático**

Feedback após a sessão ser encerrada por ausência de resposta durante os
5 minutos adicionais.

**Tela/Estado 07 --- Check-out confirmado**

Feedback após o encerramento manual da sessão.

**Tela/Estado 08 --- Conflito: última vaga**

Explica que a última vaga foi ocupada antes da conclusão do check-in.

**C02 --- Administrador**

**Tela/Estado 01 --- Acesso administrativo**

usuário;

senha;

entrada.

**Tela/Estado 02 --- Dashboard administrativo**

ocupação;

vagas;

utilizações;

sessões concluídas;

tempo médio;

períodos de maior movimento.

**Tela/Estado 03 --- Histórico mínimo**

data;

horário;

tipo de evento;

informações agregadas necessárias.

**19. Estados que não exigem telas próprias**

Nem todo comportamento precisa ser representado como uma tela
permanente.

Os seguintes casos podem ser tratados por feedback contextual:

tentativa de check-in duplicada;

falha de check-in;

falha de check-out;

falha de comunicação;

operação desconhecida;

erro de processamento;

tentativa de ação incompatível com o estado atual.

A regra é:

Criar uma tela quando o estado exigir uma decisão ou compreensão
própria; utilizar feedback contextual quando uma mensagem for
suficiente.

Isso reduz complexidade sem esconder informações importantes.

**20. Relação da Fase 4 com o MVP**

As decisões de UX foram verificadas contra os critérios de "MVP pronto"
definidos na Fase 3.

A experiência definida permite:

consultar ocupação;

visualizar vagas livres;

identificar quando a Copa está lotada;

realizar check-in;

realizar check-out;

manter a sessão anônima;

controlar a permanência;

realizar renovação;

encerrar automaticamente sessões sem resposta;

apresentar feedback de sucesso;

apresentar conflitos de forma compreensível;

manter a ocupação pública anônima;

utilizar a experiência em smartphone;

adaptar a experiência para desktop;

considerar requisitos básicos de acessibilidade.

Nenhuma decisão da Fase 4 adicionou um novo MUST HAVE ao escopo
congelado.

**21. Decisões preservadas para as próximas fases**

As seguintes decisões continuam deliberadamente pendentes.

Arquitetura

estrutura interna da aplicação;

responsabilidades entre componentes;

comunicação entre frontend e backend;

persistência;

concorrência.

Sessão anônima

mecanismo de identificação da sessão;

persistência;

duração;

comportamento em diferentes dispositivos/navegadores.

Atualização da ocupação

mecanismo técnico para refletir alterações com baixo atraso;

estratégia de atualização;

comportamento diante de falhas de comunicação.

Temporizador

implementação técnica do controle de 30 + 5 minutos;

gerenciamento das sessões;

comportamento em situações de indisponibilidade.

Administração

mecanismo técnico de proteção da área administrativa.

Dados

estrutura das entidades;

relacionamento entre sessões, ocupações, eventos e espaços;

persistência do histórico.

Stack

Ainda não foram escolhidas:

tecnologia de frontend;

tecnologia de backend;

banco de dados;

infraestrutura;

serviços externos.

Essas decisões deverão ser tomadas com base nas necessidades reais
identificadas nas fases anteriores.

**22. Princípios reafirmados**

Durante a Fase 4, os seguintes princípios foram reafirmados.

**22.1 SharedSpace monitora espaços, não pessoas.**

A experiência pública não deve transformar ocupação em identificação
individual.

**22.2 A interação principal deve ser rápida.**

Consulta, check-in e check-out são ações recorrentes e devem possuir
baixa fricção.

**22.3 A ocupação deve estar sempre clara.**

O usuário não deve precisar interpretar a interface para descobrir se
existe vaga.

**22.4 Feedback faz parte da funcionalidade.**

Uma ação não está completa apenas porque o botão foi pressionado.

O usuário precisa saber o resultado.

**22.5 Conflitos devem ser explicados.**

Quando o estado mudou durante uma ação, o sistema deve explicar o
motivo.

**22.6 Boa UX é obrigatória.**

Polimento visual sofisticado não é.

**22.7 Mobile-first é a referência.**

O contexto principal do colaborador é móvel.

**22.8 Acessibilidade faz parte da implementação.**

Não haverá uma "versão acessível" separada.

**22.9 Não antecipar complexidade futura.**

Funcionalidades futuras não devem influenciar negativamente a
simplicidade do MVP.

**23. Decisões de escopo preservadas**

A Fase 4 não alterou o escopo congelado na Fase 3.

Continuam válidas:

uma organização no piloto;

uma Copa;

capacidade 5;

consulta de ocupação;

check-in manual;

check-out manual;

sessão anônima;

atualização com baixo atraso;

histórico mínimo;

proteção administrativa simples;

controle de permanência 30 + 5;

analytics administrativos básicos.

Continuam como SHOULD HAVE:

fila prioritária;

edição do espaço;

desativação/reativação.

Continuam como COULD HAVE:

QR Code;

alerta de disponibilidade;

representação visual elaborada;

dashboards sofisticados;

gráficos avançados;

animações e microinterações.

Continuam como NOT NOW:

múltiplas organizações;

multi-tenancy;

cadastro de novos espaços;

exclusão de espaços;

login individual de colaboradores;

autenticação completa;

sensores;

IoT;

identificação pública dos ocupantes.

**24. Relação com os riscos do MVP**

As decisões de UX também preservam os riscos já aceitos.

Ocupação manual

A confiabilidade continua dependendo da colaboração do usuário.

A UX reduz a fricção para aumentar a probabilidade de utilização
correta.

Esquecimento de check-out

O controle de permanência 30 + 5 reduz o impacto de sessões esquecidas.

Sessão anônima

A solução não garante reconhecimento da mesma pessoa em diferentes
navegadores ou dispositivos.

Essa limitação é aceita no MVP.

Ausência da fila

A fila prioritária permanece SHOULD HAVE.

O MVP continua válido sem ela.

Uso de outros espaços

O domínio continua genérico, mas o piloto utiliza somente a Copa.

Analytics

Os indicadores continuam deliberadamente básicos.

**25. Critérios para considerar a Fase 4 concluída**

A Fase 4 foi considerada concluída após a definição e revisão dos
seguintes pontos:

arquitetura de informação;

fluxo do colaborador;

fluxo administrativo;

jornada principal;

estados essenciais;

comportamento de lotação;

comportamento de sessão ativa;

controle de permanência;

encerramento automático;

check-out;

conflitos de concorrência;

feedbacks;

mensagens de erro;

inventário de telas;

wireframes;

responsividade;

mobile-first;

acessibilidade;

relação da experiência com os critérios de MVP.

**26. Status da Fase 4**

A Fase 4 --- UX, Fluxos e Prototipação é considerada CONCLUÍDA.

O SharedSpace possui agora uma experiência definida para o primeiro
piloto, contemplando:

fluxo principal do colaborador;

fluxo administrativo;

estados essenciais;

comportamento de ocupação;

comportamento de lotação;

sessão ativa;

controle de permanência;

renovação;

check-out;

encerramento automático;

conflitos;

feedbacks;

telas;

wireframes;

responsividade;

mobile-first;

acessibilidade.

A fase foi encerrada sem iniciar programação prematuramente.

O projeto agora possui uma base suficientemente concreta para que as
decisões técnicas sejam tomadas de forma orientada pelo produto.

**27. Próxima etapa --- Fase 5: Arquitetura**

A próxima fase será a Fase 5 --- Arquitetura.

O objetivo será transformar tudo que foi definido nas Fases 1--4 em uma
estrutura técnica coerente.

Entre as principais perguntas que deverão ser respondidas estão:

Estrutura

Como o SharedSpace será dividido internamente?

Quais serão suas principais responsabilidades?

Como frontend, backend e banco de dados se relacionarão?

Domínio

O que representa um Space?

O que representa uma sessão?

O que representa uma ocupação?

Como o histórico será registrado?

Concorrência

Como impedir que duas pessoas ocupem a última vaga simultaneamente?

Como garantir que a capacidade 5 nunca seja ultrapassada?

Sessão

Como a sessão anônima funcionará?

Como será persistida?

Como será reconhecida?

Permanência

Como o sistema controlará os 30 minutos?

Como funcionará a janela adicional de 5 minutos?

Como o encerramento automático será processado?

Atualização

Como uma mudança de ocupação será refletida para os demais usuários?

Qual nível de atraso é aceitável para o MVP?

Administração

Como a área administrativa será protegida?

Como os analytics serão obtidos a partir dos dados registrados?

**28. Princípio de transição para a Fase 5**

A principal regra para a próxima fase é:

Não escolher tecnologia primeiro e tentar encaixar o produto nela.

A arquitetura deverá responder às necessidades já identificadas.

Somente depois de compreender:

domínio;

dados;

fluxos;

concorrência;

sessões;

permanência;

atualização;

segurança;

responsabilidades;

será possível escolher conscientemente a stack de:

frontend;

backend;

banco de dados;

infraestrutura;

ferramentas de desenvolvimento.

Dessa forma, o SharedSpace continuará seguindo o princípio adotado desde
o início:

Projetar para evolução sem implementar complexidade futura antes que ela
seja necessária.

**29. Encerramento do Checkpoint 04**

Com a conclusão da Fase 4, o SharedSpace deixa de possuir apenas uma
definição funcional do MVP e passa a possuir também uma experiência de
uso concreta.

As decisões tomadas nesta fase deverão ser consideradas referência para
as próximas etapas.

A partir deste ponto:

Discovery → concluída

Requisitos → concluída

Definição do MVP → concluída

UX, Fluxos e Prototipação → concluída

Próximo checkpoint:

Fase 5 --- Arquitetura

O projeto ainda não entra em programação.

Primeiro serão definidas as estruturas técnicas necessárias para
transformar o MVP em uma aplicação implementável, mantendo o escopo
congelado e evitando decisões tecnológicas prematuras.

SharedSpace \| Checkpoint 04 --- Fase 4: UX, Fluxos e Prototipação

**SHAREDSPACE --- CHECKPOINT 05**

**FASE 5 --- ARQUITETURA E MODELAGEM TÉCNICA**

Status: CONCLUÍDA

Blocos concluídos: A01 → A13

Checkpoint da fase: A14

1\. OBJETIVO DA FASE 5

A Fase 5 teve como objetivo transformar os requisitos e decisões de
produto das fases anteriores em uma arquitetura técnica coerente,
simples, segura e suficiente para sustentar o MVP do SharedSpace.

A arquitetura foi definida sem antecipar complexidades que não fazem
parte do MVP.

2\. PRINCÍPIO ARQUITETURAL CENTRAL

"O Frontend apresenta o estado do SharedSpace. O Backend determina o
estado do SharedSpace. O Database garante a integridade dos dados que
sustentam esse estado."

Esse princípio orienta toda a arquitetura.

O Frontend não é autoridade sobre capacidade, ocupação, permanência ou
regras de negócio.

O Backend é responsável por validar e decidir as operações.

O Database garante a persistência e a integridade dos dados.

3\. ARQUITETURA GERAL

A arquitetura final é composta por:

\- Frontend

\- API REST

\- Backend

\- Database

Fluxo conceitual:

Usuário

↓

Frontend --- React + TypeScript

↓

API REST

↓

Backend --- Python + FastAPI

↓

PostgreSQL

A aplicação será um monólito modular no MVP.

Não serão utilizados microsserviços.

4\. STACK TECNOLÓGICA DEFINIDA

Frontend:

\- React

\- TypeScript

Backend:

\- Python

\- FastAPI

API:

\- REST

Database:

\- PostgreSQL

ORM:

\- SQLAlchemy

Migrations:

\- Alembic

Testes:

\- pytest

Infraestrutura:

\- Docker

Versionamento:

\- Git

\- GitHub

5\. JUSTIFICATIVA DA STACK

React + TypeScript foi escolhido para uma interface com estados claros,
comportamento dinâmico e abordagem mobile-first.

Python + FastAPI foi escolhido por sua compatibilidade com a experiência
atual de desenvolvimento em Python e por atender bem à construção de uma
API REST.

PostgreSQL foi escolhido por oferecer estrutura relacional, integridade,
transações e recursos adequados para controle de capacidade e
concorrência.

SQLAlchemy será utilizado como ORM.

Alembic será utilizado para controle de migrations.

pytest será utilizado para os testes do Backend.

Docker será utilizado para padronização do ambiente.

6\. DOMÍNIO DO SHAREDSPACE

Os principais conceitos do domínio são:

\- Space

\- Session

\- Event

\- Administrator

Conceitos futuros, mas não operacionais no MVP:

\- Organization

Analytics é tratado como uma capacidade derivada dos dados existentes, e
não como uma entidade de domínio.

Não existe uma entidade Employee/User identificada no MVP.

Princípio importante:

"Pessoa ≠ Sessão ≠ Ocupação"

A sessão representa tecnicamente um período anônimo de utilização.

7\. MODELO DE DADOS

SPACE

Campos:

\- id

\- name

\- capacity

\- status

\- created_at

\- updated_at

SESSION

Campos:

\- id

\- space_id

\- session_identifier

\- started_at

\- ended_at

\- status

\- expires_at

\- created_at

EVENT

Campos:

\- id

\- session_id

\- type

\- occurred_at

Relacionamentos:

SPACE 1:N SESSION

SESSION 1:N EVENT

Não existe identificação pessoal armazenada.

O EVENT não possui space_id próprio porque a relação pode ser obtida
através da SESSION.

8\. ESTADOS DA SESSÃO

Os estados definidos para SESSION são:

\- ACTIVE

\- CONFIRMATION_PENDING

\- COMPLETED

\- AUTO_TERMINATED

ACTIVE e CONFIRMATION_PENDING representam sessões que ocupam uma vaga.

COMPLETED e AUTO_TERMINATED não ocupam mais uma vaga.

9\. OCUPAÇÃO

A ocupação não é armazenada como um número independente.

Ela é derivada das sessões que estão ocupando uma vaga.

Ocupação:

ACTIVE + CONFIRMATION_PENDING

Não ocupam:

COMPLETED + AUTO_TERMINATED

Essa decisão evita manter duas fontes de verdade para o mesmo estado.

**10. CAPACIDADE**

A capacidade máxima da Copa no piloto é 5.

A regra fundamental é:

occupancy \<= capacity

O sistema nunca pode permitir que a ocupação ultrapasse a capacidade
configurada.

A capacidade é uma invariável do domínio.

O Frontend pode apresentar uma informação de disponibilidade, mas essa
informação pode ficar desatualizada.

O Backend sempre deve validar novamente a capacidade antes de efetivar
um check-in.

**11. CONCORRÊNCIA**

O principal problema de concorrência identificado é a disputa pela
última vaga.

Exemplo:

Dois usuários visualizam 4/5.

Ambos tentam realizar check-in.

Uma implementação ingênua poderia permitir:

5/5

e depois

6/5

Isso é proibido.

O check-in deve possuir comportamento atômico de:

"verificar capacidade + reservar/criar ocupação"

A implementação específica utilizando transação, lock, constraint ou
combinação dessas técnicas será definida durante a implementação
conforme as características do PostgreSQL.

A propriedade arquitetural já está congelada:

A capacidade jamais pode ser ultrapassada.

**12. CONFLITO DA ÚLTIMA VAGA**

Caso o Frontend apresente 4/5, mas o Backend encontre 5/5 no momento da
solicitação, a operação deve falhar de maneira explícita.

O sistema não deve apresentar um falso sucesso.

O usuário deve receber uma explicação compreensível, por exemplo:

"A última vaga acabou de ser ocupada. A Copa está lotada. Tente
novamente mais tarde. Aguarde uma vaga ser liberada."

O sistema não revela quem ocupou a vaga.

**13. SESSÃO ANÔNIMA**

O MVP não terá login de colaboradores.

Será utilizada uma sessão técnica anônima gerenciada pelo Backend,
associada a um cookie.

O identificador será:

\- aleatório

\- não significativo

\- sem dados pessoais

O Backend utiliza esse identificador para reconhecer a sessão técnica e
controlar o uso atual.

A mesma sessão técnica deve ser compartilhada entre abas do mesmo
navegador.

Outro navegador ou dispositivo pode gerar uma sessão técnica diferente.

Limitações aceitas no MVP:

\- limpar o cookie pode gerar uma nova sessão técnica;

\- outro navegador/dispositivo pode gerar outra sessão;

\- fechar o navegador não encerra automaticamente a ocupação.

Não haverá fingerprinting para tentar contornar essas limitações.

**14. SESSÃO TÉCNICA × SESSÃO DE OCUPAÇÃO**

É importante distinguir:

Sessão técnica:

\- identifica anonimamente o navegador para permitir o funcionamento do
sistema.

Sessão de ocupação:

\- representa o período em que uma vaga está sendo utilizada.

As duas coisas não são equivalentes.

**15. PERMANÊNCIA**

A regra definida para o piloto é:

30 minutos → solicitação de confirmação → janela adicional de 5 minutos
→ encerramento automático caso não haja resposta.

Fluxo:

CHECK-IN

↓

ACTIVE

↓

30 minutos

↓

CONFIRMATION_PENDING

↓

confirmação

→ ACTIVE novamente

ou

5 minutos sem resposta

→ AUTO_TERMINATED

O usuário também pode realizar CHECK-OUT a qualquer momento.

**16. CONFIRMAÇÃO DE PERMANÊNCIA**

Quando os 30 minutos forem atingidos, a sessão entra em
CONFIRMATION_PENDING.

Durante os 5 minutos adicionais:

\- a sessão continua ocupando uma vaga;

\- a ocupação continua sendo contabilizada;

\- o usuário precisa confirmar que continua utilizando o espaço.

Se confirmar:

\- a mesma SESSION continua;

\- expires_at é atualizado;

\- a sessão volta para ACTIVE;

\- um evento RENEWAL é registrado.

A renovação não cria uma nova SESSION.

**17. ENCERRAMENTO AUTOMÁTICO**

Se o usuário não responder à confirmação dentro da janela adicional de 5
minutos:

\- SESSION passa para AUTO_TERMINATED;

\- a vaga é liberada;

\- um evento AUTO_TERMINATION é registrado.

O encerramento automático é responsabilidade do Backend/processo de
execução.

O Frontend não deve ser responsável por decidir sozinho quando uma
sessão expirou.

**18. CHECK-OUT**

O usuário pode realizar check-out durante uma sessão ativa.

Após a confirmação da operação:

\- SESSION passa para COMPLETED;

\- ended_at é preenchido;

\- um evento CHECK_OUT é registrado;

\- a vaga é liberada.

Não deve haver falso sucesso.

A interface só deve apresentar sucesso depois que o Backend confirmar a
operação.

**19. AUTORIDADE TEMPORAL**

O Backend é a autoridade sobre o tempo.

O relógio do navegador é apenas uma representação visual.

O usuário não pode manipular o relógio do dispositivo para alterar a
validade da sessão.

A lógica de permanência deve utilizar o tempo determinado pelo servidor.

**20. ATUALIZAÇÃO DA OCUPAÇÃO**

Foi analisada a necessidade de manter a ocupação atualizada enquanto o
usuário observa a tela.

Alternativas avaliadas:

A. Atualização manual:

\- rejeitada para o MVP.

B. Atualização periódica:

\- escolhida.

C. WebSockets/tempo real:

\- considerada complexa demais para o MVP.

A solução definida é utilizar polling periódico.

O intervalo exato será definido e validado durante a implementação
através de testes, sem congelar arbitrariamente um número nesta fase.

O polling melhora a atualização da interface, mas não é mecanismo de
segurança.

A capacidade continua sendo validada pelo Backend.

Após uma ação realizada pelo usuário, a interface pode atualizar
imediatamente depois da confirmação do Backend.

**21. API**

A API será REST.

Endpoints conceituais definidos:

GET /spaces/{space_id}/occupancy

POST /spaces/{space_id}/sessions

GET /sessions/current

POST /sessions/{session_id}/checkout

POST /sessions/{session_id}/renew

POST /admin/login

GET /admin/analytics

GET /admin/history

O encerramento automático não será acionado pelo Frontend através de um
endpoint de usuário.

**22. API COMO CONTRATO**

A API não será apenas uma exposição direta do banco de dados.

Ela representa as operações do produto.

O Frontend não acessará o PostgreSQL diretamente.

O Backend:

\- valida requisições;

\- aplica regras;

\- controla capacidade;

\- controla sessões;

\- controla permanência;

\- registra eventos;

\- disponibiliza analytics;

\- protege a área administrativa.

**23. RESPOSTAS DA API**

A API deverá utilizar códigos HTTP adequados combinados com códigos
semânticos de erro.

Exemplos:

\- 200 --- operação realizada com sucesso

\- 201 --- recurso criado

\- 400 --- requisição inválida

\- 401 --- não autorizado

\- 409 --- conflito de estado

\- 500 --- erro interno

Exemplos de erros semânticos:

\- SPACE_FULL

\- ACTIVE_SESSION_EXISTS

A lista final de códigos será refinada durante a implementação.

**24. ÁREA ADMINISTRATIVA**

O objetivo da área administrativa no MVP é permitir validar a hipótese
do produto através dos dados de utilização.

Não é objetivo criar um sistema completo de gestão corporativa.

A área administrativa terá:

\- acesso protegido;

\- dashboard básico;

\- histórico mínimo;

\- analytics básicos.

Não terá:

\- gestão de usuários;

\- criação de espaços;

\- exclusão de espaços;

\- múltiplas organizações;

\- permissões complexas;

\- BI avançado;

\- exportações;

\- configurações complexas.

**25. DASHBOARD ADMINISTRATIVO**

O dashboard apresentará informações como:

\- ocupação atual;

\- vagas disponíveis;

\- quantidade de utilizações/check-ins;

\- sessões concluídas;

\- tempo médio de utilização;

\- período de maior utilização.

O dashboard não terá BI sofisticado no MVP.

**26. HISTÓRICO**

O histórico mínimo deve registrar:

\- timestamp;

\- tipo do evento.

Os eventos são anônimos.

Não serão registrados nomes, e-mails ou identificadores pessoais.

Não haverá no MVP:

\- filtros complexos;

\- pesquisa avançada;

\- exportação;

\- BI;

\- auditoria completa.

**27. ANALYTICS**

Analytics será uma capacidade derivada de:

\- SPACE

\- SESSION

\- EVENT

Não será criada uma entidade ANALYTICS.

Os dados devem permitir avaliar o uso do espaço e validar a hipótese do
piloto.

O sistema não deve afirmar quantidade de usuários únicos quando não
existe identificação confiável para isso.

**28. SEGURANÇA E PRIVACIDADE**

O princípio é:

"Coletar e armazenar somente o necessário para o MVP."

Não serão armazenados:

\- nome;

\- e-mail;

\- CPF;

\- matrícula;

\- cargo;

\- departamento;

\- telefone;

\- outros dados pessoais desnecessários.

O cookie anônimo terá apenas um identificador técnico aleatório.

No ambiente real será utilizado HTTPS.

O cookie deverá ser protegido com configurações adequadas, incluindo:

\- HttpOnly;

\- Secure quando houver HTTPS;

\- SameSite apropriado.

As credenciais administrativas não serão expostas no Frontend.

Senhas não serão armazenadas de forma insegura.

**29. FRONTEND NÃO CONFIÁVEL**

O Frontend é considerado não confiável para regras de negócio.

O usuário pode manipular:

\- requisições;

\- valores enviados;

\- relógio do dispositivo;

\- estado visual.

Por isso:

\- capacidade é validada no Backend;

\- permanência é controlada pelo Backend;

\- autorização administrativa é validada no Backend;

\- regras de negócio são aplicadas no Backend;

\- integridade dos dados é protegida pelo Database.

**30. LOGS**

Logs técnicos poderão existir para operação e diagnóstico.

Entretanto, não devem registrar:

\- senhas;

\- credenciais;

\- dados pessoais desnecessários;

\- informações sensíveis.

**31. ARQUITETURA MODULAR**

Embora seja um monólito, o Backend será organizado conceitualmente em
módulos:

\- Spaces

\- Sessions

\- Occupancy

\- Permanence

\- Events

\- Administration

\- Infrastructure

Analytics será tratado como uma capacidade derivada.

A estrutura interna exata de pastas, services, schemas, dependencies,
exceptions e demais componentes será definida durante a implementação.

**32. O QUE NÃO FAZ PARTE DA ARQUITETURA DO MVP**

Foram deliberadamente excluídos:

\- microsserviços;

\- Redis;

\- RabbitMQ;

\- Kafka;

\- Kubernetes;

\- GraphQL;

\- WebSockets;

\- Elasticsearch;

\- Terraform;

\- CI/CD complexo;

\- SSO;

\- MFA;

\- RBAC complexo;

\- identificação de funcionários;

\- fingerprinting;

\- biometria;

\- sensores/IoT.

Essas tecnologias podem ser consideradas futuramente apenas se houver
necessidade real.

**33. ESCALABILIDADE FUTURA**

O modelo foi construído de forma que possa suportar múltiplos espaços no
futuro.

Porém, o piloto continua limitado a:

\- 1 organização;

\- 1 espaço;

\- Copa;

\- capacidade 5.

Não foi introduzida complexidade operacional de múltiplos espaços ou
múltiplos clientes no MVP.

**34. DECISÕES ARQUITETURAIS CONGELADAS**

As seguintes decisões ficam congeladas ao final da Fase 5:

1\. Frontend + Backend + Database.

2\. Monólito modular.

3\. React + TypeScript.

4\. Python + FastAPI.

5\. REST.

6\. PostgreSQL.

7\. SQLAlchemy.

8\. Alembic.

9\. pytest.

**10. Docker.**

**11. Git/GitHub.**

**12. Backend como autoridade das regras.**

**13. Database como garantidor da integridade.**

**14. Sessão anônima por cookie técnico.**

**15. Capacidade protegida contra concorrência.**

**16. Permanência 30 + 5 minutos.**

**17. Backend como autoridade temporal.**

**18. Polling periódico para atualização da ocupação.**

**19. Área administrativa simples e protegida.**

**20. Analytics básicos.**

**21. Histórico mínimo e anônimo.**

**22. Privacidade como princípio arquitetural.**

**23. Sem identificação individual dos ocupantes.**

**35. DECISÕES DE IMPLEMENTAÇÃO AINDA ABERTAS**

A Fase 5 define a arquitetura, mas não congela detalhes de
implementação.

Ainda deverão ser definidos durante a implementação:

\- constraints específicas do PostgreSQL;

\- índices;

\- nível de isolamento;

\- mecanismo exato de transação/lock;

\- estrutura exata dos módulos;

\- services;

\- schemas;

\- dependencies;

\- exceptions;

\- mecanismo de execução do encerramento automático;

\- nome do cookie;

\- duração do cookie;

\- configuração exata de SameSite;

\- rotação do cookie, se necessária;

\- formato JSON definitivo;

\- formato final dos erros;

\- versionamento da API;

\- gerenciamento de estado no Frontend;

\- implementação das chamadas HTTP;

\- implementação do polling;

\- Docker de desenvolvimento e produção;

\- CI/CD.

**36. CRITÉRIOS DE CONCLUSÃO DA FASE 5**

A Fase 5 é considerada concluída porque:

\- a arquitetura foi definida;

\- o domínio foi modelado;

\- o modelo de dados foi definido;

\- as regras críticas foram consolidadas;

\- concorrência foi tratada conceitualmente;

\- sessão anônima foi definida;

\- permanência foi definida;

\- atualização de ocupação foi definida;

\- API foi definida conceitualmente;

\- área administrativa foi definida;

\- segurança e privacidade foram definidas;

\- stack foi escolhida;

\- arquitetura final foi consolidada.

**37. ESTADO ATUAL DO PROJETO**

Fase 1 --- Discovery:

CONCLUÍDA

Fase 2 --- Requisitos:

CONCLUÍDA

Fase 3 --- Definição do MVP:

CONCLUÍDA

Fase 4 --- UX, Fluxos e Prototipação:

CONCLUÍDA

Fase 5 --- Arquitetura e Modelagem Técnica:

CONCLUÍDA

Blocos:

A01 --- Visão arquitetural: CONCLUÍDO

A02 --- Domínio: CONCLUÍDO

A03 --- Modelagem de dados: CONCLUÍDO

A04 --- Regras de negócio: CONCLUÍDO

A05 --- Sessão anônima: CONCLUÍDO

A06 --- Capacidade e concorrência: CONCLUÍDO

A07 --- Permanência: CONCLUÍDO

A08 --- Atualização da ocupação: CONCLUÍDO

A09 --- API: CONCLUÍDO

A10 --- Administração: CONCLUÍDO

A11 --- Segurança e privacidade: CONCLUÍDO

A12 --- Escolha da stack: CONCLUÍDO

A13 --- Arquitetura final: CONCLUÍDO

A14 --- Checkpoint 05: CONCLUÍDO

**38. PRÓXIMO PASSO**

Com a Fase 5 concluída, o SharedSpace possui:

\- problema definido;

\- requisitos definidos;

\- MVP congelado;

\- UX e fluxos definidos;

\- protótipos/wireframes definidos;

\- arquitetura técnica definida;

\- domínio definido;

\- modelo de dados definido;

\- regras críticas definidas;

\- stack definida.

O próximo passo será iniciar a fase seguinte do projeto, respeitando as
decisões congeladas e evitando reabrir discussões já encerradas sem uma
necessidade real.
