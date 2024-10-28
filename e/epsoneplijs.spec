Summary:        Ghostscript IJS Plugin for the Epson EPL printers
Name:           epsoneplijs
Version:        0.4.1
Release:        9.1
Group:          System/Printing
License:        BSD
URL:            https://sourceforge.net/projects/epsonepl/
Source0:        https://osdn.dl.sourceforge.net/sourceforge/epsonepl/%{name}-%{version}.tgz
Patch0:         epsoneplijs-use_system_libs.diff
Patch1:         epsoneplijs-mandriva-install.diff
Patch2:         epsoneplijs-0.4.1-LDFLAGS.diff
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libieee1284-devel
Requires:       ghostscript >= 6.53

%description
Support for the Epson EPL-5700L/5800L/5900L/6100L/6200L printer family under
linux and other unix-like systems.
It is known to work for at least one user for each of 5700L, 5800L,
5900L, and 6100L. 6100L and 6200L support is new.

%prep
%setup -q
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch 0 -p1 -b .use_system_libs
%patch 1 -p1 -b .mandriva-install
%patch 2 -p0 -b .LDFLAGS

%build
perl -pi -e "s|-g -O2 -Wall -Werror -ansi -pedantic -Wmissing-prototypes|$CFLAGS -fPIC|g" Makefile.in

rm -f configure
libtoolize --force --copy; aclocal; autoconf

%configure \
    --with-kernelusb \
    --with-kernel1284 \
    --with-libusb \
    --with-libieee1284 

make
make test5700lusb

gcc $CFLAGS -fPIC -Wall %{optflags} -o epl-5700 epl_docs/epl-5700.c
gcc $CFLAGS -fPIC -Wall %{optflags} -o epl-5800 epl_docs/epl-5800.c
gcc $CFLAGS -fPIC -Wall %{optflags} -o epl5x00l epl_docs/epl5x00l.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%makeinstall

install -m0755 ps2epl.pl $RPM_BUILD_ROOT%{_bindir}
install -m0755 test5700lusb $RPM_BUILD_ROOT%{_bindir}/
install -m0755 epl-5700 $RPM_BUILD_ROOT%{_bindir}/
install -m0755 epl-5800 $RPM_BUILD_ROOT%{_bindir}/
install -m0755 epl5x00l $RPM_BUILD_ROOT%{_bindir}/

pushd foomatic_scripts
sh install_mandrake $RPM_BUILD_ROOT
popd

%files
%doc ChangeLog FAQ LIMITATIONS README* *.pdf epl_test* apsfilter cups epl_docs/epl-protocol.pdf epl_docs/README.1st
%{_bindir}/*
%{_datadir}/cups/model/epson/*.ppd.gz
%{_datadir}/foomatic/db/source/driver/*.xml
%{_datadir}/foomatic/db/source/opt/*.xml

%changelog
* Thu Jul 26 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora

* Wed Feb 23 2011 ennael <ennael> 0.4.1-5.mga1
+ Revision: 57983
- clean spec file
- imported package epsoneplijs

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdv2011.0
+ Revision: 605104
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-4mdv2010.1
+ Revision: 521120
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.1-3mdv2010.0
+ Revision: 424387
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2009.1
+ Revision: 321032
- use %%ldflags

* Fri Sep 05 2008 Tiago Salem <salem@mandriva.com.br> 0.4.1-1mdv2009.0
+ Revision: 281377
- version 0.4.1
- fix broken build
- fix foomatic path

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-8mdv2009.0
+ Revision: 220726
- rebuild

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-7mdv2008.1
+ Revision: 157247
- rebuild with fixed %%serverbuild macro

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-6mdv2008.1
+ Revision: 149699
- rebuild
- kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdv2008.0
+ Revision: 75344
- bump release
- fix deps (pixel)

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.4.0-4mdv2008.0
+ Revision: 68996
- fix description

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdv2008.0
+ Revision: 64159
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2008.0
+ Revision: 61083
- rebuild

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2008.0
+ Revision: 60973
- Import epsoneplijs

* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2008.0
- initial Mandriva package
