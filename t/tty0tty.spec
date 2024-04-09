%global kversion %(uname -r)

Name:           tty0tty
Release:        26.1
Summary:        Linux null modem emulator
Group:          System Environment/Kernel
License:        GPLv2
URL:            http://sourceforge.net/projects/tty0tty
Version:        1.2
Source0:        http://sourceforge.net/projects/tty0tty/files/tty0tty-%{version}.tgz
Patch0:		tty0tty-1.2.patch
BuildRequires:  kernel, kernel-devel
Requires:       tty0tty-kmod   

%description
The Linux null-modem emulator (tty0tty) is a kernel-module virtual serial
port driver for Linux. This create virtual tty ports pairs and use any pair
to connect one tty serial port based application to another.
There are a version using pseudo-terminal (UNIX 98 style).

%package kmod
Summary:        Kernel module for tty0tty
Requires:       kernel = %(uname -r|sed 's/-.*//')

%description kmod
Kernel module of Linux null modem emulator.

%prep
%setup -q
%patch 0 -p1

%build
make -C /lib/modules/*/build M=$PWD/module modules
make -C pts

%install
install -Dpm755 pts/tty0tty %{buildroot}%{_bindir}/%{name}
install -Dpm744 module/%{name}.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/tty/%{name}.ko

%post kmod
depmod -a > /dev/null 2> /dev/null ||:

%postun kmod
depmod -a > /dev/null 2> /dev/null ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README THANKS TODO VERSION
%{_bindir}/tty0tty

%files kmod
/lib/modules/%{kversion}/kernel/drivers/tty/%{name}.ko

%changelog
* Sun Mar 31 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Sun Aug 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1-1
- Update to 1.1
* Thu Nov 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Initial spec file
