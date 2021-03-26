%define rname Cairo
%define modname cairo
%define dir_name %{modname}
%define so_name %{modname}.so
%define ini_file %{modname}.ini

Summary:	Cairo Graphics Library Extension
Name:		php-%{modname}
Version:	0.1.0
Release:	1
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/Cairo/
Source0:	http://pecl.php.net/get/%{rname}-%{version}.tgz
BuildRequires:	php-devel >= 5.2.0
#BuildRequires:	httpd-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRequires:	cairo-devel >= 1.4

%description
Cairo is a 2D graphics library with support for multiple output devices.
Currently supported output targets include the X Window System, Quartz, Win32,
image buffers, PostScript, PDF, and SVG file output.

%package devel
Summary: Cairo Graphics Library Extension
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header, include files and library definition files for developing applications libraries.

%prep
%setup -q -n %{rname}-%{version}
[ "../package*.xml" != "/" ] && mv ../package*.xml .
sed -i 's|ZEND_ACC_FINAL_CLASS|ZEND_ACC_FINAL|' cairo.c

%build
phpize
%configure

make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/modules
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{so_name} %{buildroot}%{_libdir}/php/modules/

cat > %{buildroot}%{_sysconfdir}/php.d/%{ini_file} << EOF
extension = %{so_name}
EOF

# install include 
mkdir -p $RPM_BUILD_ROOT%{_includedir}/php/ext/%{modname}/
install -m 755 php_cairo_api.h $RPM_BUILD_ROOT%{_includedir}/php/ext/%{modname}/

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%doc CREDITS IGNORED README SYMBOLS TODO package*.xml 
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{ini_file}
%attr(0755,root,root) %{_libdir}/php/modules/%{so_name}

%files devel
%{_includedir}/php/ext/%{modname}/php_cairo_api.h


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Dec 2 2009 Feather Mountain <john@ossii.com.tw> 0.1.0-3.ossii
- build for OSSII

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdv2010.1
+ Revision: 468149
- rebuilt against php-5.3.1

* Sat Oct 03 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2010.0
+ Revision: 452904
- import php-cairo


* Sat Oct 03 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2010.0
- initial Mandriva package
