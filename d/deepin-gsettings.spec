%undefine _debugsource_packages
Name:           deepin-gsettings
Version:        0.21
Release:        3.1
Summary:        Gsettings for Linux Deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{name}-master.zip
BuildRequires:  python2-devel, glib2-devel, python-setuptools

%description
Gsettings for Linux Deepin.

%prep
%setup -qn %{name}-master

%build
export CFLAGS+=" -Wno-incompatible-pointer-types "
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%doc README
%{python2_sitearch}/*

%changelog
* Wed Aug 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21
- Rebuilt for Fedora
* Mon Sep 28 2015 Derek Dai
- Initial package
