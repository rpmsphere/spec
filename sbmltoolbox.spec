Name: sbmltoolbox
Version: 4.1.0
Release: 7.1
Summary: SBML toolbox for octave and matlab
License: LGPLv2
Group: Development/Tools
URL: http://sbml.org/Software/SBMLToolbox
Source0: http://sourceforge.net/projects/sbml/files/SBMLToolbox/%{version}/SBMLToolbox-%{version}.zip
BuildArch: noarch

%description
The SBMLToolbox provides a set of basic functions for reading, writing,
manipulating, and simulating SBML (System Biology Meta Language)
models. It is a free Open Source package on top of the libSBML with
full compatibility to work with MATLAB and Octave alike and share models
between the two systems.

The toolbox is not a complete turn key solution for Systems Biology.
It has its emphasis on easing the handling of SBML data and serves
as a starting point for users and developers to establish their own
methods.

%prep
%setup -q -n SBMLToolbox-%{version}

%build

%install
install -d %{buildroot}%{_datadir}/SBMLToolbox
cp -a toolbox/* %{buildroot}%{_datadir}/SBMLToolbox

%files
%doc *.txt docs/*
%{_datadir}/SBMLToolbox

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.0
- Rebuild for Fedora
