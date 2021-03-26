Name:          sablotron
Version:       1.0.3
Release:       6.1
Summary:       A fast, compact and portable XML toolkit
Group:         System/Libraries
URL:           http://www.gingerall.org/sablotron.html
Source:        http://download-1.gingerall.cz/download/sablot/Sablot-%{version}.tar.gz
License:       GPL
BuildRequires: gcc-c++
BuildRequires: expat-devel >= 1.95.6

%description
Sablotron is a fast, compact and portable XML toolkit implementing XSLT 1.0,
DOM Level2 and XPath 1.0. Sablotron is an open project; other users and
developers are encouraged to use it or to help us testing or improving it.

The goal of this project is to create a lightweight, reliable and fast XML
library processor conforming to the W3C specification, which is available
for public and can be used as a base for multi-platform XML applications.

%package devel
Summary:       Devel package for libsablotron
Group:         Development/Languages
Requires:      %{name} == %{version}

%description devel
Sablotron is a fast, compact and portable XML toolkit implementing XSLT 1.0,
DOM Level2 and XPath 1.0. Sablotron is an open project; other users and
developers are encouraged to use it or to help us testing or improving it.

The goal of this project is to create a lightweight, reliable and fast XML
library processor conforming to the W3C specification, which is available
for public and can be used as a base for multi-platform XML applications.

This is the devel package.

%prep
%setup -q -n Sablot-%{version}

%build
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/sabcmd
%{_libdir}/libsablot.so.*
%{_mandir}/man1/sabcmd.1.gz

%files devel
%{_bindir}/sablot-config
%{_libdir}/libsablot.a
%{_libdir}/libsablot.la
%{_libdir}/libsablot.so
%{_includedir}/*.h
%{_docdir}/html/*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuild for Fedora
* Tue May 29 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.3-1mamba
- update to 1.0.3
* Thu Dec 18 2003 Silvan Calarco <silvan.calarco@qilinux.it> 1.0.1-1qilnx
- fist build
