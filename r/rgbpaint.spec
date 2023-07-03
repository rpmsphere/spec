%undefine _debugsource_packages

Summary: Simple painting program for OLPC
Name: rgbpaint
Version: 0.8.7
Release: 1
License: GPL
Group: Applications/Multimedia
URL: https://mtpaint.sourceforge.net/rgbpaint.html
Source: https://downloads.sourceforge.net/mtpaint/%{name}-%{version}.tar.bz2
Source1: %{name}.png
BuildRequires: gtk2-devel

%description
rgbPaint is much simpler than mtPaint, with no menus for example.
Also it is only able to edit and save RGB images. It is a GTK+2
only program, and uses the pixbuf facilities for file handling
so it does not depend on file libraries like mtPaint does, i.e.
libpng, libjpeg, libtiff, and libungif/giflib. 

%prep
%setup -q
sed -i 's|-s|-lX11 -lm -s -Wl,--allow-multiple-definition|' configure

%build
%configure man intl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall BIN_INSTALL=%{buildroot}%{_bindir} MT_MAN_DEST=%{buildroot}%{_mandir}/man1 MT_LANG_DEST=%{buildroot}%{_datadir}/locale MT_PREFIX=%{buildroot}/usr

install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/rgbpaint.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=rgbPaint
Name[zh_TW]=紅綠藍繪圖
GenericName=Image Editor
Comment=Simple painting program for OLPC
Comment[zh_TW]=rgbPaint 簡易像素繪圖 
Exec=rgbpaint
Icon=rgbpaint
Terminal=false
Categories=Graphics;2DGraphics;RasterGraphics;GTK;
EOF

%clean
rm -rf %{buildroot}

%files
%doc COPYING NEWS README
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.7
- Rebuilt for Fedora
