%global debug_package %{nil}
Name: python-plwm
Summary: Pointless Window Manager
Version: 2.7rc1
Release: 3.1
Group: Development/Libraries
License: GPL
URL: http://plwm.sourceforge.net
Source0: http://sourceforge.net/projects/plwm/files/plwm/2.7rc1/PLWM-2.7rc1.tar.gz
BuildArch: noarch
BuildRequires: python
BuildRequires: python-xlib

%description
PLWM is a Python package, containing classes suitable for implementing
a window manager.

%prep
%setup -q -n PLWM-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc COPYING NEWS README
%{python2_sitelib}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7rc1
- Rebuild for Fedora
