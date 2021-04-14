Summary:       Processing and Analysis of Astronomical Data
Name:          iraf
Version:       2.16
Release:       22.1
License:       MIT-like
Group:         Sciences/Astronomy
Source0:       ftp://iraf.noao.edu/iraf/v216/PCIX/%{name}-src.tar.xz
Source1:       get-iraf.sh
Patch0:        iraf-build.patch
URL:           http://iraf.noao.edu/
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: readline-devel
BuildRequires: cfitsio-devel
BuildRequires: xmlrpc-c-devel
# Note: f2c.h on fedora has a different type size for integer
# than stock f2c.  To make iraf work, we need to compile with
# the included f2c.h
BuildRequires: f2c
BuildRequires: tcsh
BuildRequires: flex
BuildRequires: byacc
BuildRequires: bison
BuildRequires: ncurses-devel
Requires: java
Requires: f2c
Requires: bison

%description
IRAF stands for the Image Reduction and Analysis Facility. It
is the de facto standard for the general processing of astronomical images
and spectroscopy from the ultraviolet to the far infrared. IRAF is a 
product of the National Optical Astronomy Observatories (www.noao.edu). 

%prep
%setup -q -c
%patch0 -p1
chmod a+x util/mksysvos  util/mksysnovos
# make source lexyy.c does not get overwritten
find pkg -name "lexyy.c" | xargs touch

#find -name "ytab.c" | xargs rm -f
# lex has problems run against xppcode
#find pkg -name "lexyy.c" | xargs rm -f
#sed -i unix/boot/spp/xpp/xppcode.c -e 's!extern char \*yytext_ptr;!!g' \
#   -e s!yytext_ptr!yytext!g

%build
export iraf=%{_builddir}/%{name}-%{version}/
export host=unix/
export hlib=${iraf}${host}hlib/
export PATH=$PATH:${iraf}${host}bin/
export pkglibs=${iraf}noao/lib/,${hlib}libc/,${iraf}${host}bin/
cd %{_builddir}/%{name}-%{version}
export HOST_CURL=1
export HOST_READLINE=1
export HOST_EXPAT=1
export HOST_CFITSIO=1
export HOST_XMLRPC=1
unset IRAFARCH
export IRAFARCH=`${hlib}irafarch.csh`

rm -rf vo/votools/.old
rm -rf vo/votools/.url*
rm -f  ${iraf}${host}bin/*
rm -rf ${iraf}${host}bin.*/*
rm -f  ${iraf}${host}bin
rm -f  lib/*.a lib/*.o
rm -f  bin
ln -sf bin.${IRAFARCH} bin

pushd ${hlib}
ln -sf mach`getconf LONG_BIT`.h mach.h
ln -sf iraf`getconf LONG_BIT`.h iraf.h
popd

find -name "*.a" -delete
#Makefiles are not set up for parallel make
make src
export NOVOS=1
pushd vendor/voclient
make mylib
cp libvo/libVO.a ${iraf}lib
popd

${iraf}util/mksysnovos

unset NOVOS
export PATH=$PATH:${iraf}${host}bin/
export pkglibs=${iraf}noao/lib/,${iraf}${host}bin/,${hlib}
pushd vendor/voclient
make clean
make mylib 
cp libvo/libVO.a ${iraf}lib
popd

export pkglibs=${iraf}noao/lib/,${iraf}${host}bin/,${hlib}libc/
${iraf}util/mksysvos
sed -i ${hlib}mkiraf.csh -e s!/iraf/iraf!%{_libdir}/iraf!g
sed -i ${hlib}cl.csh -e s!/iraf/iraf!%{_libdir}/iraf!g
sed -i ${hlib}libc/iraf.h -e s!/iraf/iraf!%{_libdir}/iraf!g
cp ${iraf}${host}bin/*.a ${iraf}lib

find pkg -name "*.e" -delete
cp -p ${iraf}${host}bin/*.e ${iraf}bin
cp -p ${hlib}*.h ${iraf}lib
cp -p ${hlib}*.sh ${iraf}bin

%install
%{__mkdir_p} %{buildroot}/%{_bindir}
cd %{_builddir}/%{name}-%{version}
%{__mkdir_p} %{buildroot}/%{_libdir}/iraf
cp -pr pkg %{buildroot}/%{_libdir}/iraf
cp -pr bin.* %{buildroot}/%{_libdir}/iraf
rm -rf unix/boot unix/as.* unix/os
find -name spool -delete
cp -pr unix vo util extern noao dev *.GEN %{buildroot}/%{_libdir}/iraf
cp -pr lib %{buildroot}/%{_libdir}/iraf
cp -pr include %{buildroot}/%{_libdir}/iraf
cp -pr unix/hlib/mkiraf.csh %{buildroot}/%{_bindir}/mkiraf 
cp -pr unix/hlib/cl.csh %{buildroot}/%{_bindir}/cl
%{__mkdir_p} %{buildroot}/%{_includedir}
pushd  %{buildroot}/%{_libdir}  
cp iraf/unix/hlib/libc/iraf.h %{buildroot}/%{_includedir}
# Remove source files
# Do not remove object files as those are necessary for complilation
# -- > Woud be nice to have all static libs and headers in a
# -- > iraf-devel package (todo)
find \( -name "*.c" -o -name "*.f" -o -name "*.x" -o -name "*.s" \) -delete
popd

%files
%doc doc/*
%{_libdir}/iraf
%{_bindir}/*
%{_includedir}/iraf.h

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.16
- Rebuilt for Fedora
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
