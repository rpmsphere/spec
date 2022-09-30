Name: pike
Version: 8.0.1738
Release: 1
Summary: Powerful Interpreted Programming Language
URL: http://pike.lysator.liu.se/
License: GPL 2, LGPL 2.1, MPL 1.1
Group: Development/Languages/Other
Source: http://pike.lysator.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
BuildRequires: gcc-c++, bison, autoconf, automake, m4
BuildRequires: zlib-devel, bzip2, libxml2-devel, gmp-devel, gdbm-devel, pcre-devel
BuildRequires: libjpeg-devel libpng-devel giflib-devel libtiff-devel freetype freetype-devel
# mDNSResponder-lib needed to clarify dependency for librsvg
#BuildRequires: mDNSResponder-lib librsvg-devel
#BuildRequires: avahi-compat-mDNSResponder-devel mysql-devel
BuildRequires: libpq-devel, unixODBC-devel
BuildRequires: openssl-devel, krb5-devel
BuildRequires: libglade2-devel, SDL-devel, gtk2-devel, libglade2, libgnome-devel, libgnomeui-devel, libgnomecanvas-devel
BuildRequires: freeglut-devel
BuildRequires: fuse-devel
BuildRequires: sqlite-devel
BuildRequires: librsvg2-devel
BuildRequires: SDL_mixer-devel
BuildRequires: fftw-devel
BuildRequires: nettle-devel
BuildRequires: w3m udisks2

%description
Pike is an interpreted, object-oriented, dynamic programming language
with a syntax similar to C. It includes many powerful data types and
a module system that, for instance, provides image manipulation with
support for graphics formats like SVG, JPG, PNG, GIF, XCF and many
others,  database connectivity, advanced cryptography, XML and HTML
parsers and others.

%package devel
Summary: Development Files for C Modules for Pike
Group: Development/Languages/Other
Requires: %{name} = %{version}

%description devel
This package contains files you will need to develop C extension modules
for Pike. The package depends on  the recommended set of packages for the
Pike  environment.


#%package doc
#Summary: Pike Developer Documentation
#Group: Documentation/Other
#Requires: %{name} = %{version}
#BuildArch: noarch

#%description doc
#Developer documentation (API reference and manual) for Pike.

%prep
%setup -q -n Pike-v%{version}
# fix pike binary path in scripts:
for USRLOCALBINPIKE_FILE in `grep -Rl "/usr/local/bin/pike" *` ; do
  cp $USRLOCALBINPIKE_FILE $USRLOCALBINPIKE_FILE.bak
  cat $USRLOCALBINPIKE_FILE.bak | sed -e "s|/usr/local/bin/pike|%{_bindir}/pike|g" > $USRLOCALBINPIKE_FILE
  rm -f $USRLOCALBINPIKE_FILE.bak
done

%build
#define machine_code --with-machine-code
#make CONFIGUREARGS="--prefix=%{_prefix} --with-freetype --with-ttflib --with-gif --with-jpeglib --with-tifflib --with-svg --with-gmp --with-bignums --without-mysql --without-gdbm --with-odbc --with-postgres --with-zlib --with-pdflib --with-gtk2 --with-libpcre --without-GL --with-GLUT --with-sane --with-SDL --with-Fuse --with-sqlite %{machine_code}" all
#make doc
make CONFIGUREARGS="--prefix=%{_prefix} --without-machine-code" all

%install
rm -rf $RPM_BUILD_ROOT
make buildroot=$RPM_BUILD_ROOT INSTALLARGS="--traditional" install_nodoc

# remove pike.syms:
rm -f $RPM_BUILD_ROOT%{_bindir}/pike.syms

# remove build specs from include directory:
rm -f $RPM_BUILD_ROOT%{_includedir}/pike/specs

# move manpage to correct location:
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
if [ -d $RPM_BUILD_ROOT%{_prefix}/man/man1 ]; then
    [ -e $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1 ] && mv $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1 $RPM_BUILD_ROOT%{_mandir}/man1/
    [ -e $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1.gz ] && mv $RPM_BUILD_ROOT%{_prefix}/man/man1/pike.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
fi

# remove documentation sources that shouldn't have been installed:
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/pike

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING COPYRIGHT ANNOUNCE COMMITTERS
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/pike.1*

%files devel
%{_includedir}/%{name}

#%files doc
#%doc refdoc/modref
#%doc refdoc/traditional_manual

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 8.0.1738
- Rebuilt for Fedora
* Fri Jun 29 2012 oleksii.prudkyi.pike@gmail.com
- update to 7.8.686
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
-  try to hide error about RCS under SLE11
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
- avoid problems with machine-code at sles > 10 and openSUSE > 11.4
* Sun May 13 2012 oleksii.prudkyi.pike@gmail.com
-  try to enable CentOS
* Sat May  5 2012 oleksii.prudkyi.pike@gmail.com
- support of x86_64 in rpmlint
* Sat May  5 2012 oleksii.prudkyi.pike@gmail.com
- switch to 7.8.680
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
- removed fdupes from buildrequires
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
- hide some warnings from rpmlint
* Fri May  4 2012 oleksii.prudkyi.pike@gmail.com
-  updated to pike 7.8.352
