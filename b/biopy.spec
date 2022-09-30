%undefine _debugsource_packages

Name:          biopy
Version:       0.1.5
Release:       10.1
Summary:       A small collection of bioinformatic scripts
Group:         System/Libraries/Python
URL:           http://code.google.com/p/biopy/
Source:        http://biopy.googlecode.com/files/%{name}-%{version}.tar.gz
License:       GPLv3
BuildRequires: gcc-c++, python2-devel
BuildRequires: python2-numpy, lapack-devel, atlas

%description
This is not a high-duty, high-performance library. It is a set of functions for
exploration and development of phylogenetics. Useful for generating simulated
data or performing off-line analysis as well. Some parts are specific to *BEAST
and BEAST.

This code should work with Python 2.5 and up. For full functionality the
following packages are requited: numpy, scipy, lxml and biopython.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/*
%{python2_sitearch}/*.so
%{python2_sitearch}/biopy*

%changelog
* Mon Jul 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuilt for Fedora
