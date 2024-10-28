Summary:        A GTK front-end for CUPS
Name:           gtklp
Version:        1.3.4
Release:        1
License:        GPLv2+
Group:          System/Printing
Source0:        https://prdownloads.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
URL:            https://gtklp.sourceforge.net/
Source1:        gtklp.png
Patch1:         gtklp-1.2.5-mdv-fix-str-fmt.patch
BuildRequires:  gtk2-devel
BuildRequires:  cups-devel
Requires:       cups

%description
A GTK front-end for CUPS.

%prep
%setup -q
#patch1 -p1 -b .strfmt
sed -e '/DEF_BROWSER_CMD/{s:netscape:firefox:}' \
        -e '/DEF_HELP_HOME/{s:631/sum.html#STANDARD_OPTIONS:631/help/:}' \
        -i include/defaults.h

%build
export LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -fi
%configure --enable-forte
sed -i 's|-Werror=format-security|-Wno-error|' libgtklp/Makefile
make

%install
mkdir -p %{buildroot}/%{_datadir}/applications/
%make_install

# menu entry
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Categories=HardwareSettings;Settings;GTK;
Name=GTK CUPS
Comment=GTK Frontend for CUPS
Exec=gtklp
Icon=gtklp
EOF

cat << EOF > %buildroot%{_datadir}/applications/gtklpq.desktop
[Desktop Entry]
Type=Application
Categories=HardwareSettings;Settings;GTK;
Name=GTK Printer Queue
Comment=GTK Frontend to GTKlp CUPS Queue
Exec=gtklpq
Icon=gtklp
EOF

# menu icon
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# locales
%find_lang %name

%files -f %name.lang
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO USAGE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 1.3.0-4.mga5
+ Revision: 744904
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.3.0-3.mga5
+ Revision: 680022
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 1.3.0-2.mga4
+ Revision: 527545
- Mageia 4 Mass Rebuild
* Sun Jun 09 2013 fwang <fwang> 1.3.0-1.mga4
+ Revision: 441088
- new version 1.3.0
* Mon Jan 21 2013 malo <malo> 1.2.9-3.mga3
+ Revision: 390317
- updated RPM group
* Sat Jan 12 2013 umeabot <umeabot> 1.2.9-2.mga3
+ Revision: 352898
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Aug 23 2012 fedya <fedya> 1.2.9-1.mga3
+ Revision: 283258
- missed dot in descr
- imported package gtklp
