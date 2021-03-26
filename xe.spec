Name:			xe
License:		GPL
Version:		0.1
Release:		2.1
Group:			Applications/System
Summary:		eXtract Everything
URL:			http://gaugusch.at/xe/
Source:			http://gaugusch.at/download/%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
BuildArch:		noarch

%description
xe (eXtract Everything) is a small utility to extract any given file.

Authors:
--------
    Markus Gaugusch <xe@gaugusch.at>

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README LICENSE CHANGELOG

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora

* Wed Jul 17 2002 - xe@gaugusch.at
- first version as RPM
