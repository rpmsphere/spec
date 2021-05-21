Name: twl
Summary: The Widget Laboratory
Version: 0.1.2
Release: 2.1
License: GPL
Group: Development/Tools
URL: https://launchpad.net/twl
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: python2-devel
Requires: gnome-python-metacity

%description
A gtk+ theme viewer that refreshes when the theme is modified.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=/usr

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{python_sitelib}/*
%{_datadir}/%{name}

%changelog
* Thu Oct 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
