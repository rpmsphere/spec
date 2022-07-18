%global __os_install_post %{nil}

Name: libraspberrypi
Summary: EGL/GLES/OpenVG/etc. libraries for the Raspberry Pi's VideoCore IV
Version: 1.20181212
Release: 1
Group: libs
License: Free Software
URL: https://github.com/raspberrypi/firmware
# git clone https://github.com/raspberrypi/userland.git
Source0: %{name}-%{version}.tar.gz

%description
This package contains implementations of EGL, OpenGL ES, OpenVG, OpenWF
Composition, and others for the Raspberry Pi's VideoCore IV multimedia
processor.

%package devel
Summary: Development files for %{name}

%description devel
Development files for %{name}.

%prep
%setup -q -n userland
sed -i 's|make -j|make -i -j|' buildme

%build
./buildme --native

%install
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo /opt/vc/lib > %{buildroot}%{_sysconfdir}/ld.so.conf.d/00-vc.conf
install -d %{buildroot}%{_bindir}
install -m755 build/bin/* %{buildroot}%{_bindir}
install -d %{buildroot}/opt/vc/lib
cp -a build/lib/* %{buildroot}/opt/vc/lib
install -d %{buildroot}/opt/vc/include
cp -a build/inc/interface/vcos %{buildroot}/opt/vc/include
install -d %{buildroot}%{_libdir}/pkgconfig
cp -a build/native/release/*.pc %{buildroot}%{_libdir}/pkgconfig

%files
%{_sysconfdir}/ld.so.conf.d/00-vc.conf
%{_bindir}/*
%dir /opt/vc
/opt/vc/lib

%files devel
/opt/vc/include
%{_libdir}/pkgconfig

%changelog
* Wed Dec 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.20181212
- Rebuilt for Fedora
