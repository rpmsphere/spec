Name:           php-fineart
Version:        0.2
Release:        2
Summary:        Fineart Handwriting Writepanel's php extension.
Group:          System/Internationalization
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	php-devel,fineart-devel
Requires:  	fineart

%description
This project is fineart php extension.

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/php/modules/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/php.d/
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

%__cp fineart.so $RPM_BUILD_ROOT%{_libdir}/php/modules/fineart.so
%__cp fineart.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.d/fineart.ini
%__cp API README demo.php demo.sh $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{_libdir}/php/modules/fineart.so
%{_sysconfdir}/php.d/fineart.ini
%{_defaultdocdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Feb 01 2010 Feather Mountain <john@ossii.com.tw> 0.2-2.ossii
- Fix SPEC

* Wed Nov 25 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Change wFlag for new version fineart.
- Support Standard CJK.

* Tue Nov 17 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII
