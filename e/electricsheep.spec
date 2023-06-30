Summary: collaborative screen-saver
Name: electricsheep
Version: 2.6.8
Release: 1
License: GPL
Group: Graphics
Source: https://electricsheep.org/%{name}-%{version}.tar.gz
Patch: %{name}-%{version}.patch
URL: https://electricsheep.org
Requires: xscreensaver curl flam3 mpeg2dec
BuildRequires: expat libpng12-devel libjpeg-devel libX11-devel

%description
Electric Sheep is a screen-saver that realizes the collective dream of
sleeping computers from all over the internet.

%prep
%setup
%patch -p1

%build
%configure
sed -i -e 's|-Werror=format-security|-I/usr/include/libpng12 -lpng12|' -e 's/-Werror//' */*/Makefile */Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/xscreensaver
make DESTDIR=$RPM_BUILD_ROOT SCREENSAVER_DATADIR=/etc/xscreensaver install

%files
%doc README
%doc %{_mandir}/man1/electricsheep.1*
%{_bindir}/electricsheep*
%exclude %{_bindir}/flam3*
%exclude %{_bindir}/mpeg2dec*
%exclude %{_includedir}/*
%exclude %{_libdir}/*
%{_datadir}/electricsheep/electricsheep*.png
/etc/xscreensaver/electricsheep.xml

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.8
- Rebuilt for Fedora
* Wed Aug 01 2012 Kevin Chen <kevin.chen@ossii.com.tw>
- Rebuild for OSSII
