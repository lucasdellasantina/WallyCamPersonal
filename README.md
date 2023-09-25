se cambia el firmware,se le coloca open ipc a travez de SD(archivos) se coloca eso en una sd cuando botea la camara 




para build 

make BOARD=t31_ultimate all 

en output sacar los archivos  —> ( uImage  rootfs.squashfs )

conectartr por ssh →  usr: root pass:12345 o pass:123456 

 SD (insertarla ANTES de bootear)  `cd /mnt/mmcblk0p1`

 ```
cd /mnt/mmcblk0p1
flashcp uImage /dev/mtd2
flashcp rootfs.squashfs /dev/mtd3
reboot 
```
https://github.com/OpenIPC/motors/tree/4c7dc45e5e877f38c076343f361159844374920a/t31-kmotor


ADD sample_motor.ko a las camaaras 

scp "C:\Users\lucas\Downloads\sample_motor.ko" root@192.168.0.103:/sample_motor.ko

Automatizar el inmode para que arranque cuando inicia 
(/etc/init.d/S98-you-script OR We recently added support for /etc/rc.Local  That runs at boot as well)

how to ?

 vi /etc/rc.local

add under line 

insmod /sample_motor.ko vstep_offset=0 hmaxstep=2130 vmaxstep=1600

chmod +x /etc/rc.local






 En la carpeta HOME ASSISTAN estan las modificaciones a los arcchivos y los scripts para mover las camaras 


 SSH HOME ASSITANT

intalar sshpass  en el contenedor

- [ ]  intalar sshpass  en el contenedor

```jsx
apk add sshpass
```

- [ ]  acceder por primera vez a cada camara por ssh para agregar el keypass

```jsx
sshpass -p '123456' ssh root@192.168.1.29

```

- [ ]  agregar en el configuration.yml

```jsx
shell_command:
  c1_x_down: /bin/bash c1_x_down.sh
  c1_x_up: /bin/bash c1_x_up.sh
  c1_y_down: /bin/bash c1_y_down.sh
  c1_y_up: /bin/bash c1_y_up.sh
  c1_r: /bin/bash c1_r.sh
  c1_e: /bin/bash c1_e.sh
```

```jsx
 sshpass -p '123456' ssh root@192.168.1.29 | t31-kmotor -d g -x 300 -y 0

```

pegar en el directorio  (falta el de reset)

[
Lovelace