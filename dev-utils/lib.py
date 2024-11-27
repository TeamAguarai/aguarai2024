import subprocess
import paramiko
import os 


def establish_ssh_connection(host: str, user: str, password: str) -> paramiko.SSHClient:
    """
    Establece una conexión SSH y devuelve el cliente SSH.
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)
        return ssh
    except Exception as e:
        return None

def remove_trailing_slash(path: str) -> str:
    """Elimina barras inclinadas finales de una ruta."""
    if path.endswith(("/", "\\")):
        path = path[:-1]
    return path

def delete_remote_folder(ssh, folder_path: str) -> bool:
    """
    Elimina una carpeta remota usando una conexión SSH ya establecida.
    """
    try:
        command = f"rm -rf {folder_path}"
        stdin, stdout, stderr = ssh.exec_command(command)
        stderr_output = stderr.read().decode()
        if stderr_output:
            print(f"Error al eliminar la carpeta: {stderr_output}")
            return False
        print(f"La carpeta '{folder_path}' y su contenido fueron eliminados.")
        return True
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
        return False

def verify_and_create_remote_folder(ssh, folder_path: str) -> bool:
    """
    Verifica y crea una carpeta remota si no existe.
    """
    try:
        # Verificar si la carpeta existe
        check_command = f"[ -d {folder_path} ] && echo 'Exists' || echo 'Not exists'"
        stdin, stdout, stderr = ssh.exec_command(check_command)
        result = stdout.read().decode().strip()

        if result == "Exists":
            print(f"La carpeta '{folder_path}' ya existe.")
        else:
            print(f"La carpeta '{folder_path}' no existe. Creándola...")
            create_command = f"mkdir -p {folder_path}"
            stdin, stdout, stderr = ssh.exec_command(create_command)
            stderr_output = stderr.read().decode()
            if stderr_output:
                print(f"Error al crear la carpeta: {stderr_output}")
                return False
            print(f"Carpeta '{folder_path}' creada exitosamente.")
        return True
    except Exception as e:
        print(f"Error al verificar o crear la carpeta: {e}")
        return False

def transfer_files(ssh, local_dir: str, remote_dir: str) -> bool:
    """
    Transfiere todos los archivos de la carpeta local_dir en el equipo local
    a la carpeta remote_dir en el host remoto usando una conexión SSH existente.
    """
    try:
        sftp = ssh.open_sftp()  # Abrir el cliente SFTP
        # Recorrer todos los archivos en el directorio local
        for file_name in os.listdir(local_dir):
            local_file_path = os.path.join(local_dir, file_name)  # Ruta completa del archivo local
            remote_file_path = os.path.join(remote_dir, file_name)  # Ruta completa del archivo remoto

            # Subir cada archivo al directorio remoto
            sftp.put(local_file_path, remote_file_path)
            print(f"Transferido: {local_file_path} -> {remote_file_path}")

        sftp.close()  # Cerrar el cliente SFTP
        print("Transferencia de archivos completada.")
        return True
    except Exception as e:
        print(f"Error al transferir archivos: {e}")
        return False


def open_cmd_with_command(command: str) -> bool:
    """
    Abre un CMD local con el comando especificado.
    """
    try:
        subprocess.run(f'start cmd /k "{command}"', shell=True)
        print(f"Se abrió un CMD con el comando: {command}")
        return True
    except Exception as e:
        print(f"Error al abrir CMD: {e}")
        return False