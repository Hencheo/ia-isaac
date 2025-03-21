# Isaac - Assistente Virtual por Reconhecimento de Voz

Isaac é um assistente virtual desenvolvido em Python que utiliza reconhecimento de voz para interagir com o usuário. O projeto combina diversas tecnologias, incluindo reconhecimento de voz, processamento de linguagem natural e interfaces gráficas modernas.

## Principais Funcionalidades

- Reconhecimento de voz para comandos e interação natural
- Interface gráfica moderna com tema escuro e efeitos de iluminação
- Resposta a perguntas comuns e comandos diversos
- Suporte a operações do sistema como abertura de programas
- Feedback visual por meio de animações e indicadores de progresso

## Requisitos

```
PyQt5==5.15.9
pytesseract==0.3.10
Pillow==10.0.0
mss==9.0.1
SpeechRecognition==3.10.0
requests==2.31.0
gTTS==2.3.2
pygame==2.5.2
openai==1.3.5
```

## Instalação

1. Clone este repositório:
```
git clone https://github.com/Hencheo/ia-isaac.git
cd ia-isaac
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Execute o script de inicialização:
```
python iniciar_isaac.py
```

## Interface

A interface do Isaac foi completamente redesenhada com um tema escuro moderno:

- Fundo azul marinho escuro (#0A1929)
- Cards com efeito de retroiluminação azul brilhante (#2979FF)
- Efeitos visuais de brilho e iluminação
- Indicadores de progresso visual
- Transições suaves entre estados

Para mais detalhes sobre as melhorias de interface, consulte o arquivo [MELHORIAS_INTERFACE.md](MELHORIAS_INTERFACE.md).

## Arquivos Principais

- `iniciar_isaac.py`: Script principal para iniciar o assistente
- `isaac.py`: Implementação principal do assistente e interface
- `baixar_dados_tesseract.py`: Utilitário para baixar dados adicionais necessários
- `requirements.txt`: Lista de dependências do projeto

## Diretórios

- `/icons`: Ícones e recursos visuais utilizados na interface
- `/fonts`: Fontes personalizadas utilizadas na interface

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.