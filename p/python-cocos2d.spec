%define __python /usr/bin/python3
%define module cocos2d

Summary:	A framework for building 2D applications
Name:		python-%{module}
Version:	0.6.3
Release:	6.1
License:	BSD
Group:		Development/Libraries
URL:		http://cocos2d.org/
Source0:	cocos-release-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python3
BuildRequires:  python3-setuptools
Requires:	python3-pyglet

%description
cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications.

%prep
%setup -q -n cocos-release-%{version}

%build
python3 setup.py build

%install
%__rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root $RPM_BUILD_ROOT --prefix /usr

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{python3_sitelib}/*

%changelog
* Fri Aug 21 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.3
- Rebuilt for Fedora
