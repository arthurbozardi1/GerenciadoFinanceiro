# Processo de Desenvolvimento

## Estrutura de Branches
- **Main**: Contém o código de produção, estável e pronto para lançamento.
- **Develop**: Branch principal para desenvolvimento contínuo. Todas as novas funcionalidades e correções são integradas aqui antes de serem preparadas para lançamento.
- **Feature/Fix**: Criado a partir do branch **develop** para desenvolver novas funcionalidades ou corrigir bugs. Após a conclusão, é mesclado de volta no **develop**.
- **Hotfix**: Criado a partir do **main** para correções urgentes em produção. Após corrigido, é mesclado no **main** e no **develop**.
- **Release**: Criado a partir do **develop** quando uma versão está pronta para ser lançada. Permite ajustes finais e testes de qualidade. Ao concluir, é mesclado no **main** e no **develop**, e uma **tag de versão** é criada.

## Fluxo de Trabalho

1. O **Product Owner (PO)** prioriza o backlog, com base nas necessidades do negócio e feedbacks de usuários.
2. Os **Developers** criam **branches de feature/fix** a partir do **develop**, onde implementam novas funcionalidades ou corrigem bugs.
3. O **Tech Leader** realiza revisões de código e aprova **pull requests** antes da integração no **develop**.
4. Ao finalizar um conjunto de funcionalidades, um **branch de release** é criado a partir do **develop**.
5. O **Quality Assurance (QA)** testa o código no **branch de release**.
6. Após a aprovação, o **branch de release** é mesclado no **main**, e uma nova **tag de versão** é criada para marcar o lançamento.
7. Em casos de emergência, cria-se um **branch de hotfix** diretamente do **main**, sendo integrado posteriormente ao **develop** para que a correção reflita em versões futuras.

## Papéis e Responsabilidades

### Product Owner (PO)
- Prioriza as funcionalidades e correções com base nas necessidades do negócio.
- Mantém o backlog atualizado e orienta a equipe sobre as prioridades.
- Valida as funcionalidades durante as releases.

### Tech Leader (TL)
- Garante a qualidade do código e orienta os **developers**.
- Define a arquitetura e revisa **pull requests**.
- Supervisiona a criação de **branches de release** e a mesclagem no **main**.

### Desenvolvedor (Developer)
- Implementa funcionalidades e corrige bugs, criando **branches de feature/fix** ou **hotfix**.
- Realiza testes unitários e submete o código para revisão.
- Mescla o código no **develop** e participa dos testes de release.

### Quality Assurance (QA)
- Testa as funcionalidades nas **branches de release**.
- Identifica e relata bugs, garantindo a estabilidade do código antes do lançamento.

### Scrum Master / Project Manager
- Organiza a equipe e facilita as cerimônias ágeis.
- Atua como facilitador entre o **PO**, o time de desenvolvimento e as partes interessadas.

---


# Descrição do Projeto

Software amador desenvolvido em Python com o intuito de auxiliar como gestor financeiro. Pode ser utilizado em pequenas empresas ou para uso pessoal. O programa lê os dados e responde com uma opinião geral entre faturas e despesas, por meio de gráficos, planilhas CSV e informações gerais. Ele utiliza as bibliotecas matplotlib, pandas e time.

Para rodar o código é necessário instalar as seguintes bibliotecas e executar o arquivo main.py 

## Bibliotecas do Python necessárias

```bash
pip install pandas
pip install matplotlib
```

## Regras para Criação de Branches, Tags e Disponibilização para o Cliente

- **Versões** entregues aos clientes serão disponibilizadas uma vez por semana.
- Toda nova versão deve ser criada em uma **branch de release** e receber uma **tag de versão** no Git.
- Se necessário um hotfix, deve-se criar uma branch no formato: **hotfix/nome-da-alteração**, e uma nova versão será lançada, atualizando apenas o patch da tag.

## Tickets

### #1234
- **Nome da branch**: `fix/1234-atualizacao_readme`
- **Descrição**: Atualizar o readme.md do projeto.

### #4345
- **Nome da branch**: `feature/4345-informacoes_main`
- **Descrição**: Dar mais informações no arquivo main ao rodar o código, indicando que para parar a execução é necessário inserir `-1`.

### #2356
- **Nome da branch**: `fix/2356-renomear_arquivos`
- **Descrição**: Alterar o nome dos arquivos `exec_integrado` e `main`.

---

**(Branches e alterações fictícias)**

### #3243
- **Nome da branch**: `feature/3243-branch4` (Solicitação de Review)
- **Descrição**: Primis efficitur tincidunt primis rhoncus taciti. Adipiscing conubia condimentum nullam felis per nisl diam faucibus.

### #6757
- **Nome da branch**: `fix/6757-branch5`
- **Descrição**: Dis nascetur egestas posuere condimentum ut ipsum platea sociosqu. Cursus vestibulum blandit ridiculus montes potenti sed ac.

### hotfix/correcao_necessaria
- **Descrição**: Branch para correção emergencial.
