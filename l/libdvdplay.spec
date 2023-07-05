Name:          libdvdplay
Version:       1.0.1
Release:       5.1
Summary:       Library designed for DVD navigation
Group:         System/Libraries
URL:           https://developers.videolan.org/libdvdplay/
Source:        https://download.videolan.org/pub/libdvdplay/%{version}/libdvdplay-%{version}.tar.bz2
License:       GPL
BuildRequires: libdvdread-devel

%description
A simple library designed for DVD navigation. It is based on libdvdread
and optionally libdvdcss.

%package devel
Summary:       Development files from the libdvdplay DVD navigation library
Group:         Development/Libraries
Requires:      %{name} = %{version}

%description devel
A simple library designed for DVD navigation. It is based on libdvdread
and optionally libdvdcss.

You will need to install these development files if you intend to rebuild
programs that use libdvdplay.

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
%{_libdir}/%{name}.so.*
%doc AUTHORS COPYING ChangeLog README

%files devel
%dir %{_includedir}/dvdplay
%{_includedir}/dvdplay/*.h
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora

* Mon May 26 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-5mamba
- rebuilt against libdvdread 4.1.2

* Fri Apr 11 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.1-4mamba
- specfile updates

* Wed Jun 29 2005 Davide Madrisan <davide.madrisan@qilinux.it> 1.0.1-3qilnx
- fixed package group
- use rpm macros for building/installing
- own %{_includedir}/dvdplay

* Fri Jun 10 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 1.0.1-2qilnx
- rebuild and moved from devel-contrib repository to devel repository

* Fri Jun 10 2005 Matteo Bernasconi <voyagernm@virgilio.it> 1.0.1-1qilnx
- first build
