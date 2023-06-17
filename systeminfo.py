import tkinter as tk
import subprocess

def start_apache():
    subprocess.call(['sudo', 'service', 'apache2', 'start'])

def stop_apache():
    subprocess.call(['sudo', 'service', 'apache2', 'stop'])

def start_mysql():
    subprocess.call(['sudo', 'service', 'mysql', 'start'])

def stop_mysql():
    subprocess.call(['sudo', 'service', 'mysql', 'stop'])

def start_vsftpd():
    subprocess.call(['sudo', 'service', 'vsftpd', 'start'])

def stop_vsftpd():
    subprocess.call(['sudo', 'service', 'vsftpd', 'stop'])

root = tk.Tk()
root.title("LukaHosting Servis Kontrol Aracı / Weppp")

apache_frame = tk.Frame(root)
apache_frame.pack(pady=10)
apache_label = tk.Label(apache_frame, text="Apache Servisi")
apache_label.pack(side=tk.LEFT, padx=10)
apache_start_btn = tk.Button(apache_frame, text="Başlat", command=start_apache)
apache_start_btn.pack(side=tk.LEFT)
apache_stop_btn = tk.Button(apache_frame, text="Durdur", command=stop_apache)
apache_stop_btn.pack(side=tk.LEFT)

mysql_frame = tk.Frame(root)
mysql_frame.pack(pady=10)
mysql_label = tk.Label(mysql_frame, text="MySQL Servisi")
mysql_label.pack(side=tk.LEFT, padx=10)
mysql_start_btn = tk.Button(mysql_frame, text="Başlat", command=start_mysql)
mysql_start_btn.pack(side=tk.LEFT)
mysql_stop_btn = tk.Button(mysql_frame, text="Durdur", command=stop_mysql)
mysql_stop_btn.pack(side=tk.LEFT)

vsftpd_frame = tk.Frame(root)
vsftpd_frame.pack(pady=10)
vsftpd_label = tk.Label(vsftpd_frame, text="vsftpd Servisi")
vsftpd_label.pack(side=tk.LEFT, padx=10)
vsftpd_start_btn = tk.Button(vsftpd_frame, text="Başlat", command=start_vsftpd)
vsftpd_start_btn.pack(side=tk.LEFT)
vsftpd_stop_btn = tk.Button(vsftpd_frame, text="Durdur", command=stop_vsftpd)
vsftpd_stop_btn.pack(side=tk.LEFT)

root.mainloop()
