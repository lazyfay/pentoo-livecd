subarch: i686
version_stamp: 2009.0
target: livecd-stage1
rel_type: default
profile: default/linux/x86/2008.0
snapshot: 2009.0-2
source_subpath: default/stage3-i686-2009.0
portage_confdir: /root/pentoo/portage
portage_overlay: /usr/local/portage /usr/portage/local/layman/enlightenment
# /usr/portage/local/layman/jokey
cflags: -Os -march=i686 -mtune=prescott -pipe -fomit-frame-pointer
cxxflags: -Os -march=i686 -mtune=prescott -pipe -fomit-frame-pointer


# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
# pkgcache_path:

livecd/use: X livecd -gnome -nls gtk -kde -eds gtk2 cairo -pam firefox gpm dvdr oss
mmx sse mpi wps
wifi injection lzma speed gnuplot pyx
-quicktime -qt -qt3 qt3support qt4 -webkit -cups -spell lua -ipv6
png jpeg gif dri svg aac nsplugin xrandr
alsa esd gstreamer jack mp3 vorbis wavpack wma
dvd mpeg ogg rtsp x264 xvid sqlite truetype
opengl dbus binary-drivers -hal acpi

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages:
sys-kernel/pentoo-sources
app-admin/gamin
=app-admin/genmenu-9999
app-admin/localepurge
app-admin/syslog-ng
app-arch/gzip
app-crypt/chntpw
app-crypt/johntheripper
app-crypt/md5bf
app-crypt/openvpn-blacklist
app-crypt/ophcrack
app-crypt/SIPcrack
app-editors/hexedit
app-editors/nano
app-editors/ghex
app-editors/scite
app-editors/vim
app-text/epdfview
app-forensics/autopsy
app-forensics/cmospwd
app-forensics/galleta
app-forensics/pasco
app-forensics/sleuthkit
app-fuzz/Peach
app-fuzz/bed
app-fuzz/bss
app-fuzz/fuzzer-server
app-fuzz/fusil
app-fuzz/http-fuzz
app-fuzz/smtp-fuzz
app-fuzz/smudge
app-fuzz/ohrwurm
app-fuzz/taof
app-misc/livecd-tools
app-misc/screen
app-mobilephone/obexftp
app-portage/gentoolkit
app-portage/layman
app-text/dos2unix
#dev-db/absinthe
dev-db/minimysqlator
dev-db/mssqlscan
dev-db/oat
dev-db/sqid
#dev-db/sqlat
dev-db/sqlbf
#dev-db/sqlinject
dev-db/sqlibf
dev-db/sqlix
dev-db/sqlmap
dev-db/sqlninja
dev-java/jad-bin
dev-lang/nasm
dev-libs/klibc
dev-libs/libxml2
dev-libs/libxslt
dev-libs/openobex
dev-python/pysqlite
dev-python/psyco
=dev-python/lxml-1.3.6
dev-util/edb
dev-util/dialog
dev-util/subversion
dev-util/nvidia-cuda-sdk
dev-util/amd-stream-sdk-bin
gnome-base/gnome-menus
mail-client/mozilla-thunderbird-bin
media-gfx/scrot
media-fonts/font-misc-misc
media-sound/audacious
media-sound/alsa-utils
media-sound/sox
media-video/vlc
net-analyzer/aimsniff
net-analyzer/amap
net-analyzer/angst
net-analyzer/arpwatch
net-analyzer/authforce
net-analyzer/autoscan-network
net-analyzer/dnsa
net-analyzer/dnsenum
#net-analyzer/driftnet
net-analyzer/dsniff
net-analyzer/etherape
net-analyzer/ettercap
net-analyzer/fasttrack
net-analyzer/fierce
net-analyzer/firewalk
net-analyzer/fragroute
net-analyzer/ftester
net-analyzer/geoedge
net-analyzer/gspoof
net-analyzer/honeyd
net-analyzer/hping
net-analyzer/hunt
#net-analyzer/hydra
net-analyzer/inguma
net-analyzer/ike-scan
net-analyzer/isic
net-analyzer/macchanger
net-analyzer/mbrowse
net-analyzer/medusa
net-analyzer/metacoretex-ng
net-analyzer/metagoofil
net-analyzer/metasploit
net-analyzer/mosref
net-analyzer/nbtscan
net-analyzer/netcat
net-analyzer/netdiscover
#net-analyzer/netdude
net-analyzer/netwag
net-analyzer/netwox
net-analyzer/ngrep
net-analyzer/nikto
net-analyzer/nmap
net-analyzer/nmbscan
=net-analyzer/ntop-3.3.8
net-analyzer/ntp-fingerprint
net-analyzer/onesixtyone
net-analyzer/p0f
net-analyzer/packit
net-analyzer/paketto
net-analyzer/rain
#net-analyzer/sara
net-analyzer/scanssh
net-analyzer/siphon
net-analyzer/sipvicious
net-analyzer/smtpmap
net-analyzer/sniffit
net-analyzer/snmpenum
net-analyzer/snort
net-analyzer/sslstrip
net-analyzer/sslsniff
net-analyzer/subdomainer
net-analyzer/tcpdump
net-analyzer/tcptraceroute
net-analyzer/thcrut
net-analyzer/theHarvester
net-analyzer/traceroute
net-analyzer/upnpscan
net-analyzer/voiphopper
net-analyzer/w3af
net-analyzer/webshag
net-analyzer/wfuzz
net-analyzer/wireshark
net-analyzer/xprobe
net-analyzer/yersinia
net-dialup/linux-atm
net-dialup/lrzsz
net-dialup/minicom
net-dns/bind-tools
net-firewall/fwbuilder
net-fs/nfs-utils
net-fs/mount-cifs
net-ftp/ftp
net-ftp/gproftpd
net-ftp/oftpd
net-im/pidgin
net-irc/irssi
net-irc/xchat
net-misc/axel
net-misc/bridge-utils
net-misc/curl
net-misc/dhcp
net-misc/dhcpcd
#net-misc/ipsorcery
net-misc/iputils
net-misc/karma
net-misc/nemesis
net-misc/neon
net-misc/netkit-fingerd
net-misc/netkit-rsh
net-misc/netsed
net-misc/ntp
net-misc/openssh
net-misc/openvpn
net-misc/partysip
net-misc/proxychains
net-misc/raccess
net-misc/rdesktop
net-misc/grdesktop
net-misc/rsync
#net-misc/sipbomber
net-misc/sipp
#net-misc/siproxd
net-misc/sipsak
net-misc/socat
net-misc/stunnel
net-misc/tcpick
net-misc/telnet-bsd
net-misc/tightvnc
net-misc/voipong
net-misc/wget
net-misc/whois
net-misc/wicd
net-misc/wlan2eth
net-proxy/3proxy
net-proxy/burpsuite
net-proxy/httpush
net-proxy/privoxy-tor
net-proxy/proxystrike
net-proxy/tsocks
#net-wireless/afrag
net-wireless/aircrack-ng
#net-wireless/airsnort
#net-wireless/airtraf
net-wireless/athload
net-wireless/b43-openfwwf
net-wireless/bluez-libs
net-wireless/bluez-utils
net-wireless/btscanner
net-wireless/cowpatty
net-wireless/crda
net-wireless/kismet-newcore
net-wireless/spectools
net-wireless/mdk
#net-wireless/ska
#net-wireless/waveselect
net-wireless/wepattack
net-wireless/wepdecrypt
net-wireless/wifi-radar
#net-wireless/wifiscanner
net-wireless/wifitap
net-wireless/wireless-tools
net-wireless/wpa_supplicant
net-wireless/hostapd
net-www/netscape-flash
sys-apps/baselayout
sys-apps/eject
sys-apps/hwsetup
sys-apps/iproute2
sys-apps/less
sys-apps/microcode-ctl
sys-apps/microcode-data
sys-apps/pciutils
sys-apps/portage
#sys-apps/slocate
sys-apps/v86d
sys-block/disktype
sys-block/gparted
sys-boot/grub
sys-boot/syslinux
sys-devel/gettext
sys-devel/crossdev
sys-devel/gdb
sys-fs/device-mapper
sys-fs/jfsutils
sys-fs/reiserfsprogs
sys-fs/reiser4progs
sys-fs/squashfs-tools
sys-fs/udev
sys-libs/gpm
sys-libs/libkudzu
sys-power/acpid
www-client/mozilla-firefox-bin
www-servers/lighttpd
x11-base/xorg-server
x11-base/xorg-x11
#x11-drivers/xf86-input-virtualbox
#x11-drivers/xf86-video-virtualbox
x11-libs/ecore
x11-libs/esmart
x11-libs/evas
x11-libs/gksu
#x11-libs/gtk+
#x11-drivers/xf86-input-evdev
x11-drivers/xf86-input-keyboard
x11-drivers/xf86-input-mouse
x11-drivers/xf86-video-apm
x11-drivers/xf86-video-ark
x11-drivers/xf86-video-ati
x11-drivers/xf86-video-chips
x11-drivers/xf86-video-cirrus
x11-drivers/xf86-video-fbdev
x11-drivers/xf86-video-glint
x11-drivers/xf86-video-i128
x11-drivers/xf86-video-intel
x11-drivers/xf86-video-mach64
x11-drivers/xf86-video-mga
x11-drivers/xf86-video-neomagic
x11-drivers/xf86-video-nv
#x11-drivers/xf86-video-openchrome
#x11-drivers/xf86-video-r128
x11-drivers/xf86-video-rendition
x11-drivers/xf86-video-radeonhd
x11-drivers/xf86-video-s3
x11-drivers/xf86-video-s3virge
x11-drivers/xf86-video-savage
x11-drivers/xf86-video-siliconmotion
x11-drivers/xf86-video-sis
x11-drivers/xf86-video-tdfx
x11-drivers/xf86-video-trident
x11-drivers/xf86-video-vesa
x11-drivers/xf86-video-vmware
x11-drivers/xf86-video-voodoo
x11-misc/dmenu
x11-plugins/firecat
#x11-plugins/e_modules
x11-plugins/e_modules-bling
x11-plugins/e_modules-calendar
x11-plugins/e_modules-cpu
x11-plugins/e_modules-language
x11-plugins/e_modules-mem
x11-plugins/e_modules-net
#x11-plugins/e_modules-notification
x11-plugins/e_modules-screenshot
x11-plugins/e_modules-weather
x11-plugins/e_modules-wlan
x11-plugins/itask-ng
x11-plugins/pidgin-encryption
x11-plugins/winlist_ng
x11-proto/dri2proto
x11-themes/gtk-chtheme
x11-terms/rxvt-unicode
x11-libs/e_dbus
x11-wm/dwm
x11-wm/enlightenment
x11-base/xorg-x11
