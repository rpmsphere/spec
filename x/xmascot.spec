%undefine _debugsource_packages

Name: xmascot
Summary: Moving mascot on your X-Window screen
Version: 2.6a
Release: 1
Group: Amusements/Games
License: free
URL: http://cclub-flying.dsl.gr.jp/products/xmascot/
Source0: http://cclub-flying.dsl.gr.jp/products/%{name}/%{name}%{version}.tar.gz
BuildRequires: libXaw-devel libXmu-devel libXt-devel libXext-devel

%description
XMascot, moving mascot on your X-Window screen.
XMascot have these features:
-Moving pretty mascot moving
-Strectch       stretch as you like
-Talking        mascot talks with extract command and data
-Alarm          mascot may make some actions at time you define
-BIFF           mascot may let you know arriving a mail.
XMascot supports these image formats:
MAG     *.mag   16 colors and 256 colors
TIFF    *.tif   16 colors and 256 colors, in raw or lzw
PPM     *.ppm   256 level color , in raw
PGM     *.pgm   256 level gray scale, in raw
PBM     *.pbm   2 level monochrome, in raw
PNM     *.pnm   PPM, PGM, or PBM
XMascot distinguish images from their suffix and can load other image formats
when {suffix}topnm, *topgm, or *topbm commands are found in your system.

%prep
%setup -q -n %{name}%{version}
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Imakefile

%build
xmkmf -a
make %{?_smp_mflags}

%install
make install install.man DESTDIR=%{buildroot}

%files
%doc ChangeLog README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%exclude /usr/lib/X11/C/app-defaults/XMascot
%exclude /usr/lib/X11/app-defaults
%{_datadir}/X11/app-defaults/XMascot
/usr/lib/X11/%{name}

%changelog
* Tue Dec 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6a
- Rebuilt for Fedora
