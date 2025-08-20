# Sistema de Pagamento PIX

Um sistema de pagamento PIX desenvolvido em Flask que permite criar pagamentos, gerar QR codes e gerenciar transações de forma simples e eficiente.

## 🚀 Funcionalidades

- **Criação de Pagamentos PIX**: Gera pagamentos com valores personalizados
- **QR Code Automático**: Cria QR codes únicos para cada transação
- **Interface Web**: Página de pagamento responsiva e moderna
- **Banco de Dados**: Armazenamento persistente de transações
- **Expiração Automática**: Pagamentos expiram em 30 minutos
- **API RESTful**: Endpoints para integração com outros sistemas

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask 2.3.0
- **Banco de Dados**: SQLite com SQLAlchemy
- **Geração de QR Code**: qrcode 7.4.2
- **Processamento de Imagens**: Pillow 10.2.0
- **WebSockets**: Flask-SocketIO 5.3.6
- **Frontend**: HTML5, CSS3, JavaScript

## 📁 Estrutura do Projeto

```
Pagamento/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── .gitignore            # Arquivos ignorados pelo Git
├── instance/             # Banco de dados SQLite
├── static/               # Arquivos estáticos
│   ├── img/             # QR codes gerados
│   ├── css/             # Estilos CSS
│   └── template_img/    # Imagens do template
├── templates/            # Templates HTML
│   ├── payment.html     # Página de pagamento
│   ├── 404.html         # Página de erro
│   └── confirmed_payment.html
├── src/                  # Código fonte
│   ├── models/          # Modelos de dados
│   │   └── payment.py   # Modelo de pagamento
│   ├── payments/        # Lógica de pagamento
│   │   └── pix.py       # Implementação PIX
│   └── repository/      # Camada de dados
│       └── database.py  # Configuração do banco
└── venv/                # Ambiente virtual Python
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd Pagamento
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   ```bash
   # No Windows
   venv\Scripts\activate
   
   # No macOS/Linux
   source venv/bin/activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação**
   ```bash
   python app.py
   ```

6. **Acesse a aplicação**
   ```
   http://127.0.0.1:5000
   ```

## 📡 API Endpoints

### 1. Criar Pagamento PIX
```http
POST /payments/pix
Content-Type: application/json

{
  "value": 100.50
}
```

**Resposta:**
```json
{
  "status": "success",
  "message": "Pix payment created successfully",
  "payment": {
    "id": 1,
    "value": 100.50,
    "paid": false,
    "bank_payment_id": "uuid-gerado",
    "qrcode": "qrcode_uuid-gerado",
    "expires_at": "2024-01-01T12:30:00"
  }
}
```

### 2. Visualizar Pagamento
```http
GET /payments/pix/{payment_id}
```

Retorna uma página HTML com o QR code e informações do pagamento.

### 3. Obter QR Code
```http
GET /payments/pix/qrcode/{file_name}
```

Retorna a imagem do QR code em formato PNG.

### 4. Confirmar Pagamento
```http
POST /payments/pix/confirmation
```

Endpoint para confirmação de pagamento (implementação futura).

## 🗄️ Modelo de Dados

### Payment
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | ID único do pagamento |
| value | Float | Valor do pagamento |
| paid | Boolean | Status do pagamento |
| bank_payment_id | String | ID do pagamento no banco |
| qrcode | String | Nome do arquivo do QR code |
| expires_at | DateTime | Data/hora de expiração |

## 🎨 Interface

O sistema possui uma interface web moderna e responsiva que inclui:

- **Página de Pagamento**: Exibe o QR code e informações da transação
- **Design Responsivo**: Adaptável a diferentes tamanhos de tela
- **Elementos Visuais**: Ícones e indicadores visuais
- **Informações Claras**: Valor, tempo de expiração e número do pedido

## 🔧 Configuração

### Variáveis de Ambiente
- `SECRET_KEY`: Chave secreta do Flask (padrão: 'secret123')
- `SQLALCHEMY_DATABASE_URI`: URI do banco de dados (padrão: SQLite local)

### Personalização
- **Tempo de Expiração**: Modifique o valor em `timedelta(minutes=30)` no arquivo `app.py`
- **Estilos**: Edite os arquivos CSS em `static/css/`
- **Templates**: Modifique os arquivos HTML em `templates/`

## 🚨 Limitações Atuais

- **Simulação**: O sistema simula pagamentos PIX (não integra com bancos reais)
- **Autenticação**: Não possui sistema de autenticação
- **Validações**: Validações básicas implementadas
- **Confirmação**: Endpoint de confirmação não implementado

## 🔮 Próximos Passos

- [ ] Integração com APIs bancárias reais
- [ ] Sistema de autenticação e autorização
- [ ] Webhooks para confirmação automática
- [ ] Dashboard administrativo
- [ ] Relatórios e analytics
- [ ] Testes automatizados
- [ ] Documentação da API com Swagger

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto de estudo para implementação de sistemas de pagamento PIX.

---

**Nota**: Este é um projeto educacional e não deve ser usado em produção sem as devidas adaptações e integrações com sistemas bancários reais.
