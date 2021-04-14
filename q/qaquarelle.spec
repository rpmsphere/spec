Name:           qaquarelle
Version:        0.0.4
Release:        28.1
License:        GPL-3.0
Summary:        Digital painting
URL:            http://qaquarelle.sourceforge.net
Group:          Graphics/Editors and Converters
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        ru.ts
Source2:        %{name}.desktop
Source3:        %{name}.png
Patch0:		%{name}-%{version}-mga-fix-toolbar.patch
Patch1:		%{name}-%{version}-mga-debug-output.patch
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(glew) >= 2.0.0
BuildRequires:	pkgconfig(glu)

%description
Program to paint with tablets using traditional drawing techniques.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod -x README
chmod -x PERFORMANCE
cp -f %{SOURCE1} .
sed -i -e "s|target.path = /usr/bin|target.path = %{_datadir}/%{name}|g" client/qasuiteapp/qasuiteapp.pro
sed -i -e "s|target.path = /usr/bin|target.path = %{_datadir}/%{name}|g" server/qasuite_server/qasuite_server.pro
sed -i -e "s|-lShiny|-lShiny -lGLU|g" ./client/qasuiteapp/qasuiteapp.pro
sed -i -e 's|loc_path = DATA_PATH + "locale/";|loc_path = DATA_PATH + "/locale/";|g' client/qasuiteapp/main.cpp
sed -i -e 's|translator.load(loc_path);|translator.load("qaquarelle", loc_path);|g' client/qasuiteapp/main.cpp
sed -i -e 's|/../share/qaquarelle||g' client/qasuiteapp/main.cpp
echo "TRANSLATIONS = ./ru.ts" >> qasuite.pro
sed -i -e '524s|QFile file|QFile newfile|' -e '525s|\&file|\&newfile|' -e '628s|QFile file|QFile newfile|' -e '629s|\&file|\&newfile|' client/modules/connector_loopback/connector.cpp
sed -i '/float atanh/d' include/qhasmath.h
sed -i '12,14d' common/modules/qhasmath/qhasmath.cpp
%ifarch aarch64
sed -i 's| -mmmx -msse -mfpmath=sse||' qmakeroot.pri
sed -i -e 's|mm_malloc.h|malloc.h|' -e 's|_mm_||' -e 's|block_sz + 64, 32|block_sz + 64|' common/modules/arrays/arrays_gpu.cpp
sed -i '/xmmintrin.h/d' common/modules/arrays/arraygrid_patch.cpp
%endif

%build
qmake-qt4
lrelease-qt4 ./qasuite.pro
mkdir -p ./bin/locale/ru
cp -f ./ru.qm ./bin/locale/ru/%{name}.qm
make

%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/%{name}/locale
cp -rf ./bin/locale/* %{buildroot}%{_datadir}/%{name}/locale/

mkdir -p %{buildroot}%{_bindir}
echo "#!/bin/bash" > %{buildroot}%{_bindir}/%{name}
echo "exec %{_datadir}/%{name}/%{name}" >> %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

chmod -x %{buildroot}%{_datadir}/%{name}/shaders/*/*.glsl
chmod -x %{buildroot}%{_datadir}/%{name}/pigments/*.xml
chmod -x %{buildroot}%{_datadir}/%{name}/images/paper/*.xml

%files
%doc README PERFORMANCE license.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Aug 16 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuilt for Fedora
* Fri Aug 15 2014 alexl <alexl> 0.0.4-5.mga5
+ Revision: 662713
- updated Russian translation
- fixed empty string for toolbar (fix-toolbar.patch)
- moved debug output from current dir into /tmp (debug-output.patch)
* Thu Aug 14 2014 alexl <alexl> 0.0.4-4.mga5
+ Revision: 662509
- translated desktop file
- fixed incorrect author's permissions (rpmlint)
- changed launch script
* Tue Apr 08 2014 alexl <alexl> 0.0.4-3.mga5
+ Revision: 612916
- some optimizations for spec
  + dams <dams>
    - clean/update specfile
* Mon Apr 07 2014 alexl <alexl> 0.0.4-1.mga5
+ Revision: 612772
- imported package qaquarelle
* Sat May 18 2013 AlexL <loginov.alex.valer@gmail.com>
- initial packaging for Mageia
* Sun Dec 16 2012 mailaender@opensuse.org
- initial packaging (digital painting application)
