Summary: Gnome KiSS viewer
Name: gnomekiss
Version: 2.0
Release: 1
Source0: %{name}-%{version}.tar.gz
Source1: gnomekiss.desktop
URL: http://devel.tlrmx.org/kiss/
License: GPL
Group: Amusements/Games
Requires: lha

%description
GnomeKiSS is a viewer for all KiSS paper dolls. Cherry KiSS and Enhanced
Palette are supported, with full alpha transparency and FKiSS.

%prep
%setup -q
%{__cp} %{SOURCE1} .

%build
%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
sed -i 's|@datadir@|%{_datadir}/pixmaps/%{name}/|g' %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%{_bindir}/gnomekiss
%{_datadir}/applications/gnomekiss.desktop
%{_datadir}/pixmaps/gnomekiss/gnome-kiss.png
%{_datadir}/pixmaps/gnomekiss/besito_sinfondo.png
%{_mandir}/man1/*
%doc COPYING doc/COMPATIBILITY AUTHORS README NEWS ChangeLog

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Tue Sep 16 2008 Wind Win <yc.yan@ossii.com.tw> 2.0-4
- Append requirement(gnomekiss need lha to open *.lhz file) for application running.
* Tue Sep 11 2008 Wind Win <yc.yan@ossii.com.tw> 2.0-3
- Rebuild for OSSII.