%global debug_package %{nil}
%global kversion %(uname -r)

Summary: 	Intel® Ethernet Connections Boot Utility
Name: 		bootutil
Version: 	23.2
Release: 	1.bin
License: 	Commercial, freeware
Group:		Development/Tools
Source0:	https://downloadmirror.intel.com/19186/eng/Preboot.tar.gz
URL:		https://downloadcenter.intel.com/download/19186/Ethernet-Intel-Preboot-EFI-
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Requires:	kernel = %(uname -r|sed 's/-.*//')

%description
This package contains software and drivers for preboot environments, including
UEFI drivers, Intel® Boot Agent, and Intel® iSCSI Remote Boot images.

%prep
%setup -q -c
tar xf APPS/BootUtil/Linux_x64/DRIVER/iqvlinux.tar.gz
iconv -f utf16 -t utf8 readme.txt > README.txt
sed -i '154s|3|5|' src/linux/driver/Makefile

%build
export NALDIR=$PWD
cd src/linux/driver
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/char
cp src/linux/driver/iqvlinux.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/char
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp APPS/BootUtil/BootIMG.FLB %{buildroot}%{_libexecdir}/%{name}
cp APPS/BootUtil/iv.txt %{buildroot}%{_libexecdir}/%{name}
%ifarch x86_64
cp APPS/BootUtil/Linux_x64/bootutil64e %{buildroot}%{_libexecdir}/%{name}/%{name}
%else
cp APPS/BootUtil/Linux32/bootutil32 %{buildroot}%{_libexecdir}/%{name}/%{name}
%endif
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_libexecdir}/%{name}
exec %{name}
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%post
depmod -a > /dev/null 2> /dev/null

%postun
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt RelNotes.rtf
%{_bindir}/%{name}
%{_libexecdir}/%{name}
/lib/modules/%{kversion}/kernel/drivers/char/iqvlinux.ko

%changelog
* Fri Sep 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 23.2
- Initial package
