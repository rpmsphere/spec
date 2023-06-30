%undefine _debugsource_packages

Name:           dukto
Version:        6.0
Release:        17.1
Summary:        Dukto R6 file transfer tool
Group:          Applications/Networking
License:        GPL
URL:            https://msec.it/dukto
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:  qt4-devel

%description
Dukto is an easy file transfer tool designed for LAN use.
You can use it to transfer files from one PC to another,
without worrying about users, permissions, operating systems,
protocols, clients, servers and so on... Just start dukto on
the two PCs and transfer files and folders by dragging
onto it's window.

%prep
%setup -q

%build
/usr/bin/qmake-qt4 dukto.pro
make

%install
%__install -D -m0755 dukto "%{buildroot}%{_bindir}/dukto"
%__install -D -m0644 dukto.png "%{buildroot}%{_datadir}/pixmaps/dukto.png"
desktop-file-install --dir "%{buildroot}%{_datadir}/applications" dukto.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/dukto
%{_datadir}/applications/dukto.desktop
%{_datadir}/pixmaps/dukto.png

%changelog
* Wed Nov 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0
- Rebuilt for Fedora
