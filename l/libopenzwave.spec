Name: libopenzwave
Group: Development/Libraries
Summary: Library to access Z-Wave interfaces
URL:http://code.google.com/p/open-zwave/
License: LGPLv2+
Version: 1.2.919
Release: 9.1
BuildRequires: gcc-c++ make libudev-devel doxygen graphviz
BuildRequires: systemd-devel pkgconfig
BuildRequires: ghostscript-core
Source0: libopenzwave-%{version}.tar.gz

%description
OpenZWave is an open-source, cross-platform library designed to enable anyone to
add support for Z-Wave home-automation devices to their applications, without 
requiring any in depth knowledge of the Z-Wave protocol.

Z-Wave employs a proprietary protocol which the owners, Sigma Designs, have 
chosen not to release into the public domain. There is also no official free 
or low-cost SDK that can be used to develop applications (The ControlThink SDK
is now tied exclusively to their own Z-Wave PC interface). The only way to 
obtain the protocol documentation and sample code is to purchase an expensive 
development kit, and sign a non-disclosure agreement (NDA) preventing the 
release of that knowledge.

OpenZWave was created to fill that gap. We do not have the official 
documentation, have signed no NDA, and are free to develop the library as we 
see fit. Our knowledge comes from existing bodies of open-source code 
(principally the Z-Wave parts of LinuxMCE), and through examining the 
messages sent by Z-Wave devices.

The goal of the project is to make a positive contribution to the Z-Wave 
community by creating a library that supports as much of the Z-Wave 
specification as possible, and that can be used as a "black-box" solution 
by anyone wanting to add Z-Wave to their application. It is NOT our aim 
to publish alternative documentation of the Z-Wave protocol, or to 
attempt to "punish" Sigma Designs for their decision to keep the 
protocol closed.

%package devel
Summary: Open-ZWave header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files needed when you want to compile your own 
applications using openzwave.

%prep
%setup -q 

%build
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
CFLAGS=-Wno-array-bounds VERSION_MAJ=$major_ver VERSION_MIN=$minor_ver VERSION_REV=$revision PREFIX=/usr sysconfdir=%{_sysconfdir}/openzwave/ includedir=%{_includedir} docdir=%{_defaultdocdir}/openzwave-%{version} instlibdir=%{_libdir} make

%install
rm -rf %{buildroot}/*
major_ver=$(echo %{version} | awk -F \. {'print $1'})
minor_ver=$(echo %{version} | awk -F \. {'print $2'})
revision=$(echo %{version} | awk -F \. {'print $3'})
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_defaultdocdir}/openzwave-%{version}/
mkdir -p %{buildroot}/%{_sysconfdir}/
mkdir -p %{buildroot}/%{_includedir}/openzwave/
DESTDIR=%{buildroot} VERSION_MAJ=$major_ver VERSION_MIN=$minor_ver VERSION_REV=$revision PREFIX=/usr sysconfdir=%{_sysconfdir}/openzwave/ includedir=%{_includedir}/openzwave/ docdir=%{_defaultdocdir}/openzwave-%{version} instlibdir=%{_libdir} make install
cp -p INSTALL %{buildroot}/%{_defaultdocdir}/openzwave-%{version}/
cp -pr license %{buildroot}/%{_defaultdocdir}/openzwave-%{version}/
rm %{buildroot}%{_defaultdocdir}/openzwave-%{version}/Doxyfile.in
rm -rf %{buildroot}%{_defaultdocdir}/openzwave-%{version}/html/

%files
%{_defaultdocdir}/openzwave-%{version}
%{_bindir}/MinOZW
%{_libdir}/libopenzwave.so.*
%config(noreplace) %{_sysconfdir}/openzwave/

%files devel
%{_includedir}/openzwave/
%{_libdir}/libopenzwave.so
%{_libdir}/pkgconfig/libopenzwave.pc

%post
/sbin/ldconfig 

%postun
/sbin/ldconfig 

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.919
- Rebuilt for Fedora
* Fri Jun 21 2013 justin@dynam.ac
- Add MultiInstance.patch to handle buggy devices such as Vitrum that
  send wrong commands
* Fri Jun 21 2013 justin@dynam.ac
- Remove debug output from RPM installation commands-
* Fri Jun 21 2013 justin@dynam.ac
- Initial RPM Packages that should work for all Platforms
