%global debug_package %{nil}

Name:           azdrawing
Version:        1.5
Release:        1
Summary:        Drawing software
License:        GPL3.0+
Group:          Productivity/Graphics/Other
URL:            https://osdn.net/projects/azdrawing
Source:         https://osdn.net/projects/azdrawing/downloads/63500/%{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xft)
BuildRequires:  desktop-file-utils

%description
A painting software for line drawings and monochrome cartoons.

%prep
%setup -q
sed -i 's|-Wall|-Wall -Wno-narrowing|' Makefile

%build
make %{?_smp_mflags}

%install
%make_install prefix=%{buildroot}/usr

%post
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%postun
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%files
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*%{name}*.??g
%exclude /usr/share/icons/hicolor/icon-theme.cache
%license LGPL GPL

%changelog
* Mon Dec 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora
