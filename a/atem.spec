Name:           atem
Version:        0.3.5
Release:        6.1
Summary:        Command line tool to convert MetaStock to csv
License:        BSD-3-Clause
Group:          Productivity/Text/Convertors
URL:            https://github.com/rudimeier/atem/
Source:         %{name}-%{version}.tar.gz
BuildRequires: gengetopt
BuildRequires: help2man

%description
Atem converts metastock binary data to ASCII text. It was written due to the
lack of a fast and reliable tool.

%prep
%setup -q

%build
autoreconf -vfi
%configure
make

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
* Sat Oct  8 2011 sweet_f_a@gmx.de
- build from tar ball instead of git repo
* Mon Sep  5 2011 sweet_f_a@gmx.de
- initial package atem 0.3.2
