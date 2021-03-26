Name:           grafx2
Version:        2.4
Release:        7.1
Summary:        Ultimate 256-color bitmap paint program
Group:          Graphics/Editors and Converters
License:        GPLv2+
URL:            http://pulkomandy.tk/projects/GrafX2
Source0:        %{name}-%{version}.2035-src.tgz
Patch0:         grafx2-2.4-mga-hicolor-icon.patch
Patch1:         grafx2-2.4-mga-desktop.patch
BuildRequires:  dos2unix
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(zlib)

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs Deluxe
Paint and Brilliance. Specialized in 256-color drawing, it includes a very
large number of tools and effects that make it particularly suitable
for pixel art, game graphics, and generally any detailed graphics painted
with a mouse.

%prep
%setup -q -n %{name}
%autopatch -p1
dos2unix doc/README.txt

%build
make -C src

%install
%makeinstall -C src
install -D -m644 misc/unix/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/README.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuild for Fedora
* Tue Feb 09 2016 umeabot <umeabot> 2.4-2.mga6
+ Revision: 952572
- Mageia 6 Mass Rebuild
* Wed Mar 04 2015 akien <akien> 2.4-1.mga5
+ Revision: 817669
- imported package grafx2
  
