# import os
# import time
# import alive_progress

# comandStart = '/start'
# plan1 = "openApp"
# plan2 = "SystemCrush"

# def openApp():
#     while True:
#         app_name = input("Введите название программы (например, chrome): ")

#         try:
#             start_time = time.time()
#             result = os.system(f'start {app_name}')
#             end_time = time.time()

#             elapsed_time = end_time - start_time
#             if result == 0:
#                 print(f"Программа {app_name} успешно запущена за {elapsed_time:.2f} секунд(ы)!")
#             else:
#                 print(f"Не удалось запустить программу {app_name}. Проверьте название.")
#         except Exception as e:
#             print(f"Произошла ошибка при запуске программы {app_name}: {e}")

#         q = input("Попробовать ещё раз? [yes/no]: ").lower()
#         if q not in ['yes', 'да']:
#             print("Завершение работы с этим планом.")
#             break

# def SystemCrush(file_name, size_in_gb):
#     size_in_bytes = size_in_gb * 1024**3  # Convert GB to bytes
#     chunk_size = 1024 * 1024  # Size of each block (1 MB)
#     written_bytes = 0

#     desktop_path = r"C:\Users\morgu\OneDrive\Рабочий стол\TEST"
    
#     # Full file path
#     file_path = os.path.join(desktop_path, file_name)

#     try:
#         with open(file_path, 'wb') as f:
#             while written_bytes < size_in_bytes:
#                 remaining_bytes = size_in_bytes - written_bytes
#                 write_size = min(chunk_size, remaining_bytes)
#                 f.write(b'\0' * write_size)
#                 written_bytes += write_size
#                 print(f"Progress: {written_bytes / size_in_bytes * 100:.2f}%")
#     except PermissionError:
#         print("Error: Permission denied. Check if the file is already open or if you have write permissions.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def SelectPlan():
#     w = input("Welcome to システムカミカゼ. This program can execute specific actions on your PC. To start, type '/start': ")
#     if w == comandStart:
#         print("Available plans:")
#         print("1. OpenApp")
#         print("2. SystemCrush")
        
#         selected_plan = input("Enter the number of the plan you want to execute: ")

#         if selected_plan == "1":
#             openApp()
#         elif selected_plan == "2":
#             # You need to pass the filename and size for the SystemCrush plan
#             file_name = input("Enter the name of the file to create: ")
#             try:
#                 size_in_gb = int(input("Enter the size of the file in GB: "))
#                 if size_in_gb > 0:
#                     SystemCrush(file_name, size_in_gb)
#                 else:
#                     print("Error: The size must be a positive number.")
#             except ValueError:
#                 print("Invalid input for size. Please enter a valid integer.")
#         else:
#             print("Invalid selection. Please choose 1 or 2.")

# # Start the program
# SelectPlan()



import os
import time
import alive_progress

comandStart = '/start'
plan1 = "openApp"
plan2 = "SystemCrush"

def openApp():
    while True:
        app_name = input("Введите название программы (например, chrome): ")

        try:
            start_time = time.time()
            result = os.system(f'start {app_name}')
            end_time = time.time()

            elapsed_time = end_time - start_time
            if result == 0:
                print(f"Программа {app_name} успешно запущена за {elapsed_time:.2f} секунд(ы)!")  
            else:
                print(f"Не удалось запустить программу {app_name}. Проверьте название.")
        except Exception as e:
            print(f"Произошла ошибка при запуске программы {app_name}: {e}")

        q = input("Попробовать ещё раз? [yes/no]: ").lower()
        if q not in ['yes', 'да']:
            print("Завершение работы с этим планом.")
            break

def SystemCrush(file_name, size_in_gb):
    size_in_bytes = size_in_gb * 1024**3  # Convert GB to bytes
    chunk_size = 1024 * 1024  # Size of each block (1 MB)
    written_bytes = 0

    desktop_path = r"C:\Users\morgu\OneDrive\Рабочий стол\TEST"
    
    # Full file path
    file_path = os.path.join(desktop_path, file_name)

    try:
        with open(file_path, 'wb') as f:
            # Initialize the progress bar
            with alive_progress.alive_bar(size_in_bytes // chunk_size, title="Writing file") as bar:
                while written_bytes < size_in_bytes:
                    remaining_bytes = size_in_bytes - written_bytes
                    write_size = min(chunk_size, remaining_bytes)
                    f.write(b'\0' * write_size)
                    written_bytes += write_size
                    bar()  # Update the progress bar
    except PermissionError:
        print("Error: Permission denied. Check if the file is already open or if you have write permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

def SelectPlan():
    w = input("Welcome to システムカミカゼ. This program can execute specific actions on your PC. To start, type '/start': ")
    if w == comandStart:
        print("Available plans:")
        print("1. OpenApp")
        print("2. SystemCrush")
        
        selected_plan = input("Enter the number of the plan you want to execute: ")

        if selected_plan == "1":
            openApp()
        elif selected_plan == "2":
            # You need to pass the filename and size for the SystemCrush plan
            file_name = input("Enter the name of the file to create: ")
            try:
                size_in_gb = int(input("Enter the size of the file in GB: "))
                if size_in_gb > 0:
                    SystemCrush(file_name, size_in_gb)
                else:
                    print("Error: The size must be a positive number.")
            except ValueError:
                print("Invalid input for size. Please enter a valid integer.")
        else:
            print("Invalid selection. Please choose 1 or 2.")

# Start the program
SelectPlan()
