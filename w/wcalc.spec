%global __os_install_post %{nil}

Summary: 	Analyses and synthesis of transmission lines
Name: 		wcalc
Version: 	1.1
Release: 	3.1
License: 	GPL
Group:          Productivity/Scientific/Electronics
URL: 		http://sourceforge.net/projects/wcalc/
Source0: 	%{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  gtk2-devel >= 2.4

%description
Wcalc is a tool for the analysis and synthesis of transmission line
structures and related components. Wcalc provides the ability to
analyze the electrical parameters of a particular structure based on
the physical dimensions and material parameters. The synthesis portion
calculates the required physical parameters to meet desired electrical
specifications. Wcalc includes several models and places an emphasis
on accuracy. Several frontends provide the user with several options
for its use.

%package devel
Requires:     	gtk2-devel
Summary:      	Analyses and synthesis of transmission lines
License:      	GPL
Group:		Development/Libraries/C and C++
Packager:	Werner Hoch <werner.ho@gmx.de>
Autoreqprov:	on

%description devel
Development files for wcalc.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --disable-gtk1 --enable-gtk2
%{__make}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README ChangeLog AUTHORS TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/mann/*
%dir %{_datadir}/wcalc-%{version}
%{_datadir}/wcalc-%{version}/*
%{_libdir}/libwcalc.so.1*
%dir %{_libexecdir}/cgi-bin
%{_libexecdir}/cgi-bin/*

%files devel
%{_includedir}/*
%{_libdir}/libwcalc.a
%{_libdir}/libwcalc.la
%{_libdir}/libwcalc.so
%{_libdir}/pkgconfig/*

%changelog
* Sun Jan 08 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Sun Nov 15 2009 Werner Hoch <werner.ho@gmx.de> - 1.1
- build fix for openSUSE 11.2
* Sun Mar 01 2009 Werner Hoch <werner.ho@gmx.de> - 1.1
- new version 1.1
* Mon Nov 24 2008 Werner Hoch <werner.ho@gmx.de> - 1.0
- build fixes for factory
* Sat Jun 21 2008 Werner Hoch <werner.ho@gmx.de> - 1.0
- fixed OBS RPMLINT errors
- created devel package
* Sun Mar 23 2008 Werner Hoch <werner.ho@gmx.de>
- new version 1.0 on SF, not sure if it's the same
* Sun Dec  2 2007 Werner Hoch <werner.ho@gmx.de> - 
- Initial build of version 1.0
