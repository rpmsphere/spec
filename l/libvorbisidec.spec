Name:          libvorbisidec
Version:       1.2.0
Release:       4.1
Summary:       A fixed-point version of the Ogg Vorbis decoder
Group:         System/Libraries
URL:           https://wiki.xiph.org/Tremor
# Source package got with:
# svn co https://svn.xiph.org/trunk/Tremor/
Source:        https://svn.xiph.org/trunk/Tremor//libvorbisidec-%{version}.tar.gz
License:       GPL
BuildRequires: libogg-devel

%description
A fixed-point version of the Ogg Vorbis decoder for platforms
that can' do floating point math.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
A fixed-point version of the Ogg Vorbis decoder for platforms
that can' do floating point math.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/*.so.*
%doc COPYING README

%files devel
%{_prefix}/include/tremor/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Sat Dec 11 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.2.0-1mamba
- package created by autospec
