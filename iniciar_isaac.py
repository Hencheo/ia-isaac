import os
import sys
import subprocess
import webbrowser

def verificar_dependencias():
    """Verifica se todas as dependências estão instaladas"""
    try:
        import PyQt5
        import pytesseract
        import PIL
        import mss
        import speech_recognition
        import requests
        import gtts
        import pygame
        print("✅ Todas as dependências Python estão instaladas.")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {str(e)}")
        return False

def verificar_tesseract():
    """Verifica se o Tesseract-OCR está instalado e configurado"""
    try:
        import pytesseract
        texto = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract-OCR encontrado (versão {texto})")
        return True
    except Exception as e:
        print(f"❌ Tesseract-OCR não encontrado ou não configurado corretamente: {str(e)}")
        print("Por favor, instale o Tesseract-OCR e configure o caminho corretamente em isaac.py")
        return False

def instalar_dependencias():
    """Instala as dependências do projeto"""
    print("📦 Instalando dependências...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências.")
        return False

def criar_diretorios():
    """Cria os diretórios necessários se não existirem"""
    diretorios = ["fonts", "icons"]
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"📁 Diretório {diretorio} criado.")

def iniciar_isaac():
    """Inicia o Isaac"""
    print("🚀 Iniciando Isaac...")
    try:
        subprocess.run([sys.executable, "isaac.py"])
    except Exception as e:
        print(f"❌ Erro ao iniciar o Isaac: {str(e)}")

def menu_principal():
    """Exibe o menu principal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("🤖 ISAAC - Assistente de IA com Interface Moderna")
    print("=" * 50)
    print("\nEscolha uma opção:")
    print("1. Iniciar Isaac")
    print("2. Verificar dependências")
    print("3. Instalar/atualizar dependências")
    print("4. Abrir documentação")
    print("0. Sair")
    
    opcao = input("\nOpção: ")
    
    if opcao == "1":
        iniciar_isaac()
    elif opcao == "2":
        verificar_dependencias()
        verificar_tesseract()
        input("\nPressione Enter para continuar...")
        menu_principal()
    elif opcao == "3":
        instalar_dependencias()
        criar_diretorios()
        input("\nPressione Enter para continuar...")
        menu_principal()
    elif opcao == "4":
        # Abrir o README.md se existir ou tentar abrir página online
        if os.path.exists("README.md"):
            with open("README.md", "r", encoding="utf-8") as f:
                conteudo = f.read()
                print("\n" + conteudo)
        else:
            print("Abrindo documentação online...")
            webbrowser.open("https://github.com/Hencheo/ia-isaac")
        input("\nPressione Enter para continuar...")
        menu_principal()
    elif opcao == "0":
        print("👋 Até a próxima!")
        sys.exit(0)
    else:
        print("❌ Opção inválida!")
        input("\nPressione Enter para continuar...")
        menu_principal()

if __name__ == "__main__":
    criar_diretorios()
    menu_principal()