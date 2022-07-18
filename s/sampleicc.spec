%global __os_install_post %{nil}

Version:        1.6.6
Release:        11.1
Source:         SampleICC-1.6.6.tar.gz
Summary:        Color Management System
Name:           sampleicc
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            http://sourceforge.net/projects/sampleicc/
BuildRequires:  doxygen gcc-c++ gettext graphviz libjpeg-devel libpng-devel libtiff-devel libxml2-devel pkgconfig
BuildRequires:	netpbm
BuildRequires:	ghostscript-core

%package -n lib%{name}
Summary:        Colour Management System Libraries
Group:          Development/Libraries/Other

%package -n lib%{name}-devel
Summary:        Headers, Configuration and static Libs + Documentation
Group:          Development/Libraries/Other
Requires:       lib%{name} = %{version}

%description
SampleICC provides an open source platform independent C++ library for reading,
writing, manipulating, and applying ICC profiles along with applications that
make use of this library.

%description -n lib%{name}
SampleICC provides an open source platform independent C++ library for reading,
writing, manipulating, and applying ICC profiles along with applications that
make use of this library.

%description -n lib%{name}-devel
Header files, libraries and documentation for development of Color Management
applications.

%prep
%setup -n SampleICC-%{version}

%build
%configure

%install
make %{_smp_mflags}
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_libdir}/lib*.la

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*

%files -n lib%{name}
%{_libdir}/libSampleICC.so.*
%{_libdir}/libICC_utils.so.*

%files -n lib%{name}-devel
%{_libdir}/libSampleICC.so
%{_includedir}/SampleICC
%{_libdir}/pkgconfig/*
%{_libdir}/libSampleICC.a
%{_libdir}/libICC_utils.a
%{_libdir}/libICC_utils.so

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.6
- Rebuilt for Fedora
* Thu Nov  1 2012 p.drouand@gmail.com
- Remove unused files
* Wed May  9 2012 ku.b@gmx.de
- more spec tweaks
* Tue Apr  3 2012 ku.b@gmx.de
- minor spec tweaks
* Tue Apr  3 2012 ku.b@gmx.de
- add copyright to spec file
* Thu Jan 19 2012 ku.b@gmx.de
- update to 1.6.6
- add changes file
* Tue Aug 24 2010 ku.b@gmx.de>
- initial specfile'ification
