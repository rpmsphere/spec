Name:          libaosd
Version:       0.2.7
Release:       4.1
Summary:       An advanced on screen display (OSD) library
Group:         System/Libraries
URL:           http://www.atheme.org/project/libaosd
Source:        http://distfiles.atheme.org/libaosd-%{version}.tgz
License:       MIT
BuildRequires: libpng-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
libaosd is an advanced on screen display (OSD) library, which uses Cairo
to create high quality rendered graphics to be overlaid on top of the screen.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
libaosd is an advanced on screen display (OSD) library, which uses Cairo
to create high quality rendered graphics to be overlaid on top of the screen.

This package contains static libraries and header files need for development.

%package -n aosd_cat
Group:         Applications/Text
Summary:       On-screen display tool
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n aosd_cat
aosd_cat is an advanced on-screen display tool based on libaosd.
It can be used for OSD-style notifications in shell scripts.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc LICENSE TODO

%files devel
%defattr(-,root,root)
%{_includedir}/libaosd
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n aosd_cat
%defattr(-,root,root)
%{_bindir}/aosd_cat
%{_mandir}/man1/aosd_cat.1.*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.7
- Rebuild for Fedora

* Tue Sep 28 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.2.7-1mamba
- package created by autospec
