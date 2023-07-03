%undefine _debugsource_packages

Name: pxdmcp
Summary: An XDMCP standalone client
Version: 1.0.1
Release: 8.1
Group: Applications/Internet
License: BSD
URL: https://freecode.com/projects/pxdmcp
Source0: ftp://ftp.lysator.liu.se/pub/unix/pxdmcp/%{name}-%{version}.tar.gz
BuildRequires: libnsl2-devel

%description
PXDMCP can be used to request an X11 Display Manager (XDM, GDM, CDE .. etc)
to start a new terminal session (normally used to bring up a login window)
using the XDMCP protocol. This in effect does the same thing as an X
server does when started with the "-query" argument but can be used in
circumstances where that might be impractical.

%prep
%setup -q

%build
make LIBS=-lnsl XAUTH=/usr/bin/xauth

%install
install -Dm755 xdmcp %{buildroot}%{_bindir}/xdmcp

%files
%doc README TODO
%{_bindir}/xdmcp

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
