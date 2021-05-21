Name:           libsbml
BuildRequires:  gcc-c++, make
BuildRequires:  libxml2-devel, zlib-devel
BuildRequires:  bzip2-devel
Requires:       bzip2-libs
License:        LGPL
URL:            http://sbml.org/Software/libSBML
Group:          Development/Libraries/Other
Summary:        An API Library for Systems Biology Markup Language
Version:        5.11.4
Release:        3.1
Source: http://sourceforge.net/projects/sbml/files/%{name}/%{version}/stable/libSBML-%{version}-core-plus-packages-src.tar.gz

%description
LibSBML is an open-source programming library designed to help you
read, write, manipulate, translate, and validate SBML files and data
streams. It is not an application itself (though it does come with
example programs), but rather a library you can embed in your own
applications.

LibSBML understands SBML Level 3 Version 1 and before,
as well as the draft SBML Level 2 Layout proposal by Gauges, Rost,
Sahle and Wegner. It's written in ISO C and C++ but can also be
used from Csharp, Java, MATLAB, Octave, Perl, Python, and Ruby.

Author(s):
  Sarah Keating,  
  Akiya Jouraku, 
  Frank Bergmann, 
  Ben Bornstein, 
  Michael Hucka

Contact: 
  LibSBML Team <libsbml-team@caltech.edu>

%package devel
Summary: An API Library for SBML
Group: Development/Libraries/Other
Requires: %{name}

%description devel
This package includes the header files as well as the static library. 

%prep
%setup -q -n libSBML-%{version}-Source

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%make_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%{_libdir}/libsbml.la
%{_includedir}/*
%{_libdir}/libsbml.so
%{_libdir}/libsbml*.a
%{_libdir}/pkgconfig/libsbml.pc

%files
%doc AUTHORS.txt COPYING.html COPYING.txt LICENSE.html LICENSE.txt README.txt
%{_libdir}/libsbml.so.*

%changelog
* Wed Apr 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 5.11.4
- Rebuilt for Fedora
* Wed Oct 26 2011 fbergman@u.washington.edu
- initial release, version 5.2.0
