Name:           php-penpower
Version:        0.1
Release:        2
Summary:        Penpower Handwriting Writepanel's php extension.
Group:          System/Internationalization
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:	php-devel,glib2-devel,penpower-devel
Requires:  	penpower

%description
This project is penpower php extension.

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/php/modules/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/php.d/
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

%__cp penpower.so $RPM_BUILD_ROOT%{_libdir}/php/modules/penpower.so
%__cp penpower.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.d/penpower.ini
%__cp API README demo.php demo.sh $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{_libdir}/php/modules/penpower.so
%{_sysconfdir}/php.d/penpower.ini
%{_defaultdocdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Feb 01 2010 Feather Mountain <john@ossii.com.tw> 0.1-2.ossii
- Fix SPEC

* Wed Sep 16 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII
