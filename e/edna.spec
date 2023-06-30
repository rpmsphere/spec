Summary:	An MP3 server
Name:		edna
Version:	0.6
Release:	3.1
Source0:	https://sourceforge.net/projects/edna/files/edna/0.6/%{name}-%{version}.tar.gz
License:	GPL
Group:		System Environment/Daemons
BuildArch:	noarch
Requires:	python2
URL:		https://edna.sourceforge.net/

%description
edna allows you to access your MP3 collection from any networked computer.
This software streams your MP3s via HTTP to any MP3 player that supports
playing off a remote connection (e.g. Winamp, FreeAmp, Sonique, XMMS, WMP).

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING README
%{_bindir}/%{name}
/usr/lib/%{name}

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
