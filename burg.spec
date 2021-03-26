Name:           burg
Version:        1.98.20100623
Release:        1
Summary:        Brand-new Universal loadeR from GRUB
Group:          System Environment/Base
License:        GPLv3+
URL:            http://code.google.com/p/burg/
#Source:	bzr branch lp:burg
Source0:        %{name}-%{version}.tar.gz
Source1:        90_persistent
Source2:        burg.default


BuildRequires:  flex bison ruby binutils texinfo
##BuildRequires:  glibc-static lzo-devel
BuildRequires:  freetype-devel libusb-devel
BuildRequires:  ncurses-devel glibc-devel
BuildRequires:  autoconf automake gettext-devel

%description
burg is a brand-new boot loader based on GRUB. It uses a new object format
which allows it to be built in a wider range of OS, including
Linux/Windows/OSX/Solaris/FreeBSD, etc. It also has a highly configurable
menu system which works in both text and graphic mode. Additional features
like stream support and multiple input/output device are also planned.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure TARGET_LDFLAGS=-static --disable-werror
make

%install
set -e
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# Script that makes part of burg.cfg persist across updates
##install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/burg.d/

# Ghost config file
install -d $RPM_BUILD_ROOT/boot/%{name}
touch $RPM_BUILD_ROOT/boot/%{name}/burg.cfg
ln -s ../boot/%{name}/burg.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.cfg

# Install ELF files modules and images were created from into
# the shadow root, where debuginfo generator will grab them from
find $RPM_BUILD_ROOT -name '*.mod' -o -name '*.img' |
while read MODULE
do
        BASE=$(echo $MODULE |sed -r "s,.*/([^/]*)\.(mod|img),\1,")
        # Symbols from .img files are in .exec files, while .mod
        # modules store symbols in .elf. This is just because we
        # have both boot.img and boot.mod ...
        EXT=$(echo $MODULE |grep -q '.mod' && echo '.elf' || echo '.exec')
        TGT=$(echo $MODULE |sed "s,$RPM_BUILD_ROOT,.debugroot,")
#        install -m 755 -D $BASE$EXT $TGT
done

# Defaults
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/default/burg

##rm -rf $RPM_BUILD_ROOT%{_infodir}

%clean    
rm -rf $RPM_BUILD_ROOT

%post
# Determine the partition with /boot
BOOT_PARTITION=$(df -h /boot |(read; awk '{print $1; exit}'))
%{name}-install $BOOT_PARTITION
%{name}-mkconfig -o /boot/burg/burg.cfg

%triggerin -- kernel, kernel-PAE
%{name}-mkconfig >/dev/null 2>&1

%triggerun -- kernel, kernel-PAE
%{name}-mkconfig >/dev/null 2>&1

%files
%{_libdir}/%{name}
%{_sbindir}/%{name}-*
%{_bindir}/%{name}-*
%dir %{_sysconfdir}/burg.d
%config %{_sysconfdir}/burg.d/??_*
%{_sysconfdir}/burg.d/README
%{_sysconfdir}/%{name}.cfg
%{_sysconfdir}/default/burg
%dir /boot/%{name}
# Actually, this is replaced by update-burg from scriptlets,
# but it takes care of modified persistent part
%config(noreplace) /boot/%{name}/burg.cfg
%doc COPYING INSTALL NEWS README THANKS TODO ChangeLog
%exclude %{_mandir}
%exclude %{_datadir}/info/dir
%{_datadir}/info/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.98.20100623
- Rebuild for Fedora
