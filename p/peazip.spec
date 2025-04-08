# qt4pas is deprecated maybe we will have qt5pas one day
%bcond_with qt
%undefine _debugsource_packages

Name:    peazip
Version: 10.3.0
Release: 1
Summary: File and archive manager
License: LGPLv3
Group:   Applications/Archiving
URL:     https://www.peazip.org/peazip-linux.html
Source0: https://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}.src.zip
# configure to run in users home appdata
Source1: altconf.txt

BuildRequires: fpc
BuildRequires: fpc-src
BuildRequires: lazarus
BuildRequires: desktop-file-utils

%if %{with qt}
BuildRequires: qt4pas-devel
BuildRequires: qt4-devel
BuildRequires: qtwebkit-devel
%endif

Provides:  peazip-common%{?_isa} = %{version}-%{release}
Obsoletes: peazip-common < %{version}-%{release}
Obsoletes: peazip-qt < %{version}-%{release}
Recommends: p7zip-plugins

%description
PeaZip is a cross-platform portable file and archiver manager.
Create: 7z, 7z-sfx, ARC/WRC, BZ2, GZ, *PAQ, PEA, QUAD/BALZ, split, TAR, UPX,
WIM, XZ, ZIP. Read over 150 formats: ACE, ARJ, CAB, CHM, COMPOUND (MSI, DOC,
XLS, PPT), CPIO, ISO, Java (JAR, EAR, WAR), Linux (DEB, PET/PUP, RPM, SLP),
LHA/LZH, LZMA, NSIS, OOo, PAK/PK3/PK4, RAR, SMZIP, U3P, WIM, XPI, Z/TZ, ZIPX ...

PeaZip allows to create, convert and extract multiple archives at once;
create self-extracting archives; bookmark archives and folders;
apply powerful multiple search filters to archive's content;
export job definition as command line; save archive's layouts;
use custom compressors and extractors; scan and open with custom
applications compressed and uncompressed files etc...

Other features: strong encryption, encrypted password manager, robust file copy,
split/join files (file span), secure data deletion, compare, checksum and hash
files, system benchmark, generate random passwords and keyfiles
Default package provides the GTK2 graphical interface.

%prep
%setup -q -n %{name}-%{version}.src

%build
%if %{with qt}
WGT=qt
%else
WGT=gtk2
%endif
cd dev
lazbuild --lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
        --cpu=x86_64 \
%endif
    --widgetset=${WGT} \
    -B project_pea.lpr project_peach.lpr
#project_demo_lib.lpi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/peazip
%{__cp} -r res %{buildroot}%{_datadir}/peazip
%{__cp} %{SOURCE1} %{buildroot}%{_datadir}/peazip/res

#install helper apps
#mkdir -p %{buildroot}%{_datadir}/peazip/res/7z
#mkdir -p %{buildroot}%{_datadir}/peazip/res/upx
ln -s ../../../../../..%{_bindir}/7z  %{buildroot}%{_datadir}/peazip/res/bin/7z
ln -s ../../../../../..%{_bindir}/arc  %{buildroot}%{_datadir}/peazip/res/bin/arc
ln -s ../../../../../..%{_bindir}/brotli  %{buildroot}%{_datadir}/peazip/res/bin/brotli
ln -s ../../../../../..%{_bindir}/upx  %{buildroot}%{_datadir}/peazip/res/bin/upx
ln -s ../../../../../..%{_bindir}/zpaq  %{buildroot}%{_datadir}/peazip/res/bin/zpaq
ln -s ../../../../../..%{_bindir}/zstd  %{buildroot}%{_datadir}/peazip/res/bin/zstd

cd dev
# peazip needs to be in %{_datadir}/peazip because at start need to read res/altconf.txt
install peazip %{buildroot}%{_datadir}/peazip
ln -s ../..%{_datadir}/peazip/peazip %{buildroot}%{_bindir}
#install pealauncher %{buildroot}%{_datadir}/peazip/res
#ln -s ../..%{_datadir}/peazip/res/pealauncher %{buildroot}%{_bindir}
install pea %{buildroot}%{_datadir}/peazip/res
ln -s ../..%{_datadir}/peazip/res/pea %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     ../res/share/batch/freedesktop_integration/peazip.desktop
install -Dm644 ../res/share/batch/freedesktop_integration/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# IHMO if this is necessary should be done outside of rpmbuild.
## move and convert peazip icon
#mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
#convert %{name}.ico %{name}.png
## The .ico file in 4.8 seens to have multiple files inside
#%{__cp} %{name}-1.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
#%{__cp} %{name}-2.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
#%{__cp} %{name}-4.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

%files
%doc readme*
%license dev/copying_we.txt
%{_bindir}/peazip
%{_bindir}/pea
#{_bindir}/pealauncher
#{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/peazip

%changelog
* Sun Apr 06 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 10.3.0
- Rebuilt for Fedora
* Tue Feb 20 2018 Sérgio Basto <sergio@serjux.com> - 6.5.1-1
- Updated to 6.5.1
* Thu Nov 12 2015 Sérgio Basto <sergio@serjux.com> - 5.8.1-1
- Update PeaZip to 5.8.1
* Wed Jul 15 2015 Sérgio Basto <sergio@serjux.com> - 5.6.1-2
- Update peazip-5.6.1, enable qt build
* Tue May 26 2015 Sérgio Basto <sergio@serjux.com> - 5.5.3-1
- Update peazip-5.5.3
* Fri Jan 17 2014 Sérgio Basto <sergio@serjux.com> - 5.2.1-2
- Bump relversion for epel7
* Thu Jan 16 2014 Sérgio Basto <sergio@serjux.com> - 5.2.1-1
- Update to 5.2.1
* Mon Oct 07 2013 Sérgio Basto <sergio@serjux.com> - 5.1.1-1
- Update to 5.1.1
* Fri Jun 28 2013 Sérgio Basto <sergio@serjux.com> - 5.0-1
- New upstream release.
* Sun Apr 28 2013 Sérgio Basto <sergio@serjux.com> - 4.9.2-1
- First release based on specs of Mageia on https://svnweb.mageia.org/packages/cauldron/peazip/current/SPECS/peazip.spec?view=markup
and https://pkgs.org/download/peazip with src.rpm on https://download.opensuse.org/repositories/home:/zhonghuaren/Fedora_18/src/
* Fri Mar 08 2013 Giorgio Tani
- Initial spec
