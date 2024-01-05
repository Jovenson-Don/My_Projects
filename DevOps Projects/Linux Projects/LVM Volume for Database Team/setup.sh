sudo -i

# Install lvm
yum install -y lvm2

# Create dba_users group
groupadd dba_users

# Add bob
usermod -G dba_users bob

# Create PVs
pvcreate /dev/vdb
pvcreate /dev/vdc

# Create VG
vgcreate dba_storage /dev/vdb /dev/vdc

#Create LVM
lvcreate -n volume_1 -l 100%FREE dba_storage

## Persistent mountpoint

# Format
mkfs.xfs /dev/dba_storage/volume_1
# Mount
mkdir -p /mnt/dba_storage
mount -t xfs /dev/dba_storage/volume_1 /mnt/dba_storage
# Make persistent
echo "/dev/mapper/dba_storage-volume_1 /mnt/dba_storage xfs defaults 0 0" >> /etc/fstab
# Ensure that the mountpoint "/mnt/dba_storage" has the group ownership set to the "dba_users" group
chown :dba_users /mnt/dba_storage
# Ensure that the mount point "/mnt/dba_storage" has "read/write" and execute permissions for the owner and group and no permissions for anyone else.
chmod 770 /mnt/dba_storage