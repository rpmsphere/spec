Name:           truffle
Version:        0.1.3
Release:        7.1
Summary:        A tool to roll over futures contracts
License:        BSD-3-Clause
Group:          Productivity/Text/Convertors
URL:            https://github.com/hroptatyr/truffle/
Source:         %{name}-%{version}.tar.xz
Patch1:         test-portable-readlink.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Truffle is a command line tool to roll over futures contracts
according to some specified roll-over schema.  The focus is clearly
on batch processing and speed.

%prep
%setup -q
%patch1 -p1

%build
%configure --docdir=%{_docdir}
make V=1

%install
%{?make_install} %{!?make_install:make install DESTDIR=%{buildroot}}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora
* Fri Jun  1 2012 sweet_f_a@gmx.de
- update to tarball release 0.1.3
* Wed Sep  7 2011 sweet_f_a@gmx.de
- initial package truffle 0.1.0
