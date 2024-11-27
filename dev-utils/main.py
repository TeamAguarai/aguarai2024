import lib

# CONTRASEÑA INNECESARIA!! con ssh-keygen

PI_HOST = "pi.local"    
PI_USER = "pi"     
PI_PWD = "1234"            
PI_DIR = "~/proyecto/"          
LOCAL_DEV_DIR = "./dev/"               
COMPILER = "g++"              
EXECUTABLE = "programa"        
LINKER_FLAGS = "-lwiringPi"    

PI_DIR = lib.remove_trailing_slash(PI_DIR)

def transfer_dev_files(ssh, local_dir_path, remote_dir_path):
    print(f'\nLos archivos de "{LOCAL_DEV_DIR}" se enviaran a la "{PI_HOST}@{PI_USER}:{PI_DIR}". Si la carpeta no existe sera creada')
    lib.verify_and_create_remote_folder(ssh, remote_dir_path)
    lib.transfer_files(ssh, local_dir_path, remote_dir_path)    

def start_terminal():
    connect_ssh_command = f"ssh -t {PI_USER}@{PI_HOST}"
    lib.open_cmd_with_command(f'{connect_ssh_command} "cd {PI_DIR}; bash"')    


if __name__ == "__main__":
    print("Conectando...")
    ssh = None
    while ssh == None:
        ssh = lib.establish_ssh_connection(PI_HOST, PI_USER, PI_PWD)
        if ssh == None: print("Conexion fallida. Reintentando...")

    print("Conexion establecida.")
    clean_first = input("\nDesar limpiar el proyecto? (Esto es para evitar tener archivos basura al campilar) [s/n]: ")
    if clean_first.lower() == "s":
        lib.delete_remote_folder(ssh, PI_DIR)

    transfer_dev_files(ssh, LOCAL_DEV_DIR,PI_DIR)
    ssh.close()

    start_terminal()
    