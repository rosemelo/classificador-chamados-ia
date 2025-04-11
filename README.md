# 🤖 Central de Chamados com IA

Este é um projeto simples e divertido usando **Python**, **IA** e **Streamlit** para classificar mensagens de clientes e responder de forma descontraída 😄.

---

## ✨ O que o projeto faz?

- Usa um modelo de IA para **classificar automaticamente os chamados** recebidos.
- Categoriza em: `pedido`, `valores`, `transacao` ou `outros`.
- Gera uma **resposta automática com bom humor**, dependendo da categoria.

---

## 🚀 Como usar

1. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

2. Treine o modelo (se ainda não estiver treinado):

    ```bash
    python train.py
    ```

3. Execute o aplicativo:

    ```bash
    streamlit run app.py
    ```

4. Acesse o aplicativo no navegador pelo endereço exibido no terminal (ex: http://localhost:8501)

---

## 🗂 Estrutura do Projeto

```
chamados-ia/
├── app.py                   ← Interface com o usuário (Streamlit)
├── classify.py             ← Funções para pré-processamento e classificação
├── respostas.py            ← Geração de respostas divertidas 😄
├── train.py                ← Script para treinar o modelo
├── data/
│   └── chamados.csv        ← Base de dados com chamados de exemplo
├── model/
│   └── classificador.pkl   ← Modelo treinado salvo aqui
├── requirements.txt        ← Lista de dependências
└── README.md               ← Este arquivo
```

---

## 📁 Exemplo de dados (`chamados.csv`)

O arquivo CSV precisa estar na pasta `data/` com o nome `chamados.csv`. Ele deve conter duas colunas:

```csv
texto,categoria
Meu pedido ainda não chegou,pedido
Foi cobrado o valor errado,valores
O pagamento não caiu ainda,transacao
Preciso de ajuda com o aplicativo,outros
```

⚠️ Caso o CSV esteja no `.gitignore`, coloque um exemplo como esse no README para quem quiser clonar o projeto.

---

## 🔁 Como melhorar o modelo

Você pode melhorar a IA adicionando novos exemplos ao `chamados.csv`. Depois disso, basta reexecutar o treinamento com:

```bash
python train.py
```

O modelo será atualizado automaticamente.

---

## 🌐 Quer publicar?

1. Suba seu projeto no GitHub.
2. Crie uma conta no [Streamlit Cloud](https://streamlit.io/cloud).
3. Conecte com seu repositório e publique com um clique! 🔗

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 🙌

---

## 🧠 Quer aprender mais?

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Curso de IA com Python (freeCodeCamp)](https://www.youtube.com/watch?v=aircAruvnKk)
- [Bootcamps e Labs da DIO](https://www.dio.me)
- [Cursos gratuitos no Coursera e edX](https://www.coursera.org/)
- [Alura](https://www.alura.com.br) também tem ótimos cursos de IA, Python e Data Science.

---

## 🪪 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👩‍💻 Desenvolvido por

Feito com 💜 por [Rose Melo](https://github.com/rosemelo)  