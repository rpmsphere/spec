%define __python /usr/bin/python2
%undefine _debugsource_packages
%define __spec_install_post %{nil}

Name:           python-wafo
Version:        0.1.2
Release:        15.1
Summary:        Toolbox for statistical analysis and simulation of random waves and loads
Group:          Development/Languages/Python
License:        GPLv3
URL:            https://pypi.python.org/pypi/wafo/0.1.2
Source0:        https://pypi.python.org/packages/source/w/wafo/wafo-0.1.2.zip
BuildArch:      noarch
BuildRequires:  python3-devel unzip
BuildRequires:  atlas-devel suitesparse-devel
BuildRequires:  numpy python3-scipy
Requires:       numpy scipy

%description
Wave Analysis for Fatigue and Oceanography (WAFO) is a toolbox of Python
routines for statistical analysis and simulation of random waves and random
loads. It contain tools for:

Fatigue Analysis
----------------
 - Fatigue life prediction for random loads
 - Theoretical density of rainflow cycles

Sea modelling
-------------
 - Simulation of linear and non-linear Gaussian waves
 - Estimation of seamodels (spectrums)
 - Joint wave height, wave steepness, wave period distributions

Statistics
------------
 - Extreme value analysis
 - Kernel density estimation
 - Hidden markov models

%prep
%setup -q -n wafo-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --prefix=/usr --root $RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
* Sat Feb 26 2011 scorot@gtt.fr - 0.1.2
- initial package
