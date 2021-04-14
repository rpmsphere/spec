Name:           cfortran
Version:        4.4
Release:        3.1
Summary:        Interfacing C or C++ and FORTRAN
Group:          Development/Libraries
License:        freeware
URL:		http://www-zeus.desy.de/~burow/cfortran/
Source0: 	http://www-zeus.desy.de/~burow/cfortran/cfortran.h
Source1: 	http://www-zeus.desy.de/~burow/cfortran/cfortran.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
cfortran.h is an easy-to-use powerful bridge between C and FORTRAN.
It provides a transparent, machine independent interface between
C and FORTRAN routines and global data.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} ${RPM_BUILD_ROOT}%{_includedir}/cfortran.h
install -Dm644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/doc/%{name}-%{version}/cfortran.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_includedir}/cfortran.h
%{_datadir}/doc/%{name}-%{version}/cfortran.html

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.4
- Rebuilt for Fedora
