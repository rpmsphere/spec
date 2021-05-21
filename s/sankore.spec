Name:		sankore
Version:	2.00
Release:	1353445475git
License:	GPL-3.0+
Summary:	The open-source software suite for digital teachers
URL:		https://github.com/Sankore/
Group:		Amusements/Teaching/Other
Source0:	%{name}-3.1.git.1353445475.tar.gz
Source1:	%{name}-thirdparty-1353579018.tar.gz
Patch0:		tutorial_it.diff
Patch1:		editor_it.diff
BuildRequires:	libnotify libgomp
BuildRequires:	qtwebkit-devel qt-devel
BuildRequires:	openssl-devel
BuildRequires:	phonon-devel
BuildRequires:	libpaper-devel
BuildRequires:	t1lib-devel
BuildRequires:	desktop-file-utils
Requires:	qtwebkit phonon

%description
Sankore can be considered as three integrated functions in one outstanding tool:
- uniboard universal interactive white board software
- the sankore teaching designer
- the sankore editor
  
%prep
%setup -q -n sankore-3.1.git.1353445475 -a 1
mv sankore-thirdparty* Sankore-ThirdParty

#freetype
cd Sankore-ThirdParty/freetype
qmake-qt4 freetype.pro -spec linux-g++
make -j4

#xpdf
cd ../xpdf/xpdf-3.03
./configure \
	      --with-freetype2-library="../../freetype/lib/linux" \
	      --with-freetype2-includes="../../freetype/freetype-2.4.6/include"
cd ..
qmake-qt4 xpdf.pro -spec linux-g++
make -j4

#quazip
cd ../quazip
qmake-qt4 quazip.pro -spec linux-g++
make -j4

%setup -q -n %{name}-3.1.git.1353445475
#Italian Tutorial
%patch0 -p1
#Italian Editor
%patch1 -p1

%build
qmake-qt4 Sankore_3.1.pro -spec linux-g++ 
make -j4

%install
make INSTALL="install -p" release-install
#missed icon, taking one
install -D -m 0644 resources/images/uniboard.png %{buildroot}%{_libdir}/OpenSankore/sankore.png

#missed desktop file, writing one
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Open Sankore
Comment=Software to create presentations for interactive whiteboard (TNI)
Exec=%{name}
Icon=%{_libdir}/OpenSankore/sankore.png
StartupNotify=true
Terminal=false
Type=Application
Categories=KDE;Education;Engineering;
EOF

#Install files
mkdir -p %{buildroot}%{_libdir}/OpenSankore/i18n/
install -D -m 0755 build/linux/release/product/Open-Sankore %{buildroot}%{_libdir}/OpenSankore/Open-Sankore
cp -a build/linux/release/product/* %{buildroot}%{_libdir}/OpenSankore

#sankore
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
# --------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------
cd %{_libdir}/OpenSankore
LD_LIBRARY_PATH=$PWD/qtlib:$PWD/plugins/cffadaptor:$LD_LIBRARY_PATH %{_libdir}/OpenSankore/Open-Sankore
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

# clean some exe bits
find %{buildroot}%{_libdir}/OpenSankore/library -type f -name *.js -exec chmod -x {} \;
find %{buildroot}%{_libdir}/OpenSankore/library -type f -name *.svg -exec chmod -x {} \;
find %{buildroot}%{_libdir}/OpenSankore/library -type f -name *.css -exec chmod -x {} \;
find %{buildroot}%{_libdir}/OpenSankore/library -type f -name *.xml -exec chmod -x {} \;
chmod -x %{buildroot}%{_libdir}/OpenSankore/library/*/*/*.html

#Internalization
lrelease-qt4 Sankore_3.1.pro
cp -a resources/i18n/sankore*.qm %{buildroot}%{_libdir}/OpenSankore/i18n/
cp -a /usr/share/qt4/translations/qt_??.qm %{buildroot}%{_libdir}/OpenSankore/i18n/

#qt.conf
cp -a resources/linux/qtlinux/* %{buildroot}%{_libdir}/OpenSankore/

#customizations
cp -a resources/customizations %{buildroot}%{_libdir}/OpenSankore/

#cffadaptor
cd plugins/cffadaptor
qmake-qt4 UBCFFAdaptor.pro -spec linux-g++
make
mkdir -p %{buildroot}%{_libdir}/OpenSankore/plugins/cffadaptor
cp -a build/linux/release/lib/libCFF_Adaptor.so.1.0.0 %{buildroot}%{_libdir}/OpenSankore/plugins/cffadaptor/libCFF_Adaptor.so

#plugins
cp -a %_libdir/qt4/plugins/* %{buildroot}%{_libdir}/OpenSankore/plugins/

#copy qt library
mkdir -p %{buildroot}%{_libdir}/OpenSankore/qtlib
%define qtlib %{buildroot}%{_libdir}/OpenSankore/qtlib
cp -a %_libdir/libphonon.so.4* %qtlib
cp -a %_libdir/libQtWebKit.so.4* %qtlib
cp -a %_libdir/libQtDBus.so.4* %qtlib
cp -a %_libdir/libQtScript.so.4* %qtlib
cp -a %_libdir/libQtSvg.so.4* %qtlib
cp -a %_libdir/libQtXmlPatterns.so.4* %qtlib
cp -a %_libdir/libQtNetwork.so.4* %qtlib
cp -a %_libdir/libQtXml.so.4* %qtlib
cp -a %_libdir/libQtGui.so.4* %qtlib
cp -a %_libdir/libQtCore.so.4* %qtlib
cp -a %_libdir/libQtOpenGL.so.4* %qtlib

%clean
rm -rf %{buildroot}

%files
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/OpenSankore

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.00
- Rebuilt for Fedora
* Sun Dec  9 2012 chri@gallochri.com
-Initial Debian Version
* Wed Dec  5 2012 chri@gallochri.com
-Moved files to /usr/lib(64)
* Mon Dec  3 2012 chri@gallochri.com
-Fedora_17 version added
* Mon Dec  3 2012 chri@gallochri.com
-First initial release
