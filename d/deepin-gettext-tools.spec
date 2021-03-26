Name:           deepin-gettext-tools
Version:        1.0.3
Release:        5.1
Summary:        Deepin Gettext Tools
License:        GPL3
URL:            https://github.com/linuxdeepin/${name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python2

%description
Deepin Gettext Tools.

%prep
%setup -q

%build
sed -e 's/sudo cp/cp/' -i src/generate_mo.py
sed -e 's/qmake/qmake-qt5/' -e '/lupdate/d' -i Makefile

%install
make DESTDIR=%{buildroot} install

%files
/usr/lib/deepin-gettext-tools
%{_bindir}/*
%doc README.md LICENSE

%changelog
* Wed Aug 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuild for Fedora
* Mon Sep 28 2015 Derek Dai
- Initial package
