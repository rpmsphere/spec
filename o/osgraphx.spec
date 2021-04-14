%undefine _debugsource_packages

Name: osgraphx
Summary: A 3D file viewer based on openscenegraph
Version: 1.0.0
Release: 28.1
Group: Applications/Multimedia
License: GPLv2
URL: http://sourceforge.net/projects/osgraphx/
Source0: http://sourceforge.net/projects/%{name}/files/%{version}/osGraphX-%{version}.zip
BuildRequires: dos2unix
BuildRequires: qt4-devel
BuildRequires: OpenSceneGraph-qt-devel

%description
osGraphX is a 3D file viewer. Based on openscenegraph, it can load all the OSG
supported file formats.

%prep
%setup -q -n osGraphX-%{version}
dos2unix tounix.sh
sh ./tounix.sh
sed -i '1i #include <unistd.h>' src/MiscFunctions.cpp
sed -i 's|(osg::Geometry::BIND_PER_PRIMITIVE)|(osg::Geometry::BIND_PER_PRIMITIVE_SET)|' src/scene/SceneView.cpp
sed -i 's|!geom->areFastPathsUsed()|true|' src/3rdparty/osgWorks/osgwTools/CountsVisitor.cpp

%build
cd build
qmake-qt4 -recursive INSTALL_PREFIX=$RPM_BUILD_ROOT/usr osGraphX.pro
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
cd build
make install

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=osGraphX
Comment=A 3D file viewer based on openscenegraph
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF
# remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/*.txt

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man*/*

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
