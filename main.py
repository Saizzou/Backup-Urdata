from PySide6.QtWidgets import QWidget, QFileDialog
from design.design import *
from src import backup
from datetime import datetime
import sys, threading, time


app = QApplication(sys.argv)
mainWindow = QWidget()
main_ui = Ui_MainWindow()
main_ui.setupUi(mainWindow)


backup_thread = None
stop_event = threading.Event()

# CODE CODE CODE #
def select_directory():
    file_dialog = QFileDialog()
    file_dialog.setWindowTitle("Choose a Directory.")
    file_dialog.setFileMode(QFileDialog.Directory)

    if file_dialog.exec():
        file_path = file_dialog.selectedFiles()
        file_path = ', '.join(map(str, file_path))
        return file_path


def insert_directory_from():
    directory_path = select_directory()
    main_ui.line_from.setText(directory_path)
    main_ui.text_Status.appendPlainText("The Folder to be backuped is selected. \n")
    main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)


def insert_directory_to():
    directory_path = select_directory()
    main_ui.line_to.setText(directory_path)
    main_ui.text_Status.appendPlainText("The Storage Folder for the Backup is selected. \n")
    main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)


def insert_directory_toList():
    item = main_ui.line_from.text()
    main_ui.cb_Items.addItems([item])
    counter = main_ui.cb_Items.count()
    main_ui.lbl_counter.setText(f"{str(counter)} Directories selected")
    main_ui.text_Status.appendPlainText(f"Added : '{main_ui.line_from.text()}' to the Backup List.")


def delete_directory_fromList():
    item = main_ui.cb_Items.currentIndex()
    main_ui.cb_Items.removeItem(item)
    counter = main_ui.cb_Items.count()
    main_ui.lbl_counter.setText(f"{str(counter)} Directories selected")


def run_backup_loop(source_folders, dest_folder, interval_hours):
    while not stop_event.is_set():
        for i, j in enumerate(source_folders):
            backup.create_backup(j,dest_folder)
            main_ui.text_Status.appendPlainText(f"{i + 1}: Backup for {j} completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)

        for _ in range(int(interval_hours) * 60):  # convert hours to seconds
            if stop_event.is_set():
                break
            time.sleep(1)


def start_backup():
    global backup_thread
    
    source_folders = [main_ui.cb_Items.itemText(i) for i in range(main_ui.cb_Items.count())]
    dest_folder = main_ui.line_to.text()
    hours_text = main_ui.line_hours.text()

    if not source_folders or not dest_folder:
        main_ui.text_Status.appendPlainText("Please select and append source directories and set the destination folder before starting the backup.\n")
        main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)
        return
    
    try:
        interval_hours = int(hours_text)
        if interval_hours <= 0:
            print(ValueError)
            raise ValueError
    except ValueError:
        main_ui.text_Status.appendPlainText("Please enter a valid positive number of hours.\n")
        main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)
        return

    stop_event.clear()  # Clear any previous stop event
    backup_thread = threading.Thread(target=run_backup_loop, args=(source_folders, dest_folder, interval_hours))
    backup_thread.start()
    print("ok")
    main_ui.text_Status.appendPlainText("Backup process started.\n")
    print("ok")
    main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)
    print("ok")


def stop_backup():
    global backup_thread

    stop_event.set()  # Signal the thread to stop

    if backup_thread and backup_thread.is_alive():
        backup_thread.join()  # Wait for the thread to finish
        main_ui.text_Status.appendPlainText("Backup process stopped.\n")
        main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)


def exit_app():
    sys.exit(app.exec())

main_ui.btn_openFrom.clicked.connect(insert_directory_from)
main_ui.btn_append.clicked.connect(insert_directory_toList)
main_ui.btn_delItem.clicked.connect(delete_directory_fromList)
main_ui.btn_openTo.clicked.connect(insert_directory_to)
main_ui.btn_Exit.clicked.connect(exit_app)
main_ui.btn_Start.clicked.connect(start_backup)
main_ui.btn_Stop.clicked.connect(stop_backup)

mainWindow.show()
sys.exit(app.exec())
