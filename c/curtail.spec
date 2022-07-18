Name:           curtail
Version:        1.3.0
Release:        8
Summary:        A simple and useful image compressor
License:        GPL-3.0-or-later
URL:            https://github.com/Huluti/curtail
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig(glib-2.0)
Requires:       jpegoptim
Requires:       libwebp-tools
Requires:       optipng
Requires:       pngquant
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
Curtail (previously ImCompressor) is an useful image compressor, supporting
PNG, JPEG and WEBP file types. It support both lossless and lossy compression
modes with an option to whether keep or not metadata of images.

%prep
%setup -q -n Curtail-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/curtail
%{_datadir}/metainfo/*.xml
%{_datadir}/curtail
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/locale/*/LC_MESSAGES/curtail.mo

%changelog
* Sun Jun 19 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Sun May  1 2022 Atri Bhattacharya <badshah400@gmail.com>
- Update to version 1.3.0:
  * Add option to preserve file attributes if possible.
  * Update image libraries.
  * Updated translations.
* Tue Dec  7 2021 Atri Bhattacharya <badshah400@gmail.com>
- Update to version 1.2.2:
  * Updated translations.
* Fri Aug 27 2021 Atri Bhattacharya <badshah400@gmail.com>
- Actually add the rpmlintrc file to sources.
- BuildArch: noarch as recommended by rpmlint.
* Fri Aug 27 2021 Atri Bhattacharya <badshah400@gmail.com>
- Initial package.
- Add %%{name}-rpmlintrc to suppress explicit-lib-dependency
  trigerred for libwebp-tools Requires.
