%define ver_data 1.36.0
%define ver_main 2.30.1
%define plugindir %(gimptool-2.0 --gimpplugindir 2> /dev/null)
%define _disable_lto 1
%define _disable_rebuild_configure 1
%define __noautoprov 'libsane\\.so\\.1(.*)'
%undefine _missing_build_ids_terminate_build

Name:           iscan
Version:        %{ver_main}
Release:        25
Summary:        EPSON Image Scan! front-end for scanners and all-in-ones
License:        GPL-2.0 and AVASYSPL
Group:          System/Kernel and hardware
URL:            http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
Source0:        https://download3.ebz.epson.net/dsc/f/03/00/03/61/59/a3f8b8d60e8702a1c5bf3977d018cc2336e308a8/%{name}_%{version}-1.tar.gz
Source1:        https://download3.ebz.epson.net/dsc/f/03/00/03/61/59/646738a219f7354bf3268897385f6ce48c0776bf/%{name}-data_%{ver_data}-1.tar.gz
Source2:        epkowa.conf
# PATCH-FIX-UPSTREAM libpng15.patch (export from arch) -- Build iscan against libpng15 by giovanni
Patch0:         libpng15.patch
BuildRequires:  gettext
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libstdc++-devel
BuildRequires:  systemd
BuildRequires:  pkgconfig(gimp-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(udev)
Requires:       %{name}-data
Conflicts:	sane-backends-iscan

%description
Image Scan! is a graphical scanner utility for people that do not need all
the bells and whistles provided by several of the other utilities out there
(xsane, QuiteInsane, Kooka).

At the moment it only supports SEIKO EPSON scanners and all-in-ones.
However, the scanner driver it provides can be used by any other SANE
standard compliant scanner utility.

Note that several scanners require a non-free plugin before they can be
used with this software.

%package data
Version:	%{ver_data}
Summary:	Image Scan! for Linux data files
Group:		System/Kernel and hardware
Requires:	libxslt
BuildArch:	noarch

%description data
Provides the necessary support files for Image Scan! for Linux, including
device information and policy file generation logic.

Image Scan! for Linux will not function without this package.

%prep
%setup -q -n %{name}-%{ver_main}
%setup -q -D -T -a 1 -n %{name}-%{ver_main}
%patch0

# Fix for CXX ABI different than 1002 (export from arch)
rm non-free/libesmod-i386.so
sed -i '/libesmod-i386.so/d' non-free/checksums.md5 non-free/Makefile.*
ln -s libesmod-i386.c2.so non-free/libesmod-i386.so
ln -s libesmod-x86_64.c2.so non-free/libesmod-x86_64.so

sed -i 's|div_t index = div (i|div_t index = div (int(i)|' lib/jpegstream.cc

%build
# Build iscan
export LDFLAGS="${LDFLAGS} -ldl -lpng16"
%configure \
  --sbindir=%{_bindir} \
  --enable-dependency-reduction \
  --enable-frontend \
  --enable-jpeg \
  --enable-tiff \
  --enable-png \
  --enable-gimp \
  --enable-static=no

make

# Build data
cd %{name}-data-%{ver_data}
%configure --libdir="%{_prefix}/lib"
make
make %{name}-data.hwdb

%install
# iscan: install files
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}%{plugindir}/plug-ins
ln -s %{_bindir}/iscan %{buildroot}%{_libdir}/gimp/2.0/plug-ins/iscan
install -D -m 0644 backend/epkowa.conf %{buildroot}%{_sysconfdir}/sane.d/epkowa.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sane.d/dll.d/epkowa.conf

find %{buildroot} \( -name \*.la -o -name \*.so  \) -exec rm {} \;

%find_lang %{name}

# data: install files
cd %{name}-data-%{ver_data}
make DESTDIR=%{buildroot} install %{?_smp_mflags}

install -D -m 0644 %{name}-data.hwdb %{buildroot}/%{_udevhwdbdir}/%{name}-data.hwdb

%files -f %{name}.lang
%doc NEWS README AUTHORS COPYING
%doc non-free/AVASYSPL.en.txt
%doc doc/xinetd.sane
%dir %{_sysconfdir}/sane.d
%dir %{_sysconfdir}/sane.d/dll.d
%config %{_sysconfdir}/sane.d/epkowa.conf
%config %{_sysconfdir}/sane.d/dll.d/epkowa.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-registry
%{_libdir}/libesmod.so*
%{_libdir}/sane/libsane-epkowa.so*
%{_libdir}/gimp/2.0/plug-ins/iscan
%{_mandir}/man1/iscan.1.*
%{_mandir}/man5/sane-epkowa.5.*
%{_mandir}/man8/iscan-registry.8.*

%files data
%doc %{name}-data-%{ver_data}/COPYING
%doc %{name}-data-%{ver_data}/NEWS
%doc %{name}-data-%{ver_data}/KNOWN-PROBLEMS
%doc %{name}-data-%{ver_data}/SUPPORTED-DEVICES
%{_prefix}/lib/iscan-data
%{_datadir}/iscan-data
%{_udevhwdbdir}/%{name}-data.hwdb

%changelog
* Tue Jun 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.30.1
- Rebuild for Fedora
* Mon Oct 05 2015 tpg (Tomasz Pawe³ Gajc) <tpgxyz@gmail.com> 2.30.1-4
- (95cf933) do not provide libsane.so.1
