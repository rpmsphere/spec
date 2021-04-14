%define version_iscan_data 1.39.1
%define plugindir %(gimptool-2.0 --gimpplugindir 2> /dev/null)
%undefine _missing_build_ids_terminate_build

Name:           iscan
Version:        2.30.4
Release:        1.170
Summary:        EPSON Image Scan! front-end for scanners and all-in-ones
License:        GPL-2.0 and AVASYSPL
Group:          Hardware/Scanner
Url:            http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
Source0:        http://support.epson.net/linux/src/scanner/iscan/%{name}_%{version}-2.tar.gz
Source1:        http://support.epson.net/linux/src/scanner/iscan/iscan-data_%{version_iscan_data}-2.tar.gz
Source2:        epkowa.conf
# PATCH-FIX-UPSTREAM libpng15.patch (export from arch) -- Build iscan against libpng15 by giovanni
Patch0:         libpng15.patch
Patch1:         jpegstream.patch
# PATCH-FIX-UPSTREAM -- https://bugs.gentoo.org/692708
Patch2:         iscan-2.30.4.2-sscanf.patch
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
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

%description
Image Scan! is a graphical scanner utility for people that do not need all
the bells and whistles provided by several of the other utilities out there
(xsane, QuiteInsane, Kooka).

At the moment it only supports SEIKO EPSON scanners and all-in-ones.
However, the scanner driver it provides can be used by any other SANE
standard compliant scanner utility.

Note that several scanners require a non-free plugin before they can be
used with this software

%package data
Version:        %{version_iscan_data}
Summary:        Image Scan! for Linux data files
Group:          Hardware/Scanner
Requires:       libxslt
BuildArch:      noarch

%description data
Provides the necessary support files for Image Scan! for Linux, including
device information and policy file generation logic.

Image Scan! for Linux will not function without this package.

%prep
%setup -q
%setup -q -D -T -a 1

%patch0
%patch1 -p2
%patch2 -p1

# Fix for CXX ABI different than 1002 (export from arch)
ln -s libesmod-x86_64.c2.so non-free/libesmod-x86_64.so

%build
# Build iscan
export CFLAGS="$(echo %optflags | sed 's/\-fstack-clash-protection//')"
export CXXFLAGS="${CFLAGS}"
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

make  %{?_smp_mflags}

# Build data
cd %{name}-data-%{version_iscan_data}
%configure --libdir="%{_prefix}/lib"
make  %{?_smp_mflags}
make %{?_smp_mflags} %{name}-data.hwdb

%install
# iscan: install files
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}%{plugindir}/plug-ins
ln -s %{_bindir}/iscan %{buildroot}%{_libdir}/gimp/2.0/plug-ins/iscan
install -D -m 0644 backend/epkowa.conf %{buildroot}%{_sysconfdir}/sane.d/epkowa.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sane.d/dll.d/epkowa.conf
install -D -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
find %{buildroot} \( -name \*.la -o -name \*.so  \) -exec rm {} \;
%find_lang %{name}

# data: install files
cd %{name}-data-%{version_iscan_data}
make DESTDIR=%{buildroot} install %{?_smp_mflags}

install -D -m 0644 %{name}-data.hwdb %{buildroot}/%{_udevhwdbdir}/%{name}-data.hwdb

%post
/sbin/ldconfig
%udev_hwdb_update

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
	%udev_hwdb_update
fi

%files -f %{name}.lang
%doc NEWS README AUTHORS COPYING
%doc non-free/COPYING.EPSON.en.txt
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
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/iscan.?.gz
%{_mandir}/man?/sane-epkowa.?.gz
%{_mandir}/man?/iscan-registry.?.gz

%files data
%doc %{name}-data-%{version_iscan_data}/COPYING
%doc %{name}-data-%{version_iscan_data}/NEWS
%doc %{name}-data-%{version_iscan_data}/KNOWN-PROBLEMS
%doc %{name}-data-%{version_iscan_data}/SUPPORTED-DEVICES
#{_libexecdir}/iscan-data
/usr/lib/iscan-data/make-policy-file
%{_datadir}/iscan-data
%{_udevhwdbdir}/%{name}-data.hwdb

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.30.4
- Rebuilt for Fedora
* Thu Oct 31 2019 Alexei Podvalsky <avvissu@yandex.by>
- Update to 2.30.4:
  * update license file
- Add iscan-2.30.4.2-sscanf.patch
* Fri Apr 13 2018 avvissu@yandex.by
- Fix build with gcc >= 5 (add jpegstream.patch)
* Thu Nov  2 2017 avvissu@yandex.by
- Build with gcc4 on Factory
* Thu Jun 25 2015 avvissu@yandex.ru
- Fix build on openSUSE > 13.2:
  * create symbolic links on libesmod*.c2
* Wed Apr  8 2015 avvissu@yandex.ru
- Initial release
