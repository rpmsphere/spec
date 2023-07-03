Name:           php-screw
Version:        1.5
Release:        5.1
Summary:        A PHP script encryption tool
Group:          Development/Tools
License:        BSD
URL:            https://sourceforge.net/projects/php-screw/
Source0:        https://sourceforge.net/projects/php-screw/files/%{name}/%{version}/php_screw-%{version}.tar.gz
BuildRequires:  php-devel
BuildRequires:  automake
Requires:  	php

%description
PHP Screw is a PHP script encryption tool. When you are developing a
commercial package using PHP, the script can be distributed as encrypted
up until just before execution, preserving your intellectual property.

%prep
%setup -q -n php_screw-%{version}
sed -i 's/CG(extended_info) = 1/CG(compiler_options) |= ZEND_COMPILE_EXTENDED_INFO/' php_screw.c
sed -i 's/62/'$RANDOM'/' my_screw.h
sed -i 's|PHP_EXTENSION(php_screw,|PHP_NEW_EXTENSION(php_screw, php_screw.c,|' config.m4
sed -i -e '88d' -e 's|TSRMLS_.C||' -e 's|TSRMLS_C)|)|' php_screw.c

%build
phpize
./configure --prefix=/usr
make
make -C tools

%install
install -Dm755 modules/php_screw.so $RPM_BUILD_ROOT%{_libdir}/php/modules/php_screw.so
install -Dm755 tools/screw $RPM_BUILD_ROOT%{_bindir}/screw

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.*
%{_bindir}/screw
%{_libdir}/php/modules/php_screw.so

%changelog
* Tue Dec 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
