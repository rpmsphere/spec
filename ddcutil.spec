Name:           ddcutil
Version:        0.8.4
Release:        4.1
Summary:        Query and update monitor settings
License:        GPL-2.0+
Group:          System/GUI/Other
URL:            http://github.com/rockowitz/ddctool
Source:         https://github.com/rockowitz/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  i2c-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  python-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)

%description
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

A particular use case for ddcutil is as part of color profile management.
Monitor calibration is relative to the monitor color settings currently in
effect, e.g. red gain.  ddcutil allows color related settings to be saved at
the time a monitor is calibrated, and then restored when the calibration is
applied.

%package -n ddcutil-lib
Summary:        Shared library to query and update monitor settings
Group:          System/Libraries

%description -n ddcutil-lib
Shared library version of ddcutil, exposing a C API.

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package -n ddcutil-devel
Summary:        Development files for ddcutil
Group:          Development/Libraries/C and C++
Requires:       ddcutil-lib = %{version}

%description -n ddcutil-devel
Header files and pkgconfig control file for ddcutil.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./autogen.sh
%configure --enable-lib=yes --enable-drm=yes --enable-usb=yes \
   --docdir="%{_datadir}/doc/%{name}"
sed -i 's|-Werror | |' Makefile */Makefile */*/Makefile
make %{?_smp_mflags} V=1

%install
%make_install
rm -rf %{buildroot}/usr/share/doc/libddcutil



%files
%doc AUTHORS COPYING NEWS README.md
%{_datadir}/%{name}
%{_mandir}/man1/ddcutil.1*
%{_bindir}/ddcutil

%files -n ddcutil-lib
%{_libdir}/libddcutil.so.*

%files -n ddcutil-devel
%{_includedir}/ddcutil_types.h
%{_includedir}/ddcutil_c_api.h
%{_libdir}/pkgconfig/ddcutil.pc
%{_libdir}/libddcutil.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data/
%{_datadir}/%{name}/data/FindDDCUtil.cmake

%changelog
* Thu Dec 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.4
- Rebuild for Fedora
* Tue Sep  5 2017 jengelh@inai.de
- Clear repeated summary, fix RPM groups, repair description not
  matching the filelists.
* Tue Sep  5 2017 alarrosa@suse.com
- Use the sources as distributed in github, which is different from
  the sources in rockowitz's OBS project
- Use automake/autoconf/libtool
* Mon Sep  4 2017 alarrosa@suse.com
- Don't unset the _unpackaged_files_terminate_build test,
  which was forgotten from the original spec file. Instead,
  set --docdir correctly for configure and remove an unwanted
  file after make install.
- Add the %%doc line to the library package so it also installs the license
* Fri Sep  1 2017 alarrosa@suse.com
- Initial release of ddcutil 0.8.4 based on rockowitz's generic spec file
