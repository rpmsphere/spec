%undefine _debugsource_packages
%global __arch_install_post %{nil}

Name:          giv
Version:       0.9.35
Release:       1
Summary:       The G(reat|tk|NU) Image Viewer
Group:         Applications/Graphics
URL:           http://giv.sourceforge.net/giv/
Source0:       http://downloads.sourceforge.net/giv/giv-%{version}.tar.gz
License:       GPL
BuildRequires: cairo-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: pcre-devel
BuildRequires: cfitsio-devel
BuildRequires: git
BuildRequires: glm-devel

%description
giv, The G(reat|tk|NU) Image Viewer, is an image and vector overlay viewer.

Features:
* Based on the gtk_image_viewer widget and can thus deal with huge images at large
  zoom ins.
* Defines a simple ascii-based format for drawing vector overlays on top of the image.
  Great for Vision application.
* The display of datasets are highly customizable including line widths, marks, color
  names according to x11 database, hierarchical paths.
* Easily deals with vector sets of several million vectors.
* User defined popups when the mouse hovers over a dataset.
* A tree based dataset viewer for turning on and off the display of part of the vector
  data.

%package devel
Summary: Development files for the package giv

%description devel
Development files for the package giv.

%prep
%setup -q
#sed -i '1368d' src/agg/agg_renderer_outline_aa.h

%build
./autogen.sh --prefix=/usr
sed -i 's|-Werror=format-security||' `find . -name Makefile`
make

%install
%make_install
install AUTHORS BUGS COPYING ChangeLog NEWS README TODO %{buildroot}%{_datadir}/doc/%{name}/
install -Dm644 doc/giv-logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=GIV
Comment=Great Image Viewer
Exec=giv
Icon=giv
Type=Application
Terminal=false
Categories=Application;Graphics;
EOF

%files
%{_bindir}/%{name}*
%{_libdir}/%{name}*
%{_libdir}/lib*.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/doc/%{name}

%files devel
%{_includedir}/*/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.35
- Rebuilt for Fedora
* Fri Apr 03 2009 gil <puntogil@libero.it> 0.9.14-1mamba
- package created by autospec
