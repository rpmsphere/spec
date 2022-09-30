%undefine _debugsource_packages

Name: ds9
Version: 7.2
Summary: Astronomical Data Visualization Application
Release: 12.1
License: GPLv2+
Group: Applications/Engineering
URL: http://hea-www.harvard.edu/RD/ds9/
Source: http://hea-www.harvard.edu/saord/download/ds9/source/ds9.%{version}.tar.gz
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
%setup -q -n sao%{name}
sed -i -e 's|usr/X11R6|usr|' -e 's|44||' -e 's|-fPIC|-fPIC -fpermissive|' make.linux*
sed -i -e 's|-lxml2|-lxml2 -lfontconfig -lfreetype|' ds9/Makefile
sed -i "s|0x8b|'\x8b'|" saotk/fitsy++/outsocket.C
sed -i 's|mapdata_>0|mapdata_ != NULL|' saotk/fitsy++/*.C

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README notes.txt copyright COPYING
%{_bindir}/ds9
%{_datadir}/applications/ds9.desktop
%{_datadir}/pixmaps/ds9.png
%{_sysconfdir}/prelink.conf.d/ds9.conf

%changelog
* Wed Jun 04 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 7.2
- Rebuilt for Fedora
* Tue Jan 24 2012 <tom@mmto.org>
- version 6.2-3
- add prelink blacklist file so prelink will not screw with ds9
* Tue Jan 17 2012 <tom@mmto.org>
- version 6.2-1
- As of fedora 16, ds9 is no longer a fedora package
- but we need it and need to do something.
