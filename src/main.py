from tkinter import *
from tkinter import ttk
from typing import ClassVar
from tkinter.filedialog import askopenfilename
import os
import sys
import brotli
import threading
import winsound


root = Tk()
root.geometry("380x70")
root.resizable(width=FALSE, height=FALSE)
root.title("WASM Compressor by Mateusz Perczak")
root.configure(background="#fff")
img: ClassVar = PhotoImage(data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00`\x00\x00\x00`\x08\x06\x00\x00\x00\xe2\x98w8\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x02kIDATx\xda\xed\xda\xcb+Da\x18\xc7q\xff\x86\xbf\x86\x1a\xa4dA\n%c\\W\x16\x8a\x11\x93\xd20\x14\xe3\xb2bM\x16X\xd8\x91\xcb\x94\xfb\xb5\xc4\x8c\xad\x15rYPd\\V\xafy\xa6,\x8ec\x9c3\xce{\xce\x82\xefS\xbf\xd2\xf4\xbe\xa5\xf73=\xcf{899\x14EQ\x14EQ\xd4/j\xfc\xe8]y\x99\xdc`\xe2\xc7x\xfd\xfb\x00\x00\x00\x00\x00\x00\xf0\x7f\x03\x00\x00\xb4 \x00\x00\x00\x00\x00\x00\x18\xc2\x00\x00@\x0b\x02\x00\x00\x00\x00\x00\x80!\x0c\x00\x00\xb4 \x00\x00\x00\x00\x00\x00\x18\xc2\x00\x00@\x0b\x02\x00\x00\x00\x00\x00\x80!\x0c\x00\x00\xb4 \x00\x00\x00\x00\x00\x00\x18\xc2\x00\x00@\x0b\x02\x00\x00\x00\x00\x00\x80!\x0c\x00\x00\xb4 \x00\x00\x00\x00\x00\x00\x18\xc2\x00\x00\xf0}Fv^T^\xd9\xe2\x8f\x89\xee\xbe\x00\xe0V\x06b\x8f\x96\x00\x83\xb1\'\x00\xdcJ\xcf\xc2\x9d%\x80\xac\x01\xc0\xa5\xb4N\x9c[\x02\xb4N\x9e\x03\xe0VjB\xc7\x96\x00\xb2\x06\x00\x172z\xf0\xa6\n\xabW-\x01\nRkF\xf7_\x01\xd0\x9d\xae\xd9k\xcb\xc3\xffL\xf7\xdc5\x00\xbaS\x17\x8e\xdb\x06\x90\xb5\x00h\xcc\xd8\xe1\x9b*\xaaY\xb3\r ke\x0f\x00\x9a\x12\x9a\xbf\xb1}\xf8\x9f\t\xcd\xdf\x02\xa0+\xb5\xbd\'Y\x03\xf8{O\x01\xd0r\xfb\xd9{M\xdfl\xb2\x05(\xa8ZQ#\x1e\xdc\x86\xfe<@\xe7\xcc\x95\xe9p\x8b\xfd1\x15\x9c\xbeT\xd1\x9dd:\xc1\x99KU\xd2\xb8nZ\'{\x01\xd0|\xfb\x91\xc3\x1f\xdaz6\xad\x93\xcf\x8akc\x9e\xdf\x86\xfe<@i\xcb\xa6\xe1P\xe5\x9b\x9fim\xc7\xf4\x85a\xad\xec\x05\xc0a\xa4\x97\x1b\xfe\xdc\x9cj9\x99\xd6\x0eo\'Ms\x00\x00\x87\xf1U\xda\x07\x88~\x01\x90\xbd\x008mAM\x1b\xb6\x07\xab\xb4\'C\x0bj\xa6\x059N\xc3@\xc2p\xa8r\xdb\xc94\x84K\xea\x8d7\xa1\x86\xc13\x00\x9c&\xbcx\xaf\xf2\xcb\x97L7!\x19\xb8\xd2\xf3%\xedS\x17\xa6\x1b\x90\xec\t/=\x00\xa0#\x81\xfex\xd6\x0fb\xf5\x91\x04O\xc2\xda\x9e\x86SO\xb4\x15m{\xb6\x0f\xbf\xa2m?\xfd\xff\x03\x004#\x04"qS;\xfa\xdav\xe4\x9b\xef\xd5\xe1\xff\xcb\xf7\x82\xfaR}]\x86\xab\xdcp|\x95\xcb\xe9\xc8\xcf\xf2\x99\x17=\x9f\x17\xb3x1\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa2(\x8a\xa2(\x8a\xca\xa6>\x00 \x87\xd1R\xc4i\xf0\xc1\x00\x00\x00\x00IEND\xaeB`\x82')
root.wm_iconphoto(True, img)
current_dir: str = os.getcwd()


def compress(path_with_file):
    try:
        file: str = os.path.basename(path_with_file)
        os.chdir(path_with_file.replace(os.path.basename(path_with_file), ""))
        with open(file, "rb") as data:
            bytes_from_file: bytes = data.read()
        compressed_bytes: bytes = brotli.compress(bytes_from_file)
        with open(os.path.splitext(os.path.basename(file))[0] + ".br", "wb") as data:
            data.write(compressed_bytes)
        file_label.configure(text="Done")
        os.system(r'explorer /select,%s' % (path_with_file.replace(os.path.basename(path_with_file), "") + os.path.splitext(os.path.basename(file))[0] + ".br").replace('/', '\\'))
    except Exception as e:
        file_label.configure(text="Err: " + str(e))
    progress_bar.stop()
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)



def add_file():
    global current_dir
    file: str = askopenfilename(initialdir=current_dir, filetypes=(("Wasm files", "*.wasm"), ("All Files", "*.*")),
                                title="Choose a wasm file.")
    if file:
        file_label.configure(text="Compressing: " + os.path.basename(file))
        progress_bar.start(6)
        compress_file: ClassVar = threading.Thread(target=compress, args=(file,))
        compress_file.daemon = True
        compress_file.start()


main_style: ClassVar = ttk.Style()
main_style.theme_use('clam')
main_style.configure("TButton", background='#fff', relief="flat", font=('Bahnschrift', 12), foreground='#000')
main_style.configure("TLabel", background='#fff', foreground='#000', border='0', font=('Bahnschrift', 11))
main_style.configure("G.Horizontal.TProgressbar", foreground='#fff', background='#000', lightcolor='#fff'
                     , darkcolor='#fff', bordercolor='#fff', troughcolor='#fff')

file_button: ClassVar = ttk.Button(root, text="ADD", cursor="hand2", takefocus=False, command=add_file)
file_button.place(relx=0, rely=0, relwidth=0.2, relheight=1)

file_label: ClassVar = ttk.Label(root, anchor="center", text="Add file to start")
file_label.place(relx=0.2, rely=0.3, relwidth=0.8, relheight=0.4)

progress_bar: ClassVar = ttk.Progressbar(root, orient=HORIZONTAL, mode="indeterminate"
                                         , style="G.Horizontal.TProgressbar")
progress_bar.place(relx=0.2, rely=0.9, relwidth=0.8, height=10)

root.after(5000, lambda: root.focus_force())
root.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))
root.mainloop()
