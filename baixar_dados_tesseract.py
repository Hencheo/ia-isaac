import os
import requests
import shutil

def baixar_dados_tesseract():
    # Diretório de destino
    tessdata_dir = r"C:\Program Files\Tesseract-OCR\tessdata"
    
    # Verificar se o diretório existe
    if not os.path.exists(tessdata_dir):
        print(f"Criando diretório: {tessdata_dir}")
        os.makedirs(tessdata_dir, exist_ok=True)
    
    # URL do arquivo de dados do português
    por_url = "https://github.com/tesseract-ocr/tessdata/raw/main/por.traineddata"
    
    # Caminho de destino
    por_path = os.path.join(tessdata_dir, "por.traineddata")
    
    # Verificar se o arquivo já existe
    if os.path.exists(por_path):
        print("Arquivo de dados do português já existe.")
        return
    
    print(f"Baixando arquivo de dados do português para Tesseract OCR...")
    
    try:
        # Baixar o arquivo
        response = requests.get(por_url, stream=True)
        response.raise_for_status()
        
        # Salvar o arquivo
        with open(por_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
            
        print(f"Arquivo baixado com sucesso para: {por_path}")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {str(e)}")

if __name__ == "__main__":
    baixar_dados_tesseract()