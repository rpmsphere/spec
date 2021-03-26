%define debug_package %{nil}

%bcond_with acpi
%bcond_with bunzip2
%bcond_with cpio
%bcond_without coreutils
%bcond_with diffutils
%bcond_with dos2unix
%bcond_with e2fsprogs
%bcond_with eject
%bcond_with file
%bcond_with findutils
%bcond_with grep
%bcond_with hostname
%bcond_with kmod
%bcond_with nc
%bcond_with net_tools
%bcond_with passwd
%bcond_with procps
%bcond_with psmisc
%bcond_with rfkill
%bcond_with sed
%bcond_with sharutils
%bcond_with time
%bcond_with util_linux
%bcond_with which

Name: toybox
Version: 0.7.5
Release: 1
Source0: http://landley.net/toybox/downloads/%{name}-%{version}.tar.gz
Summary: A number of standard command line tools
URL: http://landley.net/toybox/
License: BSD
Group: System/Base
Conflicts: coreutils
%if %{with acpi}
Conflicts: acpi
%endif
%if %{with cpio}
Conflicts: cpio
%endif
%if %{with dos2unix}
Conflicts: dos2unix unix2dos
%endif
%if %{with eject}
Conflicts: eject
%endif
%if %{with which}
Conflicts: which
%endif
%if %{with sed}
Conflicts: sed
%endif
%if %{with time}
Conflicts: time
%endif

%description
A number of standard command line tools.

Toybox comes with smaller, but almost fully functional, replacements of
the command line tools in coreutils and more.

%prep
%setup -q
%setup_compile_flags
make defconfig \
HOSTCC="%{__cc}"

# adjust some settings
sed -i \
	-e 's,# CONFIG_EXPR is not set,CONFIG_EXPR=y,' \
	-e 's,# CONFIG_TR is not set,CONFIG_TR=y,' \
	-e 's,CONFIG_TOYBOX_UID_SYS=.*,CONFIG_TOYBOX_UID_SYS=0,' \
	-e 's,CONFIG_TOYBOX_UID_USR=.*,CONFIG_TOYBOX_UID_USR=1000,' \
	.config

# (tpg) disable these as they are in util-linux, procps-ng, grep, findutils  etc.
DISABLED="CLEAR COUNT HELP HEXEDIT
    IOTOP LSPCI
    LSUSB MKPASSWD NETSTAT
    PARTPROBE
    READAHEAD REBOOT RESET
    STRINGS ULIMIT
    EUPTIME USLEEP VCONFIG
    XXD"
%if ! %{with acpi}
DISABLED="$DISABLED ACPI"
%endif
%if ! %{with bunzip2}
DISABLED="$DISABLED BUNZIP2 BZCAT"
%endif
%if ! %{with cpio}
DISABLED="$DISABLED CPIO"
%endif
%if ! %{with coreutils}
DISABLED="$DISABLED CKSUM EXPR TR"
%endif
%if ! %{with diffutils}
DISABLED="$DISABLED CMP PATCH"
%endif
%if ! %{with dos2unix}
DISABLED="$DISABLED DOS2UNIX UNIX2DOS"
%endif
%if ! %{with e2fsprogs}
DISABLED="$DISABLED CHATTR LSATTR"
%endif
%if ! %{with eject}
DISABLED="$DISABLED EJECT"
%endif
%if ! %{with file}
DISABLED="$DISABLED FILE"
%endif
%if ! %{with findutils}
DISABLED="$DISABLED FIND XARGS"
%endif
%if ! %{with grep}
DISABLED="$DISABLED EGREP FGREP GREP PGREP"
%endif
%if ! %{with hostname}
DISABLED="$DISABLED HOSTNAME"
%endif
%if ! %{with kmod}
DISABLED="$DISABLED INSMOD LSMOD MODINFO RMMOD"
%endif
%if ! %{with nc}
DISABLED="$DISABLED NC NETCAT"
%endif
%if ! %{with net_tools}
DISABLED="$DISABLED IFCONFIG"
%endif
%if ! %{with passwd}
DISABLED="$DISABLED PASSWD"
%endif
%if ! %{with procps}
DISABLED="$DISABLED FREE PIDOF PKILL PMAP PS PWDX RENICE SYSCTL TOP VMSTAT W"
%endif
%if ! %{with psmisc}
DISABLED="$DISABLED KILLALL"
%endif
%if ! %{with rfkill}
DISABLED="$DISABLED RFKILL"
%endif
%if ! %{with sed}
DISABLED="$DISABLED SED"
%endif
%if ! %{with sharutils}
DISABLED="$DISABLED UUDECODE UUENCODE UNSHAR"
%endif
%if ! %{with time}
DISABLED="$DISABLED time"
%endif
%if ! %{with util_linux}
DISABLED="$DISABLED BLKID BLOCKDEV CAL DMESG FALLOCATE FLOCK FSFREEZE HWCLOCK IONICE KILL LOGIN LOSETUP MKSWAP MOUNT MOUNTPOINT NSENTER PIVOT_ROOT REV SETSID SU SWAPOFF SWAPON SWITCH_ROOT TASKSET UMOUNT"
%endif
%if ! %{with which}
DISABLED="$DISABLED which"
%endif

for i in $DISABLED; do
    sed -i -e "s,^CONFIG_$i=.*,# CONFIG_$i is not set," .config
done

%build
%make_build

%install
PREFIX="%{buildroot}" scripts/install.sh --symlink --force --long

%files
/bin/*
/sbin/*
%{_bindir}/*
%{_sbindir}/*
