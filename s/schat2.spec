%undefine _debugsource_packages

Name:           schat2
Version:        2.3.3
Release:        8.1
Summary:        Simple Chat 2
URL:            https://schat.me/
License:        GPLv3+
Group:          Networking/Chat
Source0:        schat-%{version}.tar.gz
BuildRequires:  qtwebkit-devel
BuildRequires:  GeoIP-devel

%description
Simple Chat is a simple and powerful cross-platform client-server chat for
local networks and the Internet. Chat is open source software.

%package server
Summary: Server for Simple Chat 2
Group: System/Servers

%description server
Server for Simple Chat 2.

%prep
%setup -q -n schat-%{version}

%build
qmake-qt4 GEOIP=1
make

%install
make INSTALL_ROOT=%{buildroot} install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%{_bindir}/%{name}
%{_libdir}/libschat-*
%{_libdir}/libschat.*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%files server
%{_libdir}/libschatd.*
%{_libdir}/schatd2
%{_sbindir}/schat*
%{_datadir}/schatd2

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.3
- Rebuilt for Fedora
