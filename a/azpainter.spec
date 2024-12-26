%undefine _debugsource_packages

Name:           azpainter
Version:        3.0.9a
Release:        1
Summary:        Painting software
License:        GPL3.0+
Group:          Productivity/Graphics/Other
URL:            https://osdn.net/projects/azpainter
#Source:         https://osdn.net/projects/azpainter/downloads/71988/%{name}-%{version}.tar.xz
Source0:        https://gitlab.com/azelpg/azpainter/-/archive/v%{version}/azpainter-v%{version}.tar.gz
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
Full color painting software for Linux for illustration drawing.
This is not suitable for dot editing.

%prep
%setup -q -n %{name}-v%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
#autoreconf -fiv
./configure --prefix=/usr
#make %{?_smp_mflags}
cd build
ninja

%install
#make_install
cd build
%ninja_install
cp ../AUTHORS ../ChangeLog %{buildroot}%{_docdir}/%{name}

%post
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%postun
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}3
%{_datadir}/icons/hicolor/*/apps/*%{name}*.??g
%{_datadir}/mime/packages/%{name}.xml
#license GPL3

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.9a
- Rebuilt for Fedora
