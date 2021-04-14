%undefine _debugsource_packages

name:          ssvnc
Summary:       Enhanced TightVNC Viewer
Version:       1.0.30
Release:       11.1
License:       GPL v2
Group:         Productivity/Networking/Remote Desktop/Security
Source0:       %name-%version.src.tar.gz
Source1:       icons.tar.bz2
Patch:         makefile.patch
URL:           http://www.karlrunge.com/x11vnc/ssvnc.html
BuildRequires: libX11-devel java-devel libjpeg-devel lua
BuildRequires: imake libXt-devel libXmu-devel libXaw-devel
Provides:      ssvncviewer tsvnc
BuildRequires: compat-openssl10-devel

%description
SSVNC adds encryption security to VNC connections. It provides a GUI for Windows,
Mac OS X, and Unix that automatically starts up an STUNNEL SSL tunnel for SSL or
ssh for SSH connections to any other VNC server.

Authors:
--------
    Karl J. Runge <runge@karlrunge.com>

%description -l pl
SSVNC zapewnia szyfrowanie połączeń VNC. Dostarcza GUI dla systemu Windows,
Mac OS X i Unix, które automatycznie uruchamiają tunel SSL STUNNEL dla połączeń
SSL lub ssh dla połączeń SSH do jakichkolwiek innych serwerów VNC.

Autorzy:
--------
    Karl J. Runge <runge@karlrunge.com>

%prep
%setup -q
%setup -T -D -q -a 1

%patch
sed -i -e 's|LIB      = lib/ssvnc|LIB      = %{_lib}/ssvnc|' Makefile

%build
make config
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make  ROOT=$RPM_BUILD_ROOT PREFIX=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README README.src
%{_bindir}/*
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/ssvnc.desktop
%{_libdir}/ssvnc/*
%{_mandir}/man1/*.gz

%changelog
* Wed Jun 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.30
- Rebuilt for Fedora
