Name:		menumaker
Version:	0.99.7
Release:	1
Summary:	A menu generation utility
Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://menumaker.sourceforge.net/
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python2-devel

%description
Menu Maker is 100% Python heuristics-driven menu generator for
a number of X Window Managers and desktop environments. It features
large knowledge base of known programs, powerful and flexible search
algorithms, persistence of menus across several WMs

%prep
%setup -q

%build
%configure --with-python=/usr/bin/python2
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

sed -i 's|/usr/bin/env /usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/mmaker

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING INSTALL
%{_bindir}/*
%{_libdir}/%{name}
%{_infodir}/*.info.gz
%exclude %{_infodir}/dir

%changelog
* Tue Mar 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.7
- Rebuild for Fedora
