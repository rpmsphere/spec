%undefine _debugsource_packages

Name: aewm
Summary: Minimalist window manager for X11
Version: 1.3.12
Release: 2.1
License: GPL
Group: X11
URL: http://www.red-bean.com/decklin/aewm/
Source0: http://www.red-bean.com/decklin/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  gtk2-devel libX11-devel libXext-devel libXft-devel

%description
aewm is a minimalist window manager for X11. It has no nifty
features, but is light on resources and extremely simple in
appearance. It should eventually make a good reference implementation
of the ICCCM. A few separate programs are included to handle running
programs, switching between windows, etc.

%prep
%setup -q
sed -i 's|GTKLIB =|GTKLIB = $(X11LIB)|' Makefile
sed -i -e 's|/X11R6||' -e 's|/lib|/%{_lib}|' -e 's|/man/|/share/man/|' Makefile
sed -i '8,14s|#OPT|OPT|' Makefile
sed -i 's|CC = gcc|CC = gcc -Wl,--allow-multiple-definition|' Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE NEWS README
%{_sysconfdir}/X11/%{name}
%{_bindir}/ae*
%{_mandir}/man1/ae*.1x.*

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.12
- Rebuilt for Fedora
