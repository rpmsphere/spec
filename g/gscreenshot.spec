Summary: A simple screenshot tool
Name: gscreenshot
Version: 2.8.0
Release: 5.1
Source0: https://github.com/thenaterhood/gscreenshot/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
License: GPLv2
Group: Utilities
BuildArch: noarch
BuildRequires: python3-devel
Requires: scrot python3 python3-pillow python3-gobject
URL: https://github.com/thenaterhood/gscreenshot

%description
gscreenshot is a gtk frontend for scrot, an application for taking screenshots,
written in python and pygtk. This is a fork of the original project (last
updated in 2006) that updates it to use modern technologies and to provide
updated functionality.

This application was originally written by matej.horvath. The original project
can be found at https://code.google.com/p/gscreenshot/ while Google Code is
still up and running.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%{_bindir}/%{name}*
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/menu/%{name}

%changelog
* Tue Sep 12 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.0
- Rebuilt for Fedora
