Summary:	1C 7.7 SQL handling utility
Name:		unsql
Version:	0.0.3
Release:	3.1
Group:		Utility
License:	GPL
Source:		%{name}_%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	gcc-c++, glibc-devel

%description
Utility to decode 1Cv7.DBA file and to set new values in it from CLI.

%prep
%setup

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuild for Fedora
* Sat Jun 5 2010 TI_Eugene <ti.eugene@gmail.com>
- Initial build for openSUSE Build Service