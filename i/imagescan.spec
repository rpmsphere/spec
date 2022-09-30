%global upstream utsushi

Name:           imagescan
Version:	3.65.0
Release:        1
Summary:        Next Generation Image Acquisition Utilities
Vendor:         SEIKO EPSON CORPORATION
License:        GPLv3+
URL:            http://utsushi.github.io/imagescan/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.conf
Requires:       ImageMagick
BuildRequires:  desktop-file-utils, pkgconfig, libtool-ltdl-devel
BuildRequires:  gtkmm24-devel, sane-backends-devel, libjpeg-devel
BuildRequires:  libtiff-devel, ImageMagick, automake
BuildRequires:  boost-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  libusb1-devel, ImageMagick-c++-devel

%description
This software provides applications to easily turn hard-copy documents
and imagery into formats that are more amenable to computer processing.

Included are a native driver for a number of EPSON scanners and a
compatibility driver to interface with software built around the SANE
standard.

%prep
%setup -q
sed -i 's|-Werror||' configure
sed -i 's|_1|boost::placeholders::_1|' lib/monitor.cpp drivers/esci/verify.cpp sane/handle.cpp
sed -i 's|_2|boost::placeholders::_2|' sane/handle.cpp
sed -i '26i #include <iostream>' lib/string.cpp
sed -i '24i #include <iostream>' lib/toggle.cpp
sed -i '40,42d' sane/version.hpp

%build
%configure \
    --with-jpeg \
    --with-tiff \
    --without-gtkmm \
    --with-sane \
    --with-magick \
    --with-magick-pp \
    --disable-static \
    %{CXX}

make BACKEND_NAME=%{name}

%install
rm -rf %{buildroot}
make install BACKEND_NAME=%{name} DESTDIR=%{buildroot}
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}
test -d %{buildroot}%{_sysconfdir}/%{name} \
    || %{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
install -m 644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
mv %{buildroot}%{_bindir}/%{upstream} %{buildroot}%{_bindir}/%{name}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/lib*.a
rm -rf %{buildroot}%{_libdir}/lib*.la
rm -rf %{buildroot}%{_libdir}/lib*.so
rm -rf %{buildroot}%{_libdir}/%{upstream}/lib*.a
rm -rf %{buildroot}%{_libdir}/%{upstream}/lib*.so
rm -rf %{buildroot}%{_libdir}/%{upstream}/sane/lib*.a
rm -rf %{buildroot}%{_libdir}/%{upstream}/sane/lib*.la
rm -rf %{buildroot}%{_libdir}/%{upstream}/sane/lib*.so
rm -rf %{buildroot}%{_libdir}/sane/lib*.a
rm -rf %{buildroot}%{_libdir}/sane/lib*.la
rm -rf %{buildroot}%{_libdir}/sane/lib*.so
%find_lang %{upstream}

%clean
rm -rf %{buildroot}

%define have_sane_dll_d %(test -d %{_sysconfdir}/sane.d/dll.d && echo true)

%files -f %{upstream}.lang
%doc NEWS README AUTHORS
%doc COPYING
%{_bindir}/%{name}
%{_libdir}/%{upstream}/
%if "%{_libdir}" != "%{_libexecdir}"
%{_libexecdir}/%{upstream}/
%endif
%{_libdir}/sane/libsane-%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{upstream}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%if "true" == "%{have_sane_dll_d}"
%{_sysconfdir}/sane.d/dll.d/%{name}
%endif
%{_sysconfdir}/udev/rules.d/%{upstream}-esci.rules
%{_sysconfdir}/utsushi/combo.conf

%if "true" != "%{have_sane_dll_d}"
#
#  Modify SANE's dll.conf during (un)installation
#
%post
dll=%{_sysconfdir}/sane.d/dll.conf
if [ -n "`grep '^[ \t]*#[ \t#]*%{name}' ${dll}`" ]
then				# uncomment existing entry
    sed -i 's,^[ \t]*#[ \t#]*\(%{name}\),\1,' ${dll}
elif [ -z "`grep %{name} ${dll}`" ]
then				# append brand new entry
    echo %{name} >> ${dll}
fi

%preun
if [ $1 = 0 ]
then				# comment out existing entry
    dll=%{_sysconfdir}/sane.d/dll.conf
    if [ -n "`grep '^[ \t]*%{name}' ${dll}`" ]
    then
        sed -i 's,^[ \t]*\(%{name}\),#\1,' ${dll}
    fi
fi
%endif

%changelog
* Tue Dec 7 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.65.0
- Rebuilt for Fedora
* Tue Apr 12 2016 Yuji Saito <yuji.saito@avasys.jp> - 3.16.0-1
- new upstream
* Fri Jan 22 2016 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.15.0-1
- new upstream
* Thu Dec 24 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.14.0-1
- new upstream
- set C++11 compile mode at configure time to remove unnecessary library
  dependencies on Boost.Regex and Boost.Thread
* Wed Oct 28 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.13.1-1
- new upstream
- select C++11 compile mode where known to be needed
* Wed Sep 16 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.13.0-1
- new upstream
- add new models to the package description
* Mon Aug 31 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.12.0-1
- new upstream
- add new models to the package description
* Thu Jul 30 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.11.0-1
- new upstream
- add new models to the package description
* Fri Jun 19 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.10.0-1
- new upstream
- add new models to the package description
- activate building of debuginfo packages
* Wed Mar 18 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.9.0-1
- new upstream
- add new models to the package description
- added conditionalized build support for other distributions and
  versions
- switched back to GraphicsMagick as the default, ImageMagick is only
  used when GraphicsMagick is not available
* Tue Jan 27 2015 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.8.3-1
- new upstream
* Tue Nov 18 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.8.2-1
- new upstream
* Thu Nov  6 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.8.1-1
- new upstream
* Fri Oct 17 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.8.0-1
- new upstream
* Fri Aug  8 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.7.0-1
- new upstream
- dropped HAL dependency
- switched from GraphicsMagick to ImageMagick
* Fri Apr 25 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.6.0-1
- new upstream
* Wed Feb  5 2014 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.5.0-1
- new upstream
- add GraphicsMagick build and run-time dependency
* Thu Nov 21 2013 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.4.0-1
- new upstream
* Thu Sep  5 2013 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.3.0-1
- new upstream
- renamed the SANE backend to match the package name
* Mon Mar 11 2013 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.1.0-1
- new upstream
* Fri Nov  2 2012 Olaf Meeuwissen <olaf.meeuwissen@avasys.jp> - 3.0.0-1
- first rebranded public release of Utsushi
