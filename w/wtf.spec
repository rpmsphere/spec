Summary:	Translates common Internet acronyms
Name:		wtf
Version:	20111107
Release:	4.1
License:	BSD
Group:		Productivity/Other
URL:		http://netbsd.org/
Source0:    http://download.goodking.org/downloads/%{name}-%{version}.tar.gz	
Patch0:     %{name}.suse.diff.gz
Patch1:     %{name}.6.suse.diff.gz
BuildArch:  noarch
Buildroot: 	%{_tmppath}/%{name}-%{version}-root

%description
Wtf is little shell script taken from NetBSD's CVS repository which
translates acronyms. 

%prep 
%setup -q

%patch0 -p0
%patch1 -p0

%build
sed -i -e "s:/usr/share/misc/:%{_datadir}/%{name}/:" wtf

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} -D -m 755 wtf $RPM_BUILD_ROOT/%{_bindir}
%{__mkdir} -p $RPM_BUILD_ROOT/%{_mandir}/man6
%{__install} -D -m 644 wtf.6 $RPM_BUILD_ROOT/%{_mandir}/man6
%{__mkdir} -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} -D -m 644 acronyms $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} -D -m 644 acronyms.comp $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/%{name}

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20111107
- Rebuild for Fedora
