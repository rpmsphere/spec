%define pkg  pear2rpm

Summary:     A Pear (PHP) module packager
Name:        php-%{pkg}
Version:     1.4
Release:     5.1
License:     GPL
Group:       Development/Tools
Source0:     %{pkg}-%{version}.tar.gz
Patch0:      %{pkg}-1.4-updates.patch
Patch1:      %{pkg}-1.4-rpmfix.patch
URL:         https://cvs.mandriva.com/cgi-bin/viewcvs.cgi/soft/%{pkg}/
Buildroot:   /var/tmp/%{name}-root
Requires:    php php-pear
BuildArch:   noarch

%description
This script generates a RPM package from a Pear (PHP) module.
It uses the standard RPM file structure and creates a spec
file. The script can operate on local archives and Pear module
names.

%prep
%setup -q -n %{pkg}-%{version}
%patch0 -p1
#patch1 -p0

%build

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -m 0755 %{pkg}.php ${RPM_BUILD_ROOT}%{_bindir}/%{pkg}

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root) 
%{_bindir}/*

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
* Fri Jun 01 2007 peter.pramberger@member.fsf.org 1.4-4
- added support for package requirements addition/exclusion
- make full package build default
* Mon Jan 30 2006 peter.pramberger@member.fsf.org
- created

