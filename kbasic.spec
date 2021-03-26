%define         dest_dir %{_libdir}/KBasic

Name:           kbasic
Summary:        Modern Basic IDE and compiler
Version:        1.89
Release:        8.11
URL:            http://www.kbasic.com/
License:        GPL-3.0 and LGPL-2.0 and SUSE-NonFree
Group:          Development/Tools/IDE
BuildRequires:  libtool pkgconfig
BuildRequires:  automake autoconf
BuildRequires:  pkgconfig(QtSql)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(phonon)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtSvg)
BuildRequires:  pkgconfig(QtGui)
Source0:        http://www.kbasic.com/kbasic_linux_sourcecode.tar.gz
Source1:        kbasic.png
Source2:        %{name}.desktop
Source3:        %{name}-data.tar.xz

%description
KBasic is a programming language related to VB.NET, Visual Basic, Visual Basic
for Application and Java. It combines the best features of those tools and
comes with built-in backward support for those tools and QBasic as it is 100%
syntax compatible to VB6, VBA and QBasic. Additionally, it comes with support
for VB.NET syntax, functions and similar objects and classes. KBasic uses Qt as
its toolkit. Supports PostgreSQL, SQLite, MySQL, ODBC, MPEG, MP3, WebKit, SVG,
C/C++ libraries, stylesheets, multi-platform.

Provided here are RunTime and IDE, up-to-date documentation is online (http://www.kbasic.com/doku.php?id=manuals).
Docs and examples provided here are extracted from kbasic_professional_linux.tar.gz, as suggested at
www.kbasic.com/doku.php?id=source_codes, to use them in some project, please read the licenses/ contact
the author of the software.

This is the Free Software version, use it for GPL projects only.
Icons are extracted from kbasic_professional_linux.tar.gz, as suggested at
www.kbasic.com/doku.php?id=source_codes. Most Icons are copyrighted KBasic Software
The Crystal Icon Theme is based on http://www.everaldo.com/ (License: LGPL).

Author: Bernd Noetscher

WARNING: You may use the public KBasic’s source codes of the compiler, the IDE and the VM
under the terms of the GNU Public License as published by the Free Software Foundation
(Version 3). If you are interested in using the source codes for other licenses or
closed source commercial development, you must buy commercial licenses from KBasic Software.

%prep
%setup -q -c -a 3
%__sed -i '/^CONFIG += x86/s/x86//' kbrun/kbrun.pro
%__sed -i '2s/* SPACE/+ 1/' kbasic_binding/_menubar/pcode_kbasic_binding_method_id.h
%__sed -i '/^CONFIG += x86/s/x86//;/^QMAKE_CXXFLAGS_RELEASE/s/-o3/-O2/' kbide/kbide.pro

for i in 286 293 300 307 314
do
sed -i $i's|return false;|return "";|' kbshared/_file.h
done
for i in 263 270 277 284 291
do
sed -i $i's|return false;|return "";|' kbshared/_dir.h
done
for i in 2238 2251 2448 2461 2664 2677 2853 2864 3161 3172 3183 3194
do
sed -i $i's|return false;|return NULL;|' kbrun/memory_class.cpp
done
for i in 1089 1102 1450 1461
do
sed -i $i's|return false;|return NULL;|' kbrun/memory_module.cpp
done
for i in 1388 1399 1410 1421 1508 1519
do
sed -i $i's|return false;|return NULL;|' kbrun/memory_sub.cpp
done
sed -i 507's|return false;|return NULL;|' kbrun/memory_type.cpp
for i in 795 820 846 872 988 1006 1168 1186
do
sed -i $i's|return false;|return NULL;|' kbrun/memory_variable.cpp
done
sed -i 3030's|return false;|return "";|' kbshared/_control1.cpp
for i in 2235 2248 2467 2480 2706 2719 2918 2929 3247 3258 3291 3302
do
sed -i $i's|return false;|return NULL;|' kbc/kbc/memory_class.cpp
done
#sed -i '24,26d' kbshared/XString.h
sed -i 's|size_t|size__t|g' kbshared/XString.*
for i in 1090 1103 1475 1486
do
sed -i $i's|return false;|return NULL;|' kbshared/memory_module.cpp
done
sed -i 618's|return false;|return "";|' kbshared/memory_type.cpp
for i in 1389 1400 1433 1444 1531 1542
do
sed -i $i's|return false;|return NULL;|' kbshared/memory_sub.cpp
done

%build
cd kbrun
sed -i -e 's,^#define KBC,//#define KBC,g' ../kbshared/define.h
sed -i -e 's,^#define IDE,//#define IDE,g' ../kbshared/define.h
sed -i -e 's,^//#define RUN,#define RUN,g' ../kbshared/define.h
rm moc*
%ifarch x86_64
qmake-qt4 kbrun.pro QMAKE_CXXFLAGS="-O2 -g -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches  -m64 -mtune=generic -fpermissive"
%else
qmake-qt4 kbrun.pro QMAKE_CXXFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches  -m32 -march=i686 -mtune=atom -fasynchronous-unwind-tables -fpermissive"
%endif
make

cd ../kbc
sed -i -e 's,^//#define KBC,#define KBC,g' ../kbshared/define.h
sed -i -e 's,^#define IDE,//#define IDE,g' ../kbshared/define.h
sed -i -e 's,^#define RUN,//#define RUN,g' ../kbshared/define.h
rm kbc
cp -a ../kbshared kbc
aclocal
automake -a
autoconf
CXXFLAGS="${CXXFLAGS:-%optflags} -fpermissive -Wno-format-security" ; export CXXFLAGS ;
%configure
cp -f %{_bindir}/libtool .
make VERBOSE=1 %{?_smp_mflags}

cd ../kbide
sed -i -e 's,^#define KBC,//#define KBC,g' ../kbshared/define.h
sed -i -e 's,^//#define IDE,#define IDE,g' ../kbshared/define.h
sed -i -e 's,^#define RUN,//#define RUN,g' ../kbshared/define.h
rm moc*
qmake-qt4 kbide.pro QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags} -fpermissive"
lrelease-qt4 -removeidentical -compress kbide.pro
make %{?_smp_mflags} VERBOSE=1

%install
install -d %{buildroot}%{_bindir}
install -D -m755 kbrun/kbrun %{buildroot}%{dest_dir}/kbrun
install -m755 kbc/kbc/kbc kbide/kbide %{buildroot}%{dest_dir}/
cp -r kbc/templates docs examples ide %{buildroot}%{dest_dir}/
%__ln_s %{dest_dir}/examples %{buildroot}%{dest_dir}/ide/
%__ln_s %{dest_dir}/{kbc,kbrun,kbide} %{buildroot}%{_bindir}/
install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc license.txt kbc/AUTHORS
%{_bindir}/*
%{dest_dir}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.89
- Rebuild for Fedora
* Wed Sep 11 2013 fa0sck@gmail.com
- Built  the latest available version.
  + added program icons (and examples and docs, too) from
  "professional" version package.
* Sun Mar 28 2010 lars@linux-schulserver.de
- initial version 1.080924
