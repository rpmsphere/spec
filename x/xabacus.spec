Name:          xabacus
Version:       8.0.3
Release:       22.1
Summary:       An implementation of the classic Chinese abacus
Group:         Applications/Educational
URL:           http://www.tux.org/~bagleyd/abacus.html
Source:        http://www.tux.org/~bagleyd/abacus/%{name}-%{version}.tar.xz
License:       BSD
BuildRequires: audiofile-devel
BuildRequires: esound-devel
BuildRequires: libICE-devel
BuildRequires: motif-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: libXt-devel

%description
There are books on how to use an abacus, but basically all it does is
add and subtract, the rest you have to do in your head.  Essentially,
this is a proof by induction that a computer is more powerful than an
abacus, since a computer program can contain an abacus. (But then
again, you can simulate a computer within a computer, so what does that
show). Actually, with a real abacus, one can move more than one row at
a time with 10 fingers.  But on the other hand, a real abacus does not
have the current sum displayed as an integer.

%prep
%setup -q 

%build
export LIBS=-laudiofile
%configure
make

%install
rm -rf %{buildroot}
%make_install
sed -i 's|%{buildroot}||' %{buildroot}/usr/openwin/lib/app-defaults/Abacus
mkdir -p %{buildroot}/usr/lib/X11/app-defaults
mv %{buildroot}/usr/openwin/lib/app-defaults/Abacus %{buildroot}/usr/lib/X11/app-defaults/

#make install-png
for i in 16x16 22x22 32x32 48x48; do
install -Dc -m 644 pixmaps/$i/abacus.png %{buildroot}%{_datadir}/icons/hicolor/$i/apps/abacus.png
done

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=XAbacus
Comment=Implementation of classical abacus
Exec=xabacus
Icon=abacus
Terminal=false
Type=Application
Categories=Education;Science;Math;
EOF

%clean
rm -rf %{buildroot}

%files
%doc README
%{_bindir}/*
/usr/lib/X11/app-defaults/*
%{_datadir}/games/xabacus
%{_datadir}/icons/hicolor/*/apps/abacus.png
%{_datadir}/applications/xabacus.desktop
%{_mandir}/man6/*

%changelog
* Sat May 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 8.0.3
- Rebuilt for Fedora
* Mon Feb 07 2011 Automatic Build System <autodist@mambasoft.it> 7.6.8-1mamba
- automatic update by autodist
* Sun Oct 03 2010 Automatic Build System <autodist@mambasoft.it> 7.6.7-1mamba
- automatic update by autodist
* Mon Aug 16 2010 Automatic Build System <autodist@mambasoft.it> 7.6.4-1mamba
- automatic update by autodist
* Wed Jul 07 2010 Automatic Build System <autodist@mambasoft.it> 7.6.2-1mamba
- automatic update by autodist
* Sun Feb 07 2010 Automatic Build System <autodist@mambasoft.it> 7.6-1mamba
- automatic update by autodist
* Mon Oct 26 2009 Automatic Build System <autodist@mambasoft.it> 7.5.3-1mamba
- automatic update by autodist
* Tue Oct 13 2009 Automatic Build System <autodist@mambasoft.it> 7.5.2-1mamba
- automatic update by autodist
* Sat Aug 15 2009 Automatic Build System <autodist@mambasoft.it> 7.5.1-1mamba
- automatic update by autodist
* Tue Jan 13 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 7.4.1-1mamba
- automatic update by autodist
* Fri Aug 29 2008 Tiziana Ferro <tiziana.ferro@email.it> 7.4-1mamba
- update to 7.4
- update system menu entry
- add buildrequirements
* Tue Jul 12 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 7.1.3-1qilnx
- package created by autospec
