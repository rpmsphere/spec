%global debug_package %{nil}

Summary: Window Manager based on twm with virtual screen
Name: vtwm
Version: 5.5.0
Release: 9.1
Source0: vtwm-snap.tar.gz
License: MIT
Group: Graphical desktop/Other
BuildRequires:	libX11-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imake
BuildRequires:	libXpm-devel
BuildRequires:	libXext-devel
BuildRequires:	libXt-devel
BuildRequires:	libXmu-devel
BuildRequires:	flex-static
#BuildRequires:  rplay-devel
URL: http://www.vtwm.org/
BuildRequires:	libXft-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXinerama-devel

%description
Twm is make by the Xconsortium and it is included with Xfree Package,
but it is very light. Vtwm is an extension of twm.
It implements some extensions such as virtual desktop.   
It mimic Windows(tm) look and feel.

%prep
%setup -q -n vtwm-20130906
sed -i -e 's|XCOMM NO_SOUND_SUPPORT|NO_SOUND_SUPPORT|' -e 's|^SOUND|XCOMM SOUND|' Imakefile

%build
xmkmf -a
make

%install
%make_install

# session stuff
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xsessions
cat > $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment=An extension of twm
TryExec=%{name}
Exec=%{name}
Type=Xsession
EOF

rm -rf $RPM_BUILD_ROOT/usr/lib/X11/doc/html/vtwm.1.html
#mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_mandir}

%files
%{_datadir}/xsessions/%{name}.desktop
#config(noreplace) /usr/lib/X11/twm/system.vtwmrc
%config(noreplace) /usr/share/X11/vtwm/system.vtwmrc
%_bindir/vtwm
%_mandir/man1/vtwm.1x.*

%changelog
* Mon Mar 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 5.5.0
- Rebuild for Fedora
* Tue Nov 15 2005 Olivier Thauvin <nanardon@zarb.org> 5.4.7-1plf
- 5.4.7
* Sat Oct 08 2005 Stefan van der Eijk <stefan@zarb.org> 5.4.6b-2plf
- BuildRequires: xorg-x11 for rman
- remove unpackaged file
- %%mkrel
* Sun Oct 17 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.6b-1plf
- 5.4.6b
* Thu Sep 02 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.6a-1plf
- 5.4.6a
- plf reason
- remove vendor from spec
* Thu Apr 25 2002 Stefan van der Eijk <stefan@eijk.nu> 5.4.6-3plf
- BuildRequires
* Thu Mar 14 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.6-2plf
- plf package
* Wed Mar 13 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.6-2mdk
- Fix typo
* Sun Mar 10 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.4.6-1mdkot
- First mdk release
