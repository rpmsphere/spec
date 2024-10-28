%undefine _debugsource_packages
Summary: An opensource particles simulation tool box
Name: pyparticles
Version: 0.3.5
Release: 7.1
Source0: https://jaist.dl.sourceforge.net/project/pyparticles/PyParticles-0.3.5/%{name}-%{version}.tar.gz
License: GNU GPL v3
Group: Science
BuildArch: noarch
URL: https://pyparticles.wordpress.com/
Requires: numpy, scipy, python-matplotlib, python2-pyopencl, python2-pyopengl
BuildRequires: python2-devel

%description
PyParticles supports the most popular integrations methods and the most
relevant forces model. It also offer a nice looking OpneGL interface or
at your preference a Matplotlib based GUI. PyParticles as a forces models
implements Gravity, spring, constant force and electrostatic and the user
defined vector field force. As a integrations method it includes Euler,
Midpoint, Runge Kutta, Störmer Verlet and Leap frog.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_mandir}/man1/*

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
