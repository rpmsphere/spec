Summary: A simple screenshot tool
Name: gscreenshot
Version: 3.5.0
Release: 1
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

%files
%doc README.md
%{_bindir}/%{name}*
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/menu/%{name}
%{_datadir}/bash-completion/completions/gscreenshot
%{_mandir}/man1/gscreenshot.1.gz
%{_datadir}/zsh/site-functions/_gscreenshot

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.5.0
- Rebuilt for Fedora
