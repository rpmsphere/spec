Name:         openh264
Summary:      Open Source H.264 Codec
URL:          http://www.openh264.org/
Group:        System/Libraries
License:      BSD
Version:      1.6.0
Release:      4.1
Source0:      %{name}-%{version}.tar.gz
BuildRequires: nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
make %{_smp_mflags} PREFIX=/usr

%install
%make_install PREFIX=/usr
%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc README.md LICENSE CONTRIBUTORS
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/wels
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Jul 12 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.0
- Rebuilt for Fedora
