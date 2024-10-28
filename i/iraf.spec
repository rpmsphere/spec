%define snapdate 2018.11.01
%define rel 5
%global _legacy_common_support 1

Summary:       Image Reduction and Analysis Facility
Name:          iraf
Version:       2.16.1
Release:       %{snapdate}.%{rel}
License:       MIT-like
Group:         Sciences/Astronomy
URL:           https://iraf-community.github.io/
Source0:       https://github.com/iraf-community/iraf/archive/v%{version}+%{snapdate}/%{name}-%{version}-%{snapdate}.tar.gz
# From Debian
Source10:      irafcl
Source11:      iraf.desktop
Source12:      iraf.svg
# From Debian
Patch101:      Use-system-libraries-when-possible.patch
Patch102:      Create-a-global-login.cl-in-etc.patch

#adusted to mga
Patch103:      Adjust-version-number-and-motd.patch

Patch104:      Remove-architecture-dependency-in-the-names-of-bin-subdir.patch
Patch105:      Separate-NOAO-and-dev-packages.patch

#adjusted to mga
Patch106:      Propagate-CFLAGS-and-debug-flag-to-xc.patch

Patch107:      Skip-source-dependent-tests.patch
Patch108:      Write-default-iraf-host-tmp-variables-back-to-environment.patch
Patch109:      Fix-defterm-imdif-and-cachedir-in-mkiraf.sh.patch
Patch110:      Add-common-gcc10.patch



#(eatdirt) looks like this version needs bootstrapping?
#BuildRequires: iraf-devel

BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(expat)
BuildRequires: readline-devel
BuildRequires: pkgconfig(cfitsio)
BuildRequires: xmlrpc-c-devel
# Note: f2c.h on fedora has a different type size for integer
# than stock f2c.  To make iraf work, we need to compile with
# the included f2c.h
BuildRequires: f2c
BuildRequires: tcsh
BuildRequires: flex

#Fedora requires byacc
#BuildRequires: byacc

BuildRequires: bison
BuildRequires: pkgconfig(ncurses)
#Needed to allow local compilation
Requires: f2c
Requires: bison

%description
IRAF stands for the Image Reduction and Analysis Facility. It
is the de facto standard for the general processing of astronomical images
and spectroscopy from the ultraviolet to the far infrared. IRAF is a
product of the National Optical Astronomy Observatories (www.noao.edu).

%package noao
Summary:       IRAF NOAO data reduction package
Group:         Sciences/Astronomy
Requires:      iraf = %{version}-%{release}

%description noao
IRAF stands for the Image Reduction and Analysis Facility. It
is the de facto standard for the general processing of astronomical images
and spectroscopy from the ultraviolet to the far infrared. IRAF is a
product of the National Optical Astronomy Observatories (www.noao.edu).

This file contains the NOAO packages for the reduction and analysis
of Optical Astronomy data.

%package devel
Summary:       Image Reduction and Analysis Facility (development files)
Group:         Sciences/Astronomy
Requires:      iraf = %{version}-%{release}

%description devel
IRAF stands for the Image Reduction and Analysis Facility. It
is the de facto standard for the general processing of astronomical images
and spectroscopy from the ultraviolet to the far infrared. IRAF is a
product of the National Optical Astronomy Observatories (www.noao.edu).

This package contains the IMFORT Fortran/C programming interface, and
the full SPP/VOS programming environment in which the portable IRAF
system and all applications are written.

%package noao-devel
Summary:       IRAF NOAO data reduction package (development files)
Group:         Sciences/Astronomy
Requires:      iraf-devel = %{version}-%{release}
Requires:      iraf-noao = %{version}-%{release}

%description noao-devel
IRAF stands for the Image Reduction and Analysis Facility. It
is the de facto standard for the general processing of astronomical images
and spectroscopy from the ultraviolet to the far infrared. IRAF is a
product of the National Optical Astronomy Observatories (www.noao.edu).

This package contains additional libraries and headers used for
compiling packages that extend the functionality of the iraf-noao
package.

