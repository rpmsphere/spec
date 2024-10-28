Summary: Train Control for DCC++
Name: traincontrol
Version: 1.7
Release: 1
License: GPLv2
URL: https://www.theknight.co.uk
Group: Applications/Productivity
Source: https://www.theknight.co.uk/releases/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig desktop-file-utils gcc libxml2-devel gtk3-devel systemd

%description
Control DCC trains and layout.

%prep
%setup -q

%build
%configure 
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/train
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 755 traincontrol $RPM_BUILD_ROOT%{_bindir}/
install -p -m 755 traincalc $RPM_BUILD_ROOT%{_bindir}/traincalc
install -p -m 755 traindaemon $RPM_BUILD_ROOT%{_bindir}/traindaemon
install -p -m 755 pointdaemon $RPM_BUILD_ROOT%{_bindir}/pointdaemon
install -p -m 755 pointtest $RPM_BUILD_ROOT%{_bindir}/pointtest
install -p -m 644 traincontrol.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/traincontrol.svg
install -p -m 644 traincontrol.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/traincontrol.png
install -m 644 trackrc.xml $RPM_BUILD_ROOT%{_sysconfdir}/train/trackrc.xml
install -m 644 track.xml $RPM_BUILD_ROOT%{_sysconfdir}/train/track.xml
install -m 644 points.xml $RPM_BUILD_ROOT%{_sysconfdir}/train/points.xml
install -m 644 system/traindaemon.service $RPM_BUILD_ROOT%{_unitdir}/traindaemon.service
install -m 644 system/pointdaemon.service $RPM_BUILD_ROOT%{_unitdir}/pointdaemon.service
desktop-file-install --vendor="" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications traincontrol.desktop

%files
%{_bindir}/traincontrol
%{_bindir}/traincalc
%{_bindir}/traindaemon
%{_bindir}/pointdaemon
%{_bindir}/pointtest
%{_datadir}/pixmaps/traincontrol.svg
%{_datadir}/pixmaps/traincontrol.png
%{_datadir}/applications/traincontrol.desktop
%{_unitdir}/traindaemon.service
%{_unitdir}/pointdaemon.service
%config(noreplace) %{_sysconfdir}/train/trackrc.xml
%config(noreplace) %{_sysconfdir}/train/track.xml
%config(noreplace) %{_sysconfdir}/train/points.xml

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Thu May 9 2019 Chris Knight <chris@theknight.co.uk> 1.1-1
- Much work done towards a beta release.
* Fri Nov 30 2018 Chris Knight <chris@theknight.co.uk> 1.0.0-1
- Fixes to the build and distribution system.
