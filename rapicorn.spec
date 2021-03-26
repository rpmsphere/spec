%define _disable_ld_no_undefined 1

%define api_version	1307
%define major		0
%define libname		rapicorn-libs
%define develname	%{name}-devel

%define custom_dsp 0
%{?dsp_device: %global custom_dsp 1}

%define custom_midi 0
%{?midi_device: %global custom_midi 1}

Name:		rapicorn
Summary:	Rapid development toolkit
Version:	17.0.0
Release:	1
Source0:	http://rapicorn.org/dist/%{name}/%{name}-%{version}.tar.xz
URL:		https://testbit.eu/wiki/Rapicorn_Home
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
BuildRequires:	libxml2-utils
BuildRequires:	readline-devel

Requires:	%{libname} = %{version}-%{release}

%description
Rapicorn is a toolkit for rapid development of graphical user interfaces using 
C++ and Python. Rapicorn is developed with the aim to significantly improve 
developer efficiency and user experience. 

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
License:	LGPLv2+

%description -n %{libname}
BEAST (the BEdevilled Audio System) is a GTK+/GNOME-based frontend to
BSE (the Bedevilled Sound Engine). BSE comes with the abilities to
load/store songs and synthesis networks (in .bse files), play them
modify them, etc. BEAST provides the necessary GUI to make actual
use of BSE. Synthesis filters (BseSources) are implemented in shared
library modules, and get loaded on demand.

You must install this library before running %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group: 		Development/C
License:	LGPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
export CFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD -fPIC"
export CXXFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD"
export LIBS="-lrt -lcairo"
%configure
%make_build

%install
%make_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README AUTHORS COPYING* NEWS
%{_docdir}/rapicorn%{api_version}
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/aidacc-%{api_version}
%{py_puresitedir}/Aida%{api_version}
%{py_puresitedir}/Rapicorn%{api_version}

%files -n %{libname}
%{_libdir}/librapicorn%{api_version}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Wed Apr 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Mar 18 2014 Crispin Boylan <crisb@mandriva.org> 13.07.0-1
+ Revision: 8742074
- BR readline
