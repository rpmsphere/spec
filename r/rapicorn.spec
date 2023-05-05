%define _disable_ld_no_undefined 1

Name:		rapicorn
Summary:	Rapid development toolkit
Version:	17.0.0
Release:	1
Source0:	http://rapicorn.org/dist/%{name}/%{name}-%{version}.tar.xz
URL:		https://github.com/tim-janik/rapicorn
License:	GPLv2+
Group:		Sound
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(python)
BuildRequires:	intltool
BuildRequires:	bison
BuildRequires:	flex
#BuildRequires:	libxml2-utils
BuildRequires:	readline-devel

%description
Rapicorn is a toolkit for rapid development of graphical user interfaces using 
C++ and Python. Rapicorn is developed with the aim to significantly improve 
developer efficiency and user experience. 

%package devel
Summary:	Header files and static libraries from %{name}
Group: 		Development/C
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
sed -i 's|html -S|html|' Makefile.*
sed -i '1i #include <functional>' rcore/aidasignal.hh
sed -i 's|ansi-definitions ansi-prototypes ||' ui/sinfex.l
sed -i 's|bison_yylex|flex_yylex|' ui/sinfex.cc

%build
export PYTHON=/usr/bin/python2
export CFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD -fPIC"
export CXXFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD"
export LIBS="-lrt -lcairo"
%configure
%make_build

%install
%make_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_docdir}/%{name}*
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/%{name}*
%{python2_sitelib}/*
%{_libdir}/librapicorn*.so.*

%files devel
%doc ChangeLog
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Sun Dec 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 17.0.0
- Rebuilt for Fedora
* Tue Mar 18 2014 Crispin Boylan <crisb@mandriva.org> 13.07.0-1
+ Revision: 8742074
- BR readline
