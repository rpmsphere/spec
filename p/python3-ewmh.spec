%define modulename ewmh

Name: python3-%modulename
Version: 0.1.6git
Release: 1
Summary: An implementation of EWMH (Extended Window Manager Hints) for python, based on Xlib
License: GPLv3
Group: Development/Python
URL: https://github.com/parkouss/pyewmh
Source: pyewmh-master.zip
BuildArch: noarch
BuildRequires: python3-devel python3-setuptools
Requires: python3-xlib

%description
An implementation of EWMH (Extended Window Manager Hints) for python, based on
Xlib. It allows EWMH-compliant window managers (most modern WMs) to be queried
and controlled.

%prep
%setup -q -n pyewmh-master

%build
%py3_build

%install
%py3_install

%files
%doc *.txt *.rst
%{python3_sitelib}/*

%changelog
* Wed Mar 13 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.6git
- Rebuilt for Fedora
* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.
* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux.
