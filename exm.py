

entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)