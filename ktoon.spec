%global debug_package %{nil}

Name:           ktoon
Version:        0.9a.git04
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ qt4-devel kom-devel ruby mesa-libGL-devel aspell-devel compat-ffmpeg-devel
URL:            http://www.ktoon.net/
Release:        56.1
License:        GPL
Source0:        %name-0.9a-git04.tar.gz
Group:          Productivity/Graphics/Other
Summary:        2D animation toolkit
Patch0:		ktoon-0.9a-git04-permissive.patch

%description
* A design and authoring tool for 2D Animation inspired by animators for animators
* A software application developed in C++ using the Qt library
* A free software project under constant redesign and evolution, released under the GPL terms
* A community of artists and developers around a software project
* A space for creation and publishing of free animated content

%prep
%setup -q -n %name-0.9a-git04
%patch0
rm src/plugins/*/*/*.so
sed -i 's|bool \*ok = false;|bool *ok;*ok = false;|' src/components/library/ktlibrarywidget.cpp

%build
qmake-qt4 -recursive
sed -i -e 's|^INCPATH.*=|INCPATH=-I/usr/include/compat-ffmpeg |' -e 's|^LIBS.*=|LIBS=-L%{_libdir}/compat-ffmpeg |' `find . -name Makefile`
make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT/%{_datadir}/ktoon
cp -a src/themes $RPM_BUILD_ROOT/%{_datadir}/ktoon
cd src/libktoon
install -d $RPM_BUILD_ROOT/%{_includedir}/ktoon
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/ktoon
install -Dm755 libktoon.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktoon.so.1.0.0
ln -s libktoon.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktoon.so
ln -s libktoon.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktoon.so.1
ln -s libktoon.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktoon.so.1.0
cd ../store
install -d $RPM_BUILD_ROOT/%{_includedir}/ktoon/store
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/ktoon/store
install -Dm755 libstore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libstore.so.1.0.0
ln -s libstore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libstore.so
ln -s libstore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libstore.so.1
ln -s libstore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libstore.so.1.0
cd ../libbase
install -d $RPM_BUILD_ROOT/%{_includedir}/ktoon/base
install -p *.h $RPM_BUILD_ROOT/%{_includedir}/ktoon/base
install -Dm755 libktbase.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktbase.so.1.0.0
ln -s libktbase.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktbase.so
ln -s libktbase.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktbase.so.1
ln -s libktbase.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/ktoon/libktbase.so.1.0
cd ../components
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/ktoon/data
cp -a colorpalette/palettes $RPM_BUILD_ROOT/%{_datadir}/ktoon/data
cp -a help/help $RPM_BUILD_ROOT/%{_datadir}/ktoon/data
cd ../shell
cp -a data/* $RPM_BUILD_ROOT/%{_datadir}/ktoon/data
cd ../../bin
install -Dm755 ktoon.bin $RPM_BUILD_ROOT/%{_bindir}/ktoon.bin
cd ../launcher
#install -Dm755 ktoon $RPM_BUILD_ROOT/%{_bindir}/ktoon
cat > $RPM_BUILD_ROOT/%{_bindir}/ktoon <<EOF
#!/usr/bin/bash
export KTOON_HOME="%{_datadir}/ktoon"
export KTOON_SHARE="%{_datadir}/ktoon"
export KTOON_LIB="%{_libdir}/ktoon"
export KTOON_INCLUDE="%{_includedir}/ktoon"
export KTOON_BIN="%{_bindir}"
export LD_LIBRARY_PATH="${KTOON_LIB}:/usr/lib/kom/plugins:$LD_LIBRARY_PATH"
exec ${KTOON_BIN}/ktoon.bin $*
EOF
chmod +x $RPM_BUILD_ROOT/%{_bindir}/ktoon
install -Dm644 ktoon.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/ktoon.desktop
install -Dm644 icons/ktoon.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/ktoon.png
cd ../src/plugins
install -d -m755 $RPM_BUILD_ROOT/%{_libdir}/ktoon/plugins
install -m755 */*/*.so $RPM_BUILD_ROOT/%{_libdir}/ktoon/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9a.git04
- Rebuild for Fedora
* Fri Nov 09 2007 - pnemec@suse.cz
- fixed type in wraper script
* Tue Jun 05 2007 - pnemec@suse.cz
- hacked package so everything is installed under /usr/%%lib/ktoon 
  and program is run trough wraper with LD_LIBRARY_PATH
- added destkop file
* Fri May 04 2007 - pnemec@suse.cz
- initial version 0.7.2