%prep
%setup -q -n %{name}-%{version}-%{snapdate}
%autopatch -p1
sed -i 's|-DHAVE_CFITSIO|-I/usr/include/cfitsio -DHAVE_CFITSIO|' vendor/libvotable/Makefile

%build
export CC="gcc -fcommon"
export iraf=$(pwd)/
export host=${iraf}unix/
export BUILD_TMP=${iraf}/irafbuild
export HOME=${BUILD_TMP}
export IRAFARCH=$(./unix/hlib/irafarch.sh)

mkdir -p ${BUILD_TMP}
mkdir -p ${BUILD_TMP}/bin
mkdir -p ${BUILD_TMP}/lib
sed "s/__VERSION__/%{version}-%{snapdate}/" -i unix/hlib/zzsetenv.def
sed "s/__DATE__/$(date -uR)/" -i unix/hlib/zzsetenv.def

./install  \
        --term xterm \
        --bindir ${BUILD_TMP}/bin \
        --cache ${BUILD_TMP}/cache \
        --imdir ${BUILD_TMP}/imdir \
        --root ${iraf} < /dev/null || true

cp unix/f2c/libf2c/f2c.h include/
./util/mkarch ${IRAFARCH}

export PATH=$PATH:${BUILD_TMP}/bin
bin=${iraf}bin/ noaobin=${iraf}/noao/bin/ %__make sysgen

