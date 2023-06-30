%undefine _debugsource_packages

Name:          libjackasyn
Version:       0.13
Release:       8.1
Summary:       A wrapper library for JACK system
Group:         System/Libraries
URL:           https://gige.xdv.org/libjackasyn/
Source:        https://gige.xdv.org/libjackasyn/download/libjackasyn-%{version}.tar.gz
License:       GPL
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel

%description
libjackasyn is a library that allows you to run any Linux sound program
made for the OSS system as a JACK client.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
libjackasyn is a library that allows you to run any Linux sound program
made for the OSS system as a JACK client.

This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's|-shared|-shared -Wl,--allow-multiple-definition|' Makefile.in

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
chmod 755 $RPM_BUILD_ROOT/usr/lib/*
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/jacklaunch
%{_libdir}/*.so.*
%doc AUTHORS COPYING README TODO

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13
- Rebuilt for Fedora
* Thu Aug 14 2008 gil <puntogil@libero.it> 0.13-1mamba
- package created by autospec
