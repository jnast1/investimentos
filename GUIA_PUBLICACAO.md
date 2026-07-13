# Guia: publicar o Dashboard no GitHub Pages

Tempo estimado: 10 minutos. Custo: zero. Resultado: um link permanente
(ex.: `https://seuusuario.github.io/investimentos/`) que abre de qualquer
computador ou celular, com as APIs funcionando sem bloqueio.

---

## Por que isso resolve os problemas de conexão

Quando a página roda num domínio de verdade (github.io) em vez de um
arquivo local (file:///), o navegador envia uma origem válida nas
requisições. O firewall do Banco Central, que recusava a origem nula do
arquivo local, passa a responder normalmente, e as extensões de
bloqueio param de interferir. INCC, CDI, IPCA e Selic voltam a ser 100%
automáticos.

## Sobre privacidade (importante)

O GitHub Pages gratuito publica a página num endereço público. Por isso
o arquivo `index.html` desta pasta é uma **versão limpa**: as carteiras
começam vazias e os parâmetros do imóvel são genéricos de exemplo.

Na primeira vez que você abrir o seu link, cadastre suas ações, FIIs,
fundos e os parâmetros do imóvel, e clique em Aplicar. **Tudo fica salvo
apenas no seu navegador** (localStorage), nunca no site. Quem abrir o
mesmo link em outro computador verá o painel vazio. Repita o cadastro
uma vez em cada dispositivo que usar (computador do trabalho, celular),
ou me peça que eu crie botões de exportar/importar configuração.

---

## Passo a passo

### 1. Criar a conta (se ainda não tiver)
1. Acesse **github.com** e clique em **Sign up**
2. Informe e-mail, senha e um nome de usuário (ele fará parte do seu
   link, ex.: `joaonast`)
3. Confirme o código enviado por e-mail

### 2. Criar o repositório
1. Logado, clique no **+** no canto superior direito e em **New repository**
2. Em **Repository name**, digite: `investimentos`
3. Marque **Public** (necessário para o Pages gratuito)
4. Não marque nenhuma outra opção
5. Clique em **Create repository**

### 3. Enviar o arquivo
1. Na página do repositório recém-criado, clique no link
   **uploading an existing file** (aparece no meio da tela)
2. Arraste o arquivo **index.html** desta pasta para a área de upload
   (o nome precisa ser exatamente `index.html`)
3. Clique no botão verde **Commit changes**

### 4. Ativar o GitHub Pages
1. No repositório, clique em **Settings** (aba superior, ícone de engrenagem)
2. No menu lateral esquerdo, clique em **Pages**
3. Em **Source**, deixe **Deploy from a branch**
4. Em **Branch**, selecione **main** e a pasta **/ (root)**
5. Clique em **Save**

### 5. Acessar
1. Aguarde 1 a 2 minutos
2. Recarregue a página de Settings → Pages: aparecerá a mensagem
   **"Your site is live at https://SEUUSUARIO.github.io/investimentos/"**
3. Abra o link. Os selos devem ficar verdes, incluindo o Banco Central,
   e o INCC-M deve carregar sozinho

### 6. Configurar (uma única vez por dispositivo)
1. Aba **⚙ Configuração**: cole o token da brapi e salve
2. Preencha os parâmetros do imóvel (valor de tabela 896.000, entrada,
   parcelas etc.) e clique em **Aplicar e salvar**
3. Abas **FIIs** e **Ações**: cadastre suas posições e clique em
   **Aplicar carteira**
4. Salve o link nos favoritos e, no celular, use "Adicionar à tela
   inicial" para ter um ícone de aplicativo

---

## Como atualizar o dashboard no futuro

Quando eu gerar uma versão nova do arquivo:
1. Abra o repositório no GitHub e clique em **index.html**
2. Clique no ícone de **lápis** (Edit) → apague tudo → cole o conteúdo
   novo → **Commit changes**
   (ou delete o arquivo e faça upload do novo)
3. O site atualiza sozinho em 1-2 minutos. Suas configurações não se
   perdem, pois ficam no navegador, não no arquivo.

## Se algo der errado

- **404 ao abrir o link**: aguarde mais 2 minutos ou confira se o
  arquivo se chama exatamente `index.html` (minúsculo)
- **Selo do BCB ainda vermelho**: improvável no Pages, mas se ocorrer,
  o painel continua operando com dados de fábrica + manual, como hoje
- **Quer tirar o site do ar**: Settings → Pages → Source → None, ou
  delete o repositório em Settings → Danger Zone
