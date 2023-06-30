Summary: Class library for High Energy Physics
Name: clhep
Version: 2.2.0.8
Release: 4.1
License: distributable
Group: Development/Libraries
URL: https://proj-clhep.web.cern.ch/proj-clhep/
Source: https://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-%{version}.tgz
BuildRequires: binutils, gcc-c++, autoconf, automake, make
Provides: CLHEP

%description
The CLHEP project was proposed by Leif Lönnblad at CHEP 92. It is intended
to be a set of HEP-specific foundation and utility classes such as random
generators, physics vectors, geometry and linear algebra.

%package devel
Summary: Development files for CLHEP
Group: Development/Libraries
Requires: %{name} = %{version}
Provides: CLHEP-devel

%description devel
Install this package to develop software based on CLHEP.

%prep
%setup -q -n %{version}/CLHEP
#sed -i -e 's/^g++)/*g++)/g' -e 's/^icc)/icc|icpc)/g' -e '/AM_CXXFLAGS=/s/-O //g' configure.ac */configure.ac
#sed -i -e 's/: %\.cc/: %\.cc \$(shareddir)/' -e 's/all-local: \$(shareddir)/all-local: /' Makefile.am */Makefile.am */*/Makefile.am

%build
./bootstrap
%configure \
    --includedir="%{_includedir}/CLHEP/" \
    --disable-dependency-tracking \
    --enable-exceptions \
    --disable-static

# if you parallelize the make, badness happens
%{__make} LDFLAGS+=-lc

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

pushd $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} -f libCLHEP-g++.%{version}.a libCLHEP.a
popd

mkdir doc/
for dir in */doc; do
    %{__rm} -rf $dir/CVS
    %{__mv} -f $dir doc/$(dirname $dir)
done

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README
%{_libdir}/libCLHEP*.so

%files devel
%doc doc/*
%{_bindir}/*
%{_includedir}/CLHEP
%{_libdir}/libCLHEP*.a

%changelog
* Fri Jan 08 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0.8
- Rebuilt for Fedora
* Fri Mar 05 2010 Steve Huff <shuff@vecna.org> - 2.0.4.5-1 - 8792/dag
- Updated to release 2.0.4.5.
- Fixed typo in doc cleanup script.
- Split off clhep-devel.
* Mon Jun 13 2005 Wei-Lun <chaoweilun@pcmail.com.tw> - 1.8.2.1-1
- Initial spec file created.
