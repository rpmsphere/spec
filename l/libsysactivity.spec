Summary:	Library for retrieving statistics of the system`s activity
Name:		libsysactivity
Version:	0.6.5
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://sourceforge.net/projects/libsysactivity/
Source0:	http://downloads.sourceforge.net/project/%{name}/0.6.x/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	cmake

%description
A lightweight library that retrieves statistics of the system's activity in a
portable and thread safe way. In each OS that it supports it offers the same
API for retrieving the activity of: hard disks, CPUs, memory, processes and
network interfaces.

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%cmake 
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.5
- Rebuilt for Fedora
* Sun May 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.3-1
+ Revision: 800857
- imported package libsysactivity
