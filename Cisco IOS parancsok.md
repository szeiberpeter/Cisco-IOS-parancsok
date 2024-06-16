# Cisco IOS parancsok
- Álomásnév beállítása: `Router(config) # hostname R1`

- Konfiguráció mentése:
    - Az eszköz saját NVRAM-jába
        - `Router#  write`
        - `Router# copy running-config startup-config`
    - TFTP-szerverre: 
        ```
        Router#copy running-config tftp: 
        Address or name of remote host []? 192.168.0.2
        Destination filename [Router-confg]? Router.config

        Writing running-config....!!
        [OK - 621 bytes]

        621 bytes copied in 3.004 secs (206 bytes/sec)
        ```


-  Belépési üzenet (banner) beállítása: `Router(config)# banner motd $Üzenet $`
- Interfészleírás megadása:
    ```
    Router(config)# interface GigabitEthernet0/0
    Router(config-if)# description Az interfesz leírása
    ```

- Helyi felhasználó létrehozása: `Router(config)# username admin secret titkosjelszo`

## Hálózati címek és forgalomirányítás

Interfész (Gig/Se/Vlan) IP-címének beállítása:
```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.0.1 255.255.255.0
Router(config-if)# no shutdown
```

Alapértelmezett átjáró beállítása: 
```
Switch(config)#ip default-gateway 192.168.0.1
```

Statikus alapértelmezett útvonal létrehozása:
```
Router(config)# ip route 0.0.0.0 0.0.0.0 se0/0/0
```

## Biztonság

Titkos jelszó:
```
Switch(config)# enable secret titkos
```

Konzoli (console) vagy Telnet (vty) hozzáférés jelszava:
```
Switch(config)# line vty 0
Switch(config-line)# password jelszo
Switch(config-line)# login
```
Belépés helyi felhsználóval:
```
R1(config-line)# login local
```

Jelszótitkosítás bekapcsolása:
```
Switch(config)# service password-encryption
```

## SSH
Szükséges előfeltételei:
- Állomásnév beállítása
- Domain-név: `R1(config)# ip domain-name jedlik.eu`
- Helyi felhasználó létrehozása
#### Kulcs  generálása:

```
Router(config)# crypto key generate rsa

The name for the keys will be: R1.jedlik.eu
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 1024
% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]
```
Belépés helyi felhasználóval, SSH kapcsolódás engedélyezése:
```
R1(config)# line vty 0
R1(config-line)# login local
R1(config-line)# transport input ssh
```
SSH 2-es verziójának beállítása: `R1(config)# ip ssh version 2`
