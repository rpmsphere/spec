Summary:	GTK+ bindings for applications built using PHP
Name:		php-gtk2
Version:	2.0.1
Release:	3
License:	LGPLv2+
Group:		Development/Languages
URL:		http://gtk.php.net/
Source0:	http://gtk.php.net/distributions/php-gtk.tar.gz
BuildRequires:	php-devel, libglade2-devel >= 2.4.0
BuildRequires:	php-cairo-devel
Requires:	php-cli, libglade2 >= 2.4.0

%description
PHP-GTK is an extension for PHP programming language that implements
language bindings for the GTK+ toolkit. It provides an object-oriented
interface to GTK+ classes and functions and greatly simplifies writing
client side cross-platform GUI applications.

%prep
%setup -q -n php-gtk

%build
./buildconf
#sed -i -e 's/gen_gtk-1\.c//g' configure
./configure 
make

%install
%{__rm} -rf %{buildroot}
%{__make} INSTALL_ROOT=%{buildroot} install

install -d %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/php-gtk2.ini << EOF
[php-gtk]
php-gtk.codepage = UTF-8
;php-gtk.extensions = php_gtk2.so
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/php/modules/php_gtk2.so
%doc AUTHORS ChangeLog COPYING.LIB NEWS README README.KNOWN-ISSUES TODO2
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Thu Dec  3 2009 Feather Mountain <john@ossii.com.tw> 2.0.1-3.ossii
- Update to 2009-12-3

* Tue Jul 29 2008 Wei-Lun Chao <bluebat@member.fsf.org> 2.0.1-2.ossii
- Minor tweaks

* Thu Jul 24 2008 Wind Yan <yc.yan@ossii.com.tw> 2.0.1-1.ossii
- rebuilt for FOS

* Mon Mar  3 2008 Paul Howarth <paul@city-fan.org> 2.0.0-1
- Update to PHP-GTK 2.0.0
- Build against regular php-devel, no need for private PHP any longer
- Tarball includes sanely-named directory now
- Update build requirements for GTK2 stack and PHP 5
- Include patch to support building against older PHP versions

* Fri Jan  4 2008 Paul Howarth <paul@city-fan.org> 1.0.2-3
- Rebuild against PHP 4.4.8
- Clarify license as GNU Lesser Public License, version 2.1 or later
- Use system libtool to avoid bogus rpaths on 64-bit architectures

* Thu Apr 13 2006 Paul Howarth <paul@city-fan.org> 1.0.2-2
- Rename package to php4-pcntl-gtk to match renamed underlying php package
- Remove buildroot unconditionally in %%clean and %%install
- Honour %%{optflags}
- Define %%__id_u macro in a more portable way
- Add % tag for distribution-specific build identification
- Specify libdir for configure (pacify rpmlint a bit)
- Remove explicit library dependencies that rpm will pick up automatically

* Mon Jul 18 2005 Paul Howarth <paul@city-fan.org> 1.0.2-1
- Update to 1.0.2
- Ensure all directories are owned properly
- Tarball directory stupidly named php_gtk instead of php-gtk

* Mon Apr 11 2005 Paul Howarth <paul@city-fan.org> 1.0.1-3
- Add build requirement of autoconf

* Thu Sep 30 2004 Paul Howarth <paul@city-fan.org> 1.0.1-2
- Do not do parallel make on SMP boxen; Makefile does not support parallel
  builds properly

* Wed Aug 11 2004 Paul Howarth <paul@city-fan.org> 1.0.1-1
- Update to 1.0.1
- Build now works with automake 1.8.3 and does not require buildconf/aclocal/buildconf
  routine, but does require PHP >= 4.3.0

* Tue Jul 20 2004 Paul Howarth <paul@city-fan.org> 1.0.0-1
- Rebuild against php-pcntl 4.3.8

* Sat Jun 19 2004 James Cameron <james.cameron@hp.com>
- rpm build on debian

* Wed Jun 16 2004 Paul Howarth <paul@city-fan.org> 1.0.0-0.1
- Don't disable anything in configure, makes the package more generally useful.

* Tue Jun 15 2004 Paul Howarth <paul@city-fan.org> 1.0.0-0
- Initial RPM build.
