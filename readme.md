# FastAPI Upload files to NFS in Kubernetes 

![](project.png)

## Install NFS
    dnf install nfs-utils
    systemctl enable --now nfs-server

## Install NFS client on kubernetes nodes

    Install package nfs-utils for CentOS, Fedora and Redhat or install nfs-common for Ubuntu or Debian.

## Configura NFS

    mkdir /opt/{share,vol01,vol02}

    [root@centos8 ~]# cat /etc/exports
    /opt/share	192.168.123.0/24(rw,sync)
    /opt/vol01	192.168.123.0/24(rw,sync)
    /opt/vol02	192.168.123.0/24(rw,sync)

## Ativa NFS

    exportfs -ra
    exportfs -v
    exportfs -s

## Libera firewall

    firewall-cmd --new-zone=nfs --permanent
    firewall-cmd --zone=nfs --add-service=nfs --permanent
    firewall-cmd --zone=nfs --add-source=192.168.123.0/24 --permanent
    firewall-cmd --reload

# Comandos

## Build
    
    buildah bud --layers=true -t uploads:latest .

## Run
    
    mkdir {uploads,upload}

    podman run -it --rm --name uploads \
        -v ${PWD}/upload:/upload \
        -v ${PWD}/uploads:/uploads \
        -p8000:8000 uploads:latest
