%define pyname fwrap

Name:           python2-%{pyname}
Version:        0.1.1
Release:        8.1
Summary:        Wraps Fortran code in C, Cython and Python
License:        BSD
URL:            http://sourceforge.net/projects/fwrap/files/
Group:          Development/Libraries/Python
Source0:        %{pyname}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       numpy

%description
Fwrap wraps Fortran code in C, Cython and Python. It focuses on Fortran 90 and
95, and will work with Fortran 77 so long as you limit yourself to "sane"
Fortran 77.

Fwrap is in beta-stage until otherwise indicated. All command line options and
public APIs are subject to change.

%prep
%setup -q -n %{pyname}-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt USAGE.txt
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
* Sun Feb  6 2011 ocefpaf@yahoo.com.br
- back to version 0.1.1
* Sun Jan 23 2011 ocefpaf@yahoo.com.br
- updated to revision 417 (version 0.2.0)
* Sun Dec 19 2010 ocefpaf@yahoo.com.br
- First OpenSuse release
