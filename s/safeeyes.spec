Name: safeeyes
Summary: Protect your eyes from eye strain
Version: 2.0.9
Release: 1
Group: Utility
License: GPLv3
URL: https://github.com/slgobinath/SafeEyes
Source0: https://github.com/slgobinath/SafeEyes/archive/v%{version}.tar.gz#/SafeEyes-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%description
Safe Eyes is a simple tool to remind you to take periodic breaks for your
eyes. This is essential for anyone spending more time on the computer to
avoid eye strain and other physical problems.

Features:
 - Short breaks with eye exercises
 - Long breaks to change physical position and to warm up
 - Strict break for those who are addicted to computer
 - Do not disturb when working with full-screen applications
 - Notifications before every break
 - Optional audible alert at the end of break
 - Option to lock screen after long breaks
 - Smart pause and resume based on system idle time
 - Multi-monitor support
 - Plugins to utilize Safe Eyes
 - Elegant and customizable design

%prep
%setup -q -n SafeEyes-%{version}
#sed -i 's|38.6.0|36.2.0|' setup.py

%build
%py3_build

%install
%py3_install

%post
gtk-update-icon-cache /usr/share/icons/hicolor

%postun
gtk-update-icon-cache /usr/share/icons/hicolor

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*.png

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.9
- Rebuild for Fedora
