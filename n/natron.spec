%undefine _debugsource_packages
%define oname Natron

Summary:	Nodal video compositing software
Name:		natron
Version:	2.3.4git
Release:	2.1
License:	MPLv2+
Group:		Video
URL:		https://github.com/MrKepzie/Natron
Source0:	%{oname}-master.zip
BuildRequires:	ghostscript-core
BuildRequires:	ImageMagick
BuildRequires:	boost-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gl)
#BuildRequires:	glew1-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	python-pyside-devel
BuildRequires:	shiboken-devel

%description
Natron is a free open-source video compositing software, similar in
functionality to Adobe After Effects or Nuke by The Foundry.

Features:
- 32 bits floating point linear colour processing pipeline.
- Colorspace management handled by the famous open-source OpenColorIO library.
- Dozens of file formats supported: EXR, DPX, TIFF, JPG, PNG etc.
- Support for many free and open-source OpenFX plugins.

%prep
%setup -q -n %{oname}-master
cat > config.pri << EOF
boost: LIBS += -lboost_system -lboost_thread -lboost_serialization
pyside: INCLUDEPATH += /usr/include/PySide/QtCore /usr/include/PySide/QtGui
EOF
sed -i 's|\$\$system(pkg-config --variable=libdir cairo)/libcairo.a|-lcairo|' global.pri
sed -i 's|boost/utility.hpp|boost/next_prior.hpp|' libs/yaml-cpp/include/yaml-cpp/node/detail/iterator.h

%build
qmake-qt4
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 App/%{oname} %{buildroot}%{_bindir}/%{name}

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Natron
Comment=Nodal video compositing software
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;AudioVideoEditing;
EOF

# install menu icons
for N in 16 32 48 64 128 256;
do
convert Gui/Resources/Images/natronIcon256_linux.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_datadir}/icons/hicolor/${N}x${N}/apps/%{name}.png
done

%files
%doc BUGS.md CHANGELOG.md CONTRIBUTORS.txt LICENSE.txt README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jan 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.4git
- Rebuilt for Fedora
* Sun Jul 26 2015 abfonly <abfonly@gmail.com> 1.2.1-1
- (99d86ea) Log: Update to 1.2.1, drop all external sources and patches, use internal gits
