# o que iremos precisar:

# botao para entrar no chat
# quando entrar no chat: (aparece para todos)
    # a msg que voce entrou no chat
    # o campo e o botão de enviar msg
# a cada msg que vc envia: (aparece para todos)
    # Nome: Texto da Mensagem 
    
import flet as ft

# criar uma função que gerencia o site
def main(pagina):
    texto = ft.Text("Messenger")
    pagina.add(texto)
    
    nome_usuario = ft.TextField(label="Escreva seu NOME:")
    chat = ft.Column()
    
    def enviar_msg_tunel(mensagem):
        tipo = mensagem["tipo"]
        
        if tipo == "mensagem":
            texto_msg = mensagem['texto']
            usuario_msg = mensagem['usuario']
            # adicionar a msg no chat
            chat.controls.append(ft.Text(f"{usuario_msg}: {texto_msg}"))
        else: 
            usuario_msg = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_msg} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.LIGHT_BLUE_500))
        pagina.update()
        
    # PUBSUB - publish e subscribe, cria um tunel de comunicação entre os usuarios
    
    pagina.pubsub.subscribe(enviar_msg_tunel)        
    
    def enviar_msg(event):
        pagina.pubsub.send_all({"texto": campo_msg.value, "usuario":nome_usuario.value, "tipo": 'mensagem'})
        # colocamos pra ele enviar um dicionario pois o send_all só consegue enviar uma coisa
        # limpar o campo de msg
        campo_msg.value = ""
        pagina.update()
    
    campo_msg = ft.TextField(label="Digite uma mensagem!", on_submit=enviar_msg)
    botao_enviar = ft.ElevatedButton("Enviar Menssagem", on_click=enviar_msg)
    
    def entrar_popup(event):
        # mostrar a msg que a pessoa entrou no chat
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": 'entrada'})
        # adcicionar o chat
        pagina.add(chat)    
        # fechar o popop
        popup.open = False
        pagina.update()
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        # criar o campo de mensagem do usuario
        # criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_msg, botao_enviar]
        ))
        
    
    popup = ft.AlertDialog(
        open = False, modal=True,
        title = ft.Text("Bem Vindo ao nosso Messenger!!"),
        content = nome_usuario,
        actions = [ft.ElevatedButton("Entrar", on_click=entrar_popup)]
    )
    
    def entrar_chat(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    # dentro do botão, passamos o texto que vai ficar no botão e a funcao que vai se chamada, apos o usuario clicar.
    botao_iniciar = ft.TextButton("Iniciar Chat", on_click=entrar_chat)
    pagina.add(botao_iniciar)

ft.app(target=main)