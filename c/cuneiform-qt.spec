Name:           cuneiform-qt
Version:        0.1.2
Release:        4.1
Summary:        GUI frontend for Cuneiform OCR
License:        GPLv3+
Group:          Productivity/Graphics/Other
URL:            https://www.altlinux.org/Cuneiform-Qt
Vendor:         Andrey Cherepanov <cas@altlinux.org>
Source:         %name-%version.tar.bz2
BuildRequires:  gcc-c++, pkgconfig, pkgconfig(QtGui)
Requires:       cuneiform

%description
This application is GUI frontend for Cuneiform (OCR system originally
developed and open sourced by Cognitive technologies). It allow to open
scanned image, view this one in preview pane, recornize text via Cuneiform
and save result in HTML file.

%prep
%setup -q

%build
%define qtbindir `pkg-config --variable=exec_prefix QtCore`/bin
pushd %{name}
PREFIX=/usr %{qtbindir}/qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %{name}.pro
%{__make}
popd

%install
pushd %{name}
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT
install -D -m 644 icons/%{name}.png $RPM_BUILD_ROOT{_datadir}/pixmaps/%{name}.png
popd

%files
%doc %{name}/AUTHORS %{name}/README %{name}/TODO
%{_bindir}/%{name}
%{_datadir}/apps
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
* Mon Feb 07 2011 Petr Vanek <petr@scribus.info> 0.1.2
- suse fixes
* Sat May 09 2009 TI_Eugene <ti.eugene@gmail.com> 0.1.2
- Initial build for OBS
