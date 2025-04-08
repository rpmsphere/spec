%undefine _debugsource_packages
%global __os_install_post %{nil}

Name: ds9
Version: 8.6
Summary: Astronomical Data Visualization Application
Release: 1
License: GPLv2+
Group: Applications/Engineering
URL: https://hea-www.harvard.edu/RD/ds9/
Source: https://hea-www.harvard.edu/saord/download/ds9/source/ds9.%{version}.tar.gz
Source1: ds9.desktop
Source2: ds9.png
Source3: ds9.conf
BuildRequires: gcc-c++, zip, gcc-gfortran, libstdc++-static, libXScrnSaver-devel
BuildRequires: libX11-devel, libXrandr-devel, libXt-devel, fontconfig-devel, automake
BuildRequires: tcl-devel, tk-devel, libxml2-devel, libxml2-static, libxslt-devel

%description
SAOImage DS9 is an astronomical imaging and data visualization application.
DS9 supports FITS images and binary tables, multiple frame buffers, region
manipulation, and many scale algorithms and colormaps. It provides for easy
communication with external analysis tasks and is highly configurable and
extensible.

%prep
%setup -q -n SAOImageDS9
#sed -i -e 's|usr/X11R6|usr|' -e 's|44||' make.linux*
#sed -i 's|-Wall|-Wall -fpermissive -Wno-int-conversion -Wno-implicit-function-declaration|' make.linux*
#sed -i 's|-fno-inline|-fno-inline -fpermissive -Wno-int-conversion -Wno-implicit-function-declaration|' make.linux*
#sed -i -e 's|-lxml2|-lxml2 -lfontconfig -lfreetype|' ds9/Makefile
#sed -i "s|0x8b|'\x8b'|" saotk/fitsy++/outsocket.C
#sed -i 's|mapdata_>0|mapdata_ != NULL|' saotk/fitsy++/*.C
#sed -i 's|typedef int ptrdiff_t|typedef long int ptrdiff_t|' tcl8.5.9/generic/tclInt.h
sed -i 's|typedef unsigned long z_crc_t|typedef unsigned int z_crc_t|' tclzipfs/tclZipfs.c

%build
%if 0
for i in */config.guess */*/config.guess */*/*/config.guess */*/*/*/config.guess
do
cp -f /usr/share/automake-*/config.guess $i
done
%ifarch aarch64
sed -i 's|-m64||' make.linux64
%endif
%ifarch x86_64 aarch64
ln -s make.linux64 make.include
%else
ln -s make.linux make.include
%endif
cd ast-7.1.1
./configure --enable-shared=no --prefix=/root/rpmbuild/BUILD/saods9  CC='gcc'
cd ..
%endif
#sed -i 's|-fno-inline|-fno-inline -fpermissive -Wno-int-conversion -Wno-implicit-function-declaration|' `find . -name Makefile` `find . -name Makefile.in`
unix/configure
sed -i 's| -o | -lm -o |' `find . -name 'Makefile*'`
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp bin/ds9 $RPM_BUILD_ROOT/usr/bin
%{__mkdir_p} $RPM_BUILD_ROOT/%{_datadir}/pixmaps
%{__cp} -a %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps
%{__mkdir_p} $RPM_BUILD_ROOT/%{_datadir}/applications
%{__cp} -a %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications
%{__mkdir_p} $RPM_BUILD_ROOT/etc/prelink.conf.d
%{__cp} -a %{SOURCE3} $RPM_BUILD_ROOT/etc/prelink.conf.d

%files
#doc README notes.txt copyright COPYING
%{_bindir}/ds9
%{_datadir}/applications/ds9.desktop
%{_datadir}/pixmaps/ds9.png
%{_sysconfdir}/prelink.conf.d/ds9.conf

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 8.6
- Rebuilt for Fedora
* Tue Jan 24 2012 <tom@mmto.org>
- version 6.2-3
- add prelink blacklist file so prelink will not screw with ds9
* Tue Jan 17 2012 <tom@mmto.org>
- version 6.2-1
- As of fedora 16, ds9 is no longer a fedora package
- but we need it and need to do something.
