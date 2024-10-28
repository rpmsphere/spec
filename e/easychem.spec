%undefine _debugsource_packages

Name:           easychem
Summary:        2D molecular drawing program
Version:        0.6
Release:        15.1
Source0:        https://puzzle.dl.sourceforge.net/sourceforge/easychem/%{name}-%{version}.tar.bz2
Source1:        easychem.png
Patch0:         easychem-0.6-link.patch
URL:            https://easychem.sourceforge.net/
License:        GPL
Group:          Sciences/Chemistry
BuildRequires:  gtk2-devel

%description
EasyChem is a program designed to draw chemical molecules.  The problem in all
existing programs is: they intend to be easy to use at first try, kind of a
quick-and-dirty approach. EasyChem would be a bit difficult to learn, but when
you master it, you can be very fast, and with a huge precision. In fact, it's
just like a specialized vectorial drawing tool.

%prep
%setup -q
%patch 0 -p0

%build
make -f Makefile.linux CC="gcc %optflags"
                                                                                
%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=EasyChem
Comment=2D Molecule Editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Education;Science;Chemistry;
EOF

install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING
%{_bindir}/%name
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Sat Dec 08 2012 fwang <fwang> 0.6-7.mga3
+ Revision: 328046
- apply patch
- fix linkage
* Mon Sep 19 2011 fwang <fwang> 0.6-6.mga2
+ Revision: 145290
- rebuild
* Sat May 14 2011 dmorgan <dmorgan> 0.6-5.mga2
+ Revision: 98735
- imported package easychem