%install
mkdir -p %{buildroot}%{_libdir}/iraf/bin
cp -ar bin/*.e %{buildroot}%{_libdir}/iraf/bin/

mkdir -p %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/alloc.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/sgi*.e %{buildroot}%{_libdir}/iraf/unix/bin

for f in $(find . -name \*.hlp \
    -o -name \*.hd \
    -o -name \*.men \
    -o -name \*.cl \
    -o -name \*.par \
    -o -name \*.key \
    -o -name \*.def \
    -o -name \*.dat \
    -o -name \*.gui \
    -o -name \*.pkg \
    -o -name \*.mip \
    -o -name \*.fits \
    -o -path ./dev/\* | \
    cut -c3-) \
    unix/hlib/motd* \
    lib/syserrmsg lib/syshelpdir lib/scr/help.html ; do \
  install -p -D -m 644 $f %{buildroot}%{_libdir}/iraf/$f ; \
done

mkdir -p %{buildroot}%{_libdir}/iraf/extern/
> %{buildroot}%{_libdir}/iraf/extern/.zzsetenv.def
mkdir -p %{buildroot}%{_sysconfdir}/iraf
mv %{buildroot}%{_libdir}/iraf/unix/hlib/login.cl %{buildroot}%{_sysconfdir}/iraf/
mv %{buildroot}%{_libdir}/iraf/unix/hlib/motd.etc %{buildroot}%{_sysconfdir}/iraf/motd
mv %{buildroot}%{_libdir}/iraf/unix/hlib/extern.pkg %{buildroot}%{_sysconfdir}/iraf/
mv %{buildroot}%{_libdir}/iraf/dev/irafhosts %{buildroot}%{_sysconfdir}/iraf/
rm -f %{buildroot}%{_libdir}/iraf/dev/hosts %{buildroot}%{_libdir}/iraf/dev/uhosts
rm -rf %{buildroot}%{_libdir}/iraf/unix/f2c
echo '# HOSTS -- IRAF local network host table.' > %{buildroot}%{_sysconfdir}/iraf/hosts
for f in unix/hlib/util.sh \
         unix/hlib/mkiraf.sh unix/hlib/mkmlist.sh \
         unix/hlib/irafarch.sh ; do \
  install -p -D -m 755 $f %{buildroot}%{_libdir}/iraf/$f ; \
done

# symlinks
ln -s %{_sysconfdir}/iraf/extern.pkg %{buildroot}%{_libdir}/iraf/unix/hlib/extern.pkg
ln -s %{_sysconfdir}/iraf/hosts %{buildroot}%{_libdir}/iraf/dev/hosts
ln -s %{_sysconfdir}/iraf/irafhosts %{buildroot}%{_libdir}/iraf/dev/irafhosts
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/iraf/unix/bin/sgidispatch.e %{buildroot}%{_bindir}/sgidispatch

# noao files
mkdir -p %{buildroot}%{_libdir}/iraf/noao/bin
cp -ar noao/bin/*.e %{buildroot}%{_libdir}/iraf/noao/bin

# dev files
cp -ar bin/lib*.a %{buildroot}%{_libdir}/iraf/bin/
cp -ar bin/libmain.o %{buildroot}%{_libdir}/iraf/bin/
cp -ar include %{buildroot}%{_libdir}/iraf/
cp -ar lib/*.h %{buildroot}%{_libdir}/iraf/lib
cp -ar lib/*.inc %{buildroot}%{_libdir}/iraf/lib
cp -ar lib/math %{buildroot}%{_libdir}/iraf/lib
cp -ar lib/pkg %{buildroot}%{_libdir}/iraf/lib
cp -ar lib/sysruk.x %{buildroot}%{_libdir}/iraf/lib
cp -ar pkg/cl/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/cl
cp -ar pkg/dataio/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/dataio
cp -ar pkg/ecl/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/ecl
cp -ar pkg/images/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/images
cp -ar pkg/images/tv/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/images/tv
cp -ar pkg/lists/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/lists
cp -ar pkg/plot/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/plot
cp -ar pkg/proto/color/src/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/proto/src
cp -ar pkg/proto/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/proto/
cp -ar pkg/proto/vol/src/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/proto/vol
cp -ar pkg/softools/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/softools
cp -ar pkg/system/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/system
cp -ar pkg/utilities/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/utilities
cp -ar pkg/utilities/nttools/libpkg.a %{buildroot}%{_libdir}/iraf/pkg/utilities/nttools
cp -ar unix/bin/f2c.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/generic.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/lib*.a %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/mkpkg.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/rmbin.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/rmfiles.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/rpp.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/rtar.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/wtar.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/xc.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/xpp.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/bin/xyacc.e %{buildroot}%{_libdir}/iraf/unix/bin
cp -ar unix/hlib/*.h %{buildroot}%{_libdir}/iraf/unix/hlib
cp -ar unix/hlib/*.inc %{buildroot}%{_libdir}/iraf/unix/hlib
cp -ar unix/hlib/*.sf %{buildroot}%{_libdir}/iraf/unix/hlib
cp -ar unix/hlib/f77.sh %{buildroot}%{_libdir}/iraf/unix/hlib
cp -ar unix/hlib/libc/ %{buildroot}%{_libdir}/iraf/unix/hlib

# dev symlinks
ln -s %{_libdir}/iraf/unix/bin/generic.e %{buildroot}%{_bindir}/generic
ln -s %{_libdir}/iraf/unix/bin/mkpkg.e %{buildroot}%{_bindir}/mkpkg
ln -s %{_libdir}/iraf/unix/bin/xc.e %{buildroot}%{_bindir}/xc
ln -s %{_libdir}/iraf/unix/bin/xyacc.e %{buildroot}%{_bindir}/xyacc
mkdir -p %{buildroot}%{_includedir}
ln -s %{_libdir}/iraf/unix/hlib/libc/iraf.h %{buildroot}%{_includedir}/iraf.h

# noao dev files
cp -ar noao/artdata/libpkg.a %{buildroot}%{_libdir}/iraf/noao/artdata
cp -ar noao/astcat/src/libpkg.a %{buildroot}%{_libdir}/iraf/noao/astcat
cp -ar noao/astutil/libpkg.a %{buildroot}%{_libdir}/iraf/noao/astutil
cp -ar noao/bin/lib*.a %{buildroot}%{_libdir}/iraf/noao/bin
cp -ar noao/digiphot/apphot/libpkg.a %{buildroot}%{_libdir}/iraf/noao/digiphot/apphot
cp -ar noao/digiphot/daophot/libpkg.a %{buildroot}%{_libdir}/iraf/noao/digiphot/daophot
cp -ar noao/digiphot/photcal/libpkg.a %{buildroot}%{_libdir}/iraf/noao/digiphot/photcal
cp -ar noao/digiphot/ptools/libpkg.a %{buildroot}%{_libdir}/iraf/noao/digiphot/ptools
cp -ar noao/imred/bias/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/bias
cp -ar noao/imred/ccdred/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/ccdred
cp -ar noao/imred/crutil/src/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/crutil
cp -ar noao/imred/dtoi/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/dtoi
cp -ar noao/imred/generic/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/generic
cp -ar noao/imred/irred/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/irred
cp -ar noao/imred/quadred/src/ccdproc/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/quadred/ccdproc
cp -ar noao/imred/quadred/src/quad/libpkg.a %{buildroot}%{_libdir}/iraf/noao/imred/quadred/quad
cp -ar noao/lib/*.h %{buildroot}%{_libdir}/iraf/noao/lib
cp -ar noao/lib/*.inc %{buildroot}%{_libdir}/iraf/noao/lib
cp -ar noao/mtlocal/libpkg.a %{buildroot}%{_libdir}/iraf/noao/mtlocal
cp -ar noao/nproto/libpkg.a %{buildroot}%{_libdir}/iraf/noao/nproto
cp -ar noao/obsutil/src/libpkg.a %{buildroot}%{_libdir}/iraf/noao/obsutil
cp -ar noao/onedspec/libpkg.a %{buildroot}%{_libdir}/iraf/noao/onedspec
cp -ar noao/onedspec/scombine/libpkg.a %{buildroot}%{_libdir}/iraf/noao/onedspec/scombine
cp -ar noao/rv/libpkg.a %{buildroot}%{_libdir}/iraf/noao/rv
cp -ar noao/twodspec/apextract/libpkg.a %{buildroot}%{_libdir}/iraf/noao/twodspec/apextract
cp -ar noao/twodspec/longslit/libpkg.a %{buildroot}%{_libdir}/iraf/noao/twodspec/longslit

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -Dpm644 %{SOURCE11} %{buildroot}%{_datadir}/applications/iraf.desktop

# icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -Dpm644 %{SOURCE12} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/iraf.svg

# irafcl
install -Dpm755 %{SOURCE10} %{buildroot}%{_bindir}/irafcl
sed -i -e 's,/usr/lib/,%{_libdir}/,g' %{buildroot}%{_bindir}/irafcl

%files
%doc doc/*
%dir %{_libdir}/iraf/
%dir %{_libdir}/iraf/lib/
%dir %{_libdir}/iraf/lib/scr/
%{_libdir}/iraf/lib/scr/*
%{_libdir}/iraf/lib/helpdb.mip
%{_libdir}/iraf/lib/syserrmsg
%{_libdir}/iraf/lib/syshelpdir
%{_libdir}/iraf/lib/clpackage.hd
%{_libdir}/iraf/lib/root.hd
%dir %{_libdir}/iraf/dev/
%{_libdir}/iraf/dev/*
%dir %{_libdir}/iraf/pkg/
%dir %{_libdir}/iraf/pkg/bench/
%{_libdir}/iraf/pkg/bench/*
%dir %{_libdir}/iraf/pkg/lists/
%{_libdir}/iraf/pkg/lists/*
%dir %{_libdir}/iraf/pkg/cl/
%{_libdir}/iraf/pkg/cl/*
%dir %{_libdir}/iraf/pkg/language/
%{_libdir}/iraf/pkg/language/*
%dir %{_libdir}/iraf/pkg/system/
%{_libdir}/iraf/pkg/system/*
%dir %{_libdir}/iraf/pkg/obsolete/
%{_libdir}/iraf/pkg/obsolete/*
%dir %{_libdir}/iraf/pkg/plot/
%{_libdir}/iraf/pkg/plot/*
%dir %{_libdir}/iraf/pkg/dbms/
%{_libdir}/iraf/pkg/dbms/*
%dir %{_libdir}/iraf/pkg/xtools/
%{_libdir}/iraf/pkg/xtools/*
%dir %{_libdir}/iraf/pkg/proto/
%{_libdir}/iraf/pkg/proto/*
%dir %{_libdir}/iraf/pkg/ecl/
%{_libdir}/iraf/pkg/ecl/*
%dir %{_libdir}/iraf/pkg/utilities/
%{_libdir}/iraf/pkg/utilities/*
%dir %{_libdir}/iraf/pkg/dataio/
%{_libdir}/iraf/pkg/dataio/*
%dir %{_libdir}/iraf/pkg/images/
%{_libdir}/iraf/pkg/images/*
%dir %{_libdir}/iraf/pkg/softools/
%{_libdir}/iraf/pkg/softools/*
%dir %{_libdir}/iraf/doc/
%{_libdir}/iraf/doc/*
%dir %{_libdir}/iraf/sys/
%{_libdir}/iraf/sys/*
%dir %{_libdir}/iraf/math/
%{_libdir}/iraf/math/*

%exclude %{_libdir}/iraf/pkg/*/*.a
%exclude %{_libdir}/iraf/pkg/*/*/*.a

