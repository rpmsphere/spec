%define oname playmymusic

Name:           melody
Version:        2.2.1
Release:        1
Summary:        Music player for Linux
Group:          Sound
License:        GPLv3+
URL:            https://github.com/artemanufrij/playmymusic
Source0:        %{oname}-%{version}.tar.xz
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: libgee-devel
BuildRequires: granite-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: pango-devel
BuildRequires: libsoup-devel
BuildRequires: sqlite-devel
BuildRequires: taglib-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: vala

%description
Music player for Linux.

%prep
%setup -qn %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install --vendor="" \
    --remove-category="AudioVideo" \
    --remove-category="Player" \
    --add-category="X-MandrivaLinux-Multimedia-Sound" \
	--dir %buildroot%{_datadir}/applications \
	%buildroot%{_datadir}/applications/*.desktop

%find_lang com.github.artemanufrij.playmymusic

%files -f com.github.artemanufrij.playmymusic.lang
%{_bindir}/com.github.artemanufrij.playmymusic
%{_datadir}/applications/com.github.artemanufrij.playmymusic.desktop
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.playmymusic.gschema.xml
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/com.github.artemanufrij.playmymusic.appdata.xml

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuild for Fedora
* Mon Sep 07 2020 tex - 2.2.1-1pclos2020
- create pkg
