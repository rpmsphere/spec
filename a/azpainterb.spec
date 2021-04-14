%undefine _debugsource_packages

Name:           azpainterb
Version:        1.1.3b1
Release:        1
Summary:        Painting software for dot editing
License:        GPL3.0+
Group:          Productivity/Graphics/Other
URL:            https://osdn.net/projects/azpainterb
Source:         https://osdn.net/projects/azpainterb/downloads/71050/%{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils

%description
Paint software for Linux which can be used for various purposes such as
dot editing, illustration, retouching, etc. You can sense pen pressure
with XInput2. Layer color fixed to 8bit RGBA.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
#autoreconf -fiv
./configure --prefix=/usr
make %{?_smp_mflags}

%install
%make_install
#mv %{buildroot}%{_datadir}/mime/packages/azpainter.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%post
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
#{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%postun
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
#{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%files
%doc AUTHORS ChangeLog README README_ja
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
#{_datadir}/mime/packages/%{name}.xml
%license GPL3

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3b1
- Rebuilt for Fedora