%dir %{_libdir}/iraf/bin/
#{_libdir}/iraf/bin/cl.e
#{_libdir}/iraf/bin/ecl.e
#{_libdir}/iraf/bin/irafks.e
%{_libdir}/iraf/bin/x_*.e
%dir %{_libdir}/iraf/unix/bin/
%{_libdir}/iraf/unix/bin/sgi*.e
%{_libdir}/iraf/unix/bin/alloc.e
%dir %{_libdir}/iraf/unix/boot/
%{_libdir}/iraf/unix/boot/*
%dir %{_libdir}/iraf/unix/os/
%{_libdir}/iraf/unix/os/*
%dir %{_libdir}/iraf/local/
%{_libdir}/iraf/local/*
%dir %{_libdir}/iraf/util/
%dir %{_libdir}/iraf/extern/
%{_libdir}/iraf/*/.zzsetenv.def
%dir %{_libdir}/iraf/unix/hlib/
%{_libdir}/iraf/unix/hlib/motd
%{_libdir}/iraf/unix/hlib/*.cl
%{_libdir}/iraf/unix/hlib/*.sh
%exclude %{_libdir}/iraf/unix/hlib/f77.sh
%{_libdir}/iraf/unix/hlib/clpackage.hd
%{_libdir}/iraf/unix/hlib/clpackage.men
%{_libdir}/iraf/unix/hlib/extern.pkg
%{_libdir}/iraf/unix/hlib/zzsetenv.def
%{_bindir}/irafcl
%{_bindir}/sgidispatch
%dir %{_sysconfdir}/iraf/
%{_sysconfdir}/iraf/extern.pkg
%{_sysconfdir}/iraf/hosts
%{_sysconfdir}/iraf/irafhosts
%{_sysconfdir}/iraf/login.cl
%{_sysconfdir}/iraf/motd
%{_datadir}/applications/iraf.desktop
%{_datadir}/icons/hicolor/scalable/apps/iraf.svg

%files noao
%dir %{_libdir}/iraf/noao/
%dir %{_libdir}/iraf/noao/artdata/
%{_libdir}/iraf/noao/artdata/*
%dir %{_libdir}/iraf/noao/astcat/
%{_libdir}/iraf/noao/astcat/*
%dir %{_libdir}/iraf/noao/astrometry/
%{_libdir}/iraf/noao/astrometry/*
%dir %{_libdir}/iraf/noao/astutil/
%{_libdir}/iraf/noao/astutil/*
%dir %{_libdir}/iraf/noao/bin/
%{_libdir}/iraf/noao/bin/x_*.e
%dir %{_libdir}/iraf/noao/digiphot
%{_libdir}/iraf/noao/digiphot/*
%dir %{_libdir}/iraf/noao/filterphot/
%{_libdir}/iraf/noao/filterphot/*
%dir %{_libdir}/iraf/noao/focas/
%{_libdir}/iraf/noao/focas/*
%dir %{_libdir}/iraf/noao/imred/
%{_libdir}/iraf/noao/imred/*
%dir %{_libdir}/iraf/noao/lib/
%{_libdir}/iraf/noao/lib/*
%exclude %{_libdir}/iraf/noao/lib/*.h
%exclude %{_libdir}/iraf/noao/lib/*.inc
%dir %{_libdir}/iraf/noao/mtlocal/
%{_libdir}/iraf/noao/mtlocal/*
%{_libdir}/iraf/noao/noao.cl
%{_libdir}/iraf/noao/noao.hd
%{_libdir}/iraf/noao/noao.men
%{_libdir}/iraf/noao/noao.par
%dir %{_libdir}/iraf/noao/nobsolete/
%{_libdir}/iraf/noao/nobsolete/*
%dir %{_libdir}/iraf/noao/nproto/
%{_libdir}/iraf/noao/nproto/*
%dir %{_libdir}/iraf/noao/obsutil/
%{_libdir}/iraf/noao/obsutil/*
%dir %{_libdir}/iraf/noao/onedspec/
%{_libdir}/iraf/noao/onedspec/*
%dir %{_libdir}/iraf/noao/rv/
%{_libdir}/iraf/noao/rv/*
%dir %{_libdir}/iraf/noao/surfphot/
%{_libdir}/iraf/noao/surfphot/*
%dir %{_libdir}/iraf/noao/twodspec/
%{_libdir}/iraf/noao/twodspec/*
%exclude %{_libdir}/iraf/noao/*/*.a
%exclude %{_libdir}/iraf/noao/*/*/*.a

# dev files
%files devel
%{_includedir}/iraf.h
%{_bindir}/generic
%{_bindir}/mkpkg
%{_bindir}/xc
%{_bindir}/xyacc
%{_libdir}/iraf/bin/lib*.a
%{_libdir}/iraf/bin/libmain.o
%dir %{_libdir}/iraf/include/
%{_libdir}/iraf/include/iraf
%{_libdir}/iraf/include/*.h
%{_libdir}/iraf/lib/*.h
%{_libdir}/iraf/lib/*.inc
%{_libdir}/iraf/lib/sysruk.x
%{_libdir}/iraf/lib/math/*.h
%{_libdir}/iraf/lib/pkg/*.h
%{_libdir}/iraf/pkg/cl/*.a
%{_libdir}/iraf/pkg/dataio/*.a
%{_libdir}/iraf/pkg/ecl/*.a
%{_libdir}/iraf/pkg/images/*.a
%{_libdir}/iraf/pkg/images/tv/*.a
%{_libdir}/iraf/pkg/lists/*.a
%{_libdir}/iraf/pkg/plot/*.a
%{_libdir}/iraf/pkg/proto/*.a
%{_libdir}/iraf/pkg/proto/vol/*.a
%{_libdir}/iraf/pkg/softools/*.a
%{_libdir}/iraf/pkg/system/*.a
%{_libdir}/iraf/pkg/utilities/*.a
%{_libdir}/iraf/pkg/utilities/nttools/*.a
%{_libdir}/iraf/unix/bin/f2c.e
%{_libdir}/iraf/unix/bin/generic.e
%{_libdir}/iraf/unix/bin/libboot.a
%{_libdir}/iraf/unix/bin/libf2c.a
%{_libdir}/iraf/unix/bin/libos.a
%{_libdir}/iraf/unix/bin/mkpkg.e
%{_libdir}/iraf/unix/bin/rmbin.e
%{_libdir}/iraf/unix/bin/rmfiles.e
%{_libdir}/iraf/unix/bin/rpp.e
%{_libdir}/iraf/unix/bin/rtar.e
%{_libdir}/iraf/unix/bin/wtar.e
%{_libdir}/iraf/unix/bin/xc.e
%{_libdir}/iraf/unix/bin/xpp.e
%{_libdir}/iraf/unix/bin/xyacc.e
%{_libdir}/iraf/unix/hlib/*.h
%{_libdir}/iraf/unix/hlib/*.inc
%{_libdir}/iraf/unix/hlib/*.sf
%{_libdir}/iraf/unix/hlib/f77.sh
%dir %{_libdir}/iraf/unix/hlib/libc
%{_libdir}/iraf/unix/hlib/libc/*

# noao dev files
%files noao-devel
%{_libdir}/iraf/noao/bin/lib*.a
%{_libdir}/iraf/noao/lib/*.h
%{_libdir}/iraf/noao/lib/*.inc
%{_libdir}/iraf/noao/artdata/*.a
%{_libdir}/iraf/noao/astcat/*.a
%{_libdir}/iraf/noao/astutil/*.a
%{_libdir}/iraf/noao/digiphot/apphot/*.a
%{_libdir}/iraf/noao/digiphot/daophot/*.a
%{_libdir}/iraf/noao/digiphot/photcal/*.a
%{_libdir}/iraf/noao/digiphot/ptools/*.a
%{_libdir}/iraf/noao/imred/bias/*.a
%{_libdir}/iraf/noao/imred/ccdred/*.a
%{_libdir}/iraf/noao/imred/crutil/*.a
%{_libdir}/iraf/noao/imred/dtoi/*.a
%{_libdir}/iraf/noao/imred/generic/*.a
%{_libdir}/iraf/noao/imred/irred/*.a
%{_libdir}/iraf/noao/mtlocal/*.a
%{_libdir}/iraf/noao/nproto/*.a
%{_libdir}/iraf/noao/obsutil/*.a
%{_libdir}/iraf/noao/onedspec/*.a
%{_libdir}/iraf/noao/onedspec/scombine/*.a
%{_libdir}/iraf/noao/rv/*.a
%{_libdir}/iraf/noao/twodspec/apextract/*.a
%{_libdir}/iraf/noao/twodspec/longslit/*.a

%changelog
* Sun Jul 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.16.1-2018.11.01.5
- Rebuilt for Fedora
* Mon Sep 07 2020 eatdirt <eatdirt> 2.16.1-2018.11.01.5.mga8
+ Revision: 1623181
- Fix double call to make
- Fix path and built setup
- Rebuild for new cfitsio
+ daviddavid <daviddavid>
- rebuild for new cfitsio 3.480

* Sat Jun 27 2020 joequant <joequant> 2.16.1-2018.11.01.2.mga8
+ Revision: 1599495
- add gcc10 patch
- rebuild for bootstrap
- fix bootstrap

* Fri Mar 20 2020 eatdirt <eatdirt> 2.16.1-2018.11.01.1.mga8
+ Revision: 1558375
- Upgrade to snapdate 2018.11.01

* Tue Feb 18 2020 umeabot <umeabot> 2.16.1-2018.06.15.3.mga8
+ Revision: 1542176
- Mageia 8 Mass Rebuild

* Sat Jan 04 2020 luigiwalser <luigiwalser> 2.16.1-2018.06.15.2.mga8
+ Revision: 1475971
- rebuild for readline

* Mon Sep 10 2018 wally <wally> 2.16.1-2018.06.15.1.mga7
+ Revision: 1258154
- switch to IRAF community edition
- new snapshot release 2.16.1+2018.06.15
- sync with Debian
- add new subpkgs devel, noao and noao-devel

* Sun May 13 2018 daviddavid <daviddavid> 2.16-26.mga7
+ Revision: 1228765
- rebuild for new cfitsio 3.450

* Sun Apr 08 2018 daviddavid <daviddavid> 2.16-25.mga7
+ Revision: 1216151
- rebuild for new xmlrpc-c 1.51.0

* Tue Jan 02 2018 wally <wally> 2.16-24.mga7
+ Revision: 1189444
- rebuild for new readline

* Wed Nov 30 2016 pterjan <pterjan> 2.16-23.mga6
+ Revision: 1071119
- Fix missing amov* symbols on arm

* Tue Nov 22 2016 eatdirt <eatdirt> 2.16-22.mga6
+ Revision: 1068820
- Rebuild for new cfitsio

* Tue Nov 01 2016 eatdirt <eatdirt> 2.16-21.mga6
+ Revision: 1064628
- Fix segmentation violation by compiling with -O0 and cleaning patches

* Fri Oct 28 2016 pterjan <pterjan> 2.16-20.mga6
+ Revision: 1063808
- Also create bindir under unix/
- Create dir also in our patch, not sure if used
- Create arch bin directory if it does not exist

* Thu Oct 27 2016 pterjan <pterjan> 2.16-19.mga6
+ Revision: 1063784
- Fix problems in the arm patch causing missing binaries on other architectures

* Mon Aug 01 2016 pterjan <pterjan> 2.16-18.mga6
+ Revision: 1044189
- Try to fix arm again...

* Mon Aug 01 2016 pterjan <pterjan> 2.16-17.mga6
+ Revision: 1044182
- Fix patch to not break i586
- Make it work on arm (most important part is from Debian)

* Thu Mar 10 2016 eatdirt <eatdirt> 2.16-15.mga6
+ Revision: 988671
- Rebuild for new cfitsio

* Wed Feb 03 2016 umeabot <umeabot> 2.16-14.mga6
+ Revision: 933050
- Mageia 6 Mass Rebuild

* Wed Oct 15 2014 umeabot <umeabot> 2.16-13.mga5
+ Revision: 743625
- Second Mageia 5 Mass Rebuild

* Fri Sep 26 2014 tv <tv> 2.16-12.mga5
+ Revision: 725095
- rebuild for bogus file deps

* Tue Sep 16 2014 umeabot <umeabot> 2.16-11.mga5
+ Revision: 680561
- Mageia 5 Mass Rebuild

* Fri Feb 28 2014 eatdirt <eatdirt> 2.16-10.mga5
+ Revision: 597730
- Rebuild for new cfitsio
+ joequant <joequant>
- add O2 optimizations to everything
  O3 will cause garbage output

* Thu Oct 31 2013 joequant <joequant> 2.16-8.mga4
+ Revision: 548711
- fix double memory alignment problem
  second pass at fix for 11507

* Tue Oct 29 2013 joequant <joequant> 2.16-7.mga4
+ Revision: 547906
- fix bug 11507

* Sat Oct 19 2013 umeabot <umeabot> 2.16-6.mga4
+ Revision: 531780
- Mageia 4 Mass Rebuild

* Sat Aug 10 2013 eatdirt <eatdirt> 2.16-5.mga4
+ Revision: 465260
- Packaging missing pkg/cl.par files to fix CL crash

* Sun Jul 28 2013 joequant <joequant> 2.16-4.mga4
+ Revision: 459363
- tweak spec not to clean out object files for devkit
- more spec tweaks

* Sun Jul 28 2013 joequant <joequant> 2.16-3.mga4
+ Revision: 459343
- tweak requires to set up devkit correctly

* Sun Jul 28 2013 joequant <joequant> 2.16-2.mga4
+ Revision: 459331
- don't delete .h from iraf distribution

* Sat Jul 27 2013 joequant <joequant> 2.16-1.mga4
+ Revision: 458839
- add CFITSIO variable
- use custom iraf for 32 bit also
- remove extra curl files and unneeded build requires
- add debian fixes
- add xmlrpc-c-devel to buildrequires
- use external xmlrpc
  remove unnecessary external files
- update build patch
  fix iraf data location
- add java requires
- clean up spec files
- change more default directory paths
- comment out yacc
- use host cfitsio
- using implicit length arrays in RPP to avoid overflows
- checkpoint with latest changes
- imported package iraf

