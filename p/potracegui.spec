%undefine _debugsource_packages

Summary:        GUI interface for potrace
Name:           potracegui
Version:        1.3.4
Release:        18.1
License:        GPL
Group:          Applications/Graphics
URL:            https://potracegui.sourceforge.net/
Source0:        https://prdownloads.sourceforge.net/potracegui/%name-%version.tar.bz2
Source1:        %name-icons.tar.bz2
Patch0:         %{name}-1.3.4-gcc43.patch
Patch1:         %{name}-1.3.4-pixelview.patch
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++
BuildRequires:	kdelibs-common
BuildRequires:  libX11-devel
BuildRequires:  kdelibs3-devel
Requires: 	potrace

%description
Potracegui is a GUI interface for potrace, a great program for tracing 
bitmapped images.

%prep
%setup -q -a 1
%patch0 -p0
%patch1 -p1

%build
export CXXFLAGS="-std=c++98 -fPIC"
%configure
sed -i 's|-Wl,--as-needed||' config* Makefile */Makefile */*/Makefile
%__make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# icon
install -D -m 644 %{name}-32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 644 %{name}-16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

%find_lang %name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Terminal=false
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Graphics;Viewer;
Name=PotraceGUI
Comment=GUI interface for potrace
EOF

rm -rf %buildroot%{_datadir}/applnk %buildroot%{_datadir}/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%doc COPYING README INSTALL AUTHORS
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/doc/HTML/en/potracegui/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4
- Rebuilt for Fedora
* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3.4-5mdv2008.1
+ Revision: 135450
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import potracegui
* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.4-5mdk
- Fix BuildRequires
* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.4-4mdk
- Fix BuildRequires
* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.4-3mdk
- Fix BuildRequires
* Tue Apr 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.4-2mdk
- Fix BuildRequires
- use mkrel
- Fix Menu section thanks pterjan
* Wed Jul 20 2005 Lenny Cartier <lenny@mandriva.com> 1.3.4-1mdk
- 1.3.4
* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1-1mdk
- 1.1
* Sat Jan 18 2003 Blaise Tramier <meles@free.fr> 1.0-1mdk
- first mdk package
