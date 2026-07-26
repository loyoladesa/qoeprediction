import os

def delete_qoe_files(directory_path):
    if not os.path.exists(directory_path):
        print(f"O diretório '{directory_path}' não existe.")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if filename.startswith('qoe_value_'):
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"Arquivo deletado com sucesso: {filename}")
                except OSError as e:
                    print(f"Erro ao deletar {filename}: {e}")
            else:
                print(f"Ignorado: '{filename}' é um diretório, não um arquivo.")

if __name__ == '__main__':
    diretory = os.getcwd()
    print(f'Directory {diretory} found.')
    target_dir = diretory
    delete_qoe_files(target_dir)