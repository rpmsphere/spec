%global debug_package %{nil}

Name:         sspkg
License:    Distributable
Group:        Development/Other
Version:      2.1
Release:      14.2
Summary:      Slingshot extensions for XView
Source: SlingShot2.1.tar.gz
Patch: SlingShot2.1.dif
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: xview-devel libtirpc-devel

%description
These are extensions for XView programming; it contains static and dynamic
libraries in elf-format.

%package devel
Requires: sspkg
Summary:      Slingshot Header files and static libraries
Group:        Development/Other

%description devel
All the files needed to develop applications using extensions for XView
Also include  files and the documentation.

%package devel-examples
Requires: sspkg xview
Summary:      Slingshot examples
Group:        Development/Other

%description devel-examples
A little collection of Slingshot examples. You can see the use and the
advantage of the Slingshot extension package.

%prep
%setup -q -n sspkg2.1
%patch
sed -i -e '471s|static||' -e '830s|static||' src/canshell.c
sed -i -e '806s|static||' src/rectobj.c
sed -i -e '232s|static||' -e '265s|static||' src/drawimage.c
sed -i -e 's|static||' src/tree.c
sed -i 's|-lX11|-lX11 -ltirpc|' examples/Makefile

%build
rm -f examples/tree/lex.yy.c
make

%install
perl -pi -e 's!ldconfig.*$!!' Makefile
mkdir -p $RPM_BUILD_ROOT/usr/openwin/{include,lib}

find include -type f -exec chmod 644 {} \;
make install INSTALL_DIR=$RPM_BUILD_ROOT/usr/openwin

mkdir -p $RPM_BUILD_ROOT/usr/openwin/share/doc/sspkg
find doc -type f -exec chmod 644 {} \;
cp -afv doc/* $RPM_BUILD_ROOT/usr/openwin/share/doc/sspkg

mkdir -p $RPM_BUILD_ROOT/usr/openwin/share/src/sspkg
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/sspkg
# copier les exe dans /usr/lib/sspkg
# copier les sources dans doc
#find examples -type f -perm 775 -exec cp -afv {} $RPM_BUILD_ROOT/usr/openwin/lib/sspkg/ \;
cp -avf `echo $(find examples -type f -ls |awk ' ( $3 ~ /x/ ) { print $11 } ')` $RPM_BUILD_ROOT/usr/openwin/lib/sspkg/

#(cd $RPM_BUILD_ROOT/usr/openwin/share/src/sspkg; make -C examples clean )
cp -afv examples $RPM_BUILD_ROOT/usr/openwin/share/src/sspkg
find $RPM_BUILD_ROOT/usr/openwin/share/src/sspkg/examples -type f -name \*.o -exec rm -fv {} \; 

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LEGAL_NOTICE README
/usr/openwin/lib/libsspkg.so
/usr/openwin/lib/libsspkg.so.1
/usr/openwin/lib/libsspkg.so.1.0
/usr/openwin/share/doc

%files devel
%doc LEGAL_NOTICE README
/usr/openwin/include/sspkg/*.h
/usr/openwin/lib/libsspkg.a
/usr/openwin/lib/libsspkg.so.1.0

%files devel-examples
/usr/openwin/lib/sspkg/*
/usr/openwin/share/src

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Fri Oct 06 2006 Vincent Cojot <openlook@NOSPAM.cojot.name> 2.1-5
- rebuild, adapted for RHEL4.
* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1-3mdk
- rebuild
* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.1-2mdk
- rebuild
* Thu Sep 13 2001 Philippe Libat <philippe@mandrakesoft.com> 2.1-1mdk
- mandrakization
