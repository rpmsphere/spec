%undefine _debugsource_packages

Summary:   An user friendly editor for programmers
Name:      setedit
Version:   0.5.8
Release:   1
License:   GPL
Group:     Applications/Editors
Source:    %{name}_%{version}-1.tar.gz
URL:       http://setedit.sourceforge.net/
BuildRequires: rhtvision-devel
BuildRequires: aalib-devel
BuildRequires: libmigdb-devel
#BuildRequires: pcre-devel

%description 
Setedit is a text editor specially designed for programmers. It has a nice
interface with mouse support, menus and windows (text mode). The editor is a 
very good choice for people with DOS background, especially people accustomed
to Worstar and Borland editors. The editor has overlapped windows so you can
see more than one file at the same time, configurable syntax highlighting,
macros, rectangular selection, block indentation, as well as customizable 
keyboard shortcuts and menus.

%package devel 
Summary:   Setedit Developer Environment
Group:     Development/Libraries/editors

%description devel
Header and development files for the package setedit.

%prep
%setup -q -n setedit
#sed -i 's|99\.99|5.1|' config.pl
sed -i 's|/usr/local/lib|/usr/lib64|' config.pl
sed -i 's/CLY_IOSIn | CLY_IOSBin,name/name,CLY_IOSIn | CLY_IOSBin/' mp3/mp3list.cc setedit/dstfile.cc setedit/edprj.cc
sed -i '/TScreen::windowClass/d' setedit/editmain.cc
sed -i 's|require "|require "./|' config.pl
sed -i 's|#define s(TYPE)|#define my_s(TYPE)|' include/tvsetuti.h
sed -i 's|^s(|my_s(|' infview/streams/*.cc settvuti/streams/*.cc mainsrc/ssyntax.cc

%build
rm -f Makefile
perl config.pl --libset
sed -i 's|-O3|-O2 -Wno-narrowing|' mp3/mpegsound/rhide.env
make

%install
make install prefix=$RPM_BUILD_ROOT/usr all
%ifarch x86_64 aarch64
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib64
install -m 0644 makes/libset.a $RPM_BUILD_ROOT/usr/lib64
install -m 0644 makes/libeasyd.a $RPM_BUILD_ROOT/usr/lib64
install -m 0644 makes/libmpegsnd.a $RPM_BUILD_ROOT/usr/lib64
install -m 0644 makes/librhuti.a $RPM_BUILD_ROOT/usr/lib64
install -m 0644 makes/libsettv.a $RPM_BUILD_ROOT/usr/lib64
rm -f $RPM_BUILD_ROOT/usr/lib/libset.a
mv $RPM_BUILD_ROOT/usr/lib/setedit $RPM_BUILD_ROOT/usr/lib64
rmdir $RPM_BUILD_ROOT/usr/lib
chmod 0755 $RPM_BUILD_ROOT/usr/lib64/setedit/*.so
%else
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/libset.a $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/libeasyd.a $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/libmpegsnd.a $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/librhuti.a $RPM_BUILD_ROOT/usr/lib
install -m 0644 makes/libsettv.a $RPM_BUILD_ROOT/usr/lib
chmod 0755 $RPM_BUILD_ROOT/usr/lib/setedit/*.so
%endif
mv $RPM_BUILD_ROOT/usr/doc $RPM_BUILD_ROOT/usr/share/doc
mv $RPM_BUILD_ROOT/usr/info $RPM_BUILD_ROOT/usr/share/info
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share/man

mkdir -p $RPM_BUILD_ROOT/usr/include/setedit
install -m 0644 setedit/include/*.h $RPM_BUILD_ROOT/usr/include/setedit
install -m 0644 librhuti/rhutils.h $RPM_BUILD_ROOT/usr/include/setedit

%files
%{_bindir}/*
%{_datadir}/doc/*
%{_datadir}/info/*
%{_datadir}/man/man?/*
%{_datadir}/%{name}
%{_datadir}/infview
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_libdir}/%{name}

%files devel
%{_libdir}/lib*.a
%{_includedir}/%{name}

%changelog
* Fri Jan 20 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.8
- Rebuilt for Fedora
* Sun May 4 2008 - mcatudal@comcast.net
- First Fedora 8 release
* Fri May 2 2008 - mcatudal@comcast.net
- First Mandriva release
* Sun Nov 21 2004 - Michel Catudal mcatudal@comcast.net
- Update to latest CVS code, use same directory name as CVS
  added revision number to match the revision stated
  in the change.log file
* Sun Mar 8 2004 - bbcat@netonecom.net
- Added include files for development
* Sat Jun 21 2003 - bbcat@netonecom.net
- Convert to support SuSE so it would install
